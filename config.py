
from datetime import datetime
import sys

from pathlib import Path


# ABS_PATH = ''  # for win
# ABS_PATH = f'{sys.path[0]}/app/'  # for linux

ABS_PATH = Path(__file__).parent.resolve()
APP_NAME = 'fastapi auth'


# =====================================
# load config

try:

    if sys.version_info.major == 3 and sys.version_info.minor >= 11:

        import tomllib

        with open(f"{ABS_PATH}/config.toml", "rb") as f:
            config = tomllib.load(f)
    else:

        import toml  # pip install toml

        with open(f"{ABS_PATH}/config.toml", "r") as f:
            config = toml.load(f)

    # print(config)

    IND = config['utils']['console_indent']
    SECRET_KEY = config['auth']['secret_key']
    ALGORITHM = config['auth']['algorithm']
    TOKEN_NAME = config['auth']['token_name']
    SESSION_TIME = config['auth']['session_time']
    PASSWORD_SALT = config['auth']['password_salt']

    print(f'{datetime.now()} start app: {APP_NAME}')
    # print(f'{IND} python {sys.version_info.major}.{sys.version_info.minor}')
    # print(f'{IND} config loaded: OK')

except Exception as e:
    raise Exception(f'config load -> error: {e}')
