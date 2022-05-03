import daemon

from bot import run_bot


if __name__ == "__main__":
    with daemon.DaemonContext():
        run_bot()