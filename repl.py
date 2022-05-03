# https://gist.github.com/benkehoe/2e6a08b385e3385f8a54805c99914c75
# adapted from benkehoe's gist

import argparse
import sys, os.path, re
import fetch

parser = argparse.ArgumentParser()

parser.add_argument("--roll", action="store_true", help="Roll 10s again")
parser.add_argument("--nines", action="store_true", help="Roll 10s, 9s again")
parser.add_argument("--eights", action="store_true", help="Roll 10s, 9s, 8s again")
parser.add_argument("--rote", action="store_true", help="Roll failures again (ONCE)")
parser.add_argument("--flip", action="store_true", help="Flip a coin")
parser.add_argument("--pool", "-p", type=int, help="Size of dice pool")
parser.add_argument("--difficulty", "-d", default='8', type=int, help="Lowest successful roll")

class InvalidArgs(Exception):
    pass

def exit(*args, **kwargs):
    print("Invalid arguments")
    raise InvalidArgs

parser.exit = exit

def main_loop():
        # readline adds capabilities to input
        try:
            import readline
        except:
            pass

        print("Enter commands. Use 'help' for info, 'exit' to leave.")
        while True:
            try:
                command = input('> ').strip()
                
                # remove the program name if they typed it
                prog_name = os.path.basename(sys.argv[0])
                command = re.sub(r'^{}\s+'.format(prog_name), '', command)
            except KeyboardInterrupt:
                # Ctrl-c clears the input
                sys.stdout.write('\n')
                continue
            except EOFError:
                # Ctrl-d exits
                sys.stdout.write('\n')
                break

            if command == 'exit':
                break

            if command in ['help', 'h', '?']:
                parser.print_help()
                continue

            try:
                command_args = parser.parse_args(args=command.split())
            except InvalidArgs:
                print('Invalid command')
                continue
            
            pool_size, difficulty= int(command_args.pool), int(command_args.difficulty)
            pool = fetch.Pool(pool_size, difficulty)

            if command_args.roll:
                pool.ten_again()
            elif command_args.nines:
                pool.nine_again()
            elif command_args.eights:
                pool.eight_again()
            elif command_args.rote:
                pool.rote()
            
            print(pool)

if __name__ == "__main__":
    main_loop()