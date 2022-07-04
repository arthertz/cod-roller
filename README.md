# Fetch
## A chronicles of darkness roller and dice bot
Fetch can be used either as a python library for making Chronicles of Darkness rolls or as a Discord bot that uses the new interactions API.
Good for games like Changeling: The Lost.
### Written for python!
### Using the Repl
`python repl.py`
### Discord Bot Setup
Create a file called `config.yml` in the same directory as `bot.py`
It should be configured as shown:
```yaml
secret_token: [Your Secret Token]
guild_id: [Your Guild ID] # Guild ID has been deprecated
```

This project requires dependencies to run. These are detailed in `Pipfile`. You can use Pipenv to install them automatically (`pipenv install`), or install them yourself.

### Using the Bot

```cmd
> cd fetch-roller
> pipenv shell
> python bot.py
```
