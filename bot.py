import random
import yaml
import logging
import interactions
import fetch


config = yaml.safe_load(open("config.yml"))
secret_token = config["secret_token"]
guild_id = config["guild_id"]

print(config)

logger = logging.getLogger('interactions')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='interactions.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

standard_roll_options = [
        interactions.Option(
            name="size",
            description="Dice pool size",
            type=interactions.OptionType.INTEGER,
            required=True
        ),
        interactions.Option(
            name="difficulty",
            description="Difficulty of roll (rolls below this fail)",
            type=interactions.OptionType.INTEGER,
            required=True
        )
    ]

def pool_2_embed(member, pool):
    return interactions.Embed(
        title=f"{pool.successes} Successes",
        description=str(pool),
        author=interactions.EmbedAuthor(
            name=member.nick, icon_url= user_2_avatarirl(member.user)
        )
    )

def user_2_avatarirl(user):
    user_id = user.id
    user_avatar = user.avatar
    return f"https://cdn.discordapp.com/avatars/{user_id}/{user_avatar}.png"

bot = interactions.Client(token=secret_token)

@bot.command(
    name="hug_command",
    description="Hug the bot!",
    scope=guild_id
)
async def hug_command(ctx: interactions.CommandContext):
    adverb = random.choice(["tightly", "softly", "faintly", "powerfully"])
    await ctx.send(f"*is hugged {adverb}*")
    
@bot.command(
    name="flip",
    description="Flip a coin!",
    scope=guild_id
)
async def flip(ctx: interactions.CommandContext):
    result = random.choice(["heads", "tails"])
    flip_embed = interactions.Embed(
        title="Flip",
        description=f"You flip a coin, and it comes up {result}",
        author=interactions.EmbedAuthor(
            name=ctx.member.nick,
            icon_url=user_2_avatarirl(ctx.member.user)
        )
    )
    await ctx.send(result, embeds=flip_embed)

@bot.command(
    name="roll",
    description="Basic CoD roll, reroll 10s",
    scope=guild_id,
    options = standard_roll_options
)
async def roll(ctx: interactions.CommandContext, size: int, difficulty: int):
    pool = fetch.Pool(size=size, difficulty=difficulty)
    pool.ten_again()
    embed = pool_2_embed(ctx.member, pool)
    await ctx.send(pool.comment, embeds=embed)

@bot.command(
    name="rote",
    description="Rote CoD roll-- reroll failures, but only once",
    scope=guild_id,
    options = standard_roll_options
)
async def rote(ctx: interactions.CommandContext, size: int, difficulty: int):
    pool = fetch.Pool(size=size, difficulty=difficulty)
    pool.rote()
    embed = pool_2_embed(ctx.member, pool)
    await ctx.send(pool.comment, embeds=embed)

@bot.command(
    name="nine_again",
    description="Nine again- reroll 9s and 10s for more successes",
    scope=guild_id,
    options = standard_roll_options
)
async def nine_again(ctx: interactions.CommandContext, size: int, difficulty: int):
    pool = fetch.Pool(size=size, difficulty=difficulty)
    pool.nine_again()
    embed = pool_2_embed(ctx.member, pool)
    await ctx.send(pool.comment, embeds=embed)

@bot.command(
    name="eight_again",
    description="Eight again- reroll 8s, 9s and 10s for more successes",
    scope=guild_id,
    options = standard_roll_options
)
async def eight_again(ctx: interactions.CommandContext, size: int, difficulty: int):
    pool = fetch.Pool(size=size, difficulty=difficulty)
    pool.eight_again()
    embed = pool_2_embed(ctx.member, pool)
    await ctx.send(pool.comment, embeds=embed)

def run_bot():
    bot.start()