from environs import Env, EnvValidationError
import os

env = Env()
env.read_env()

try:
    BOT_TOKEN = env.str("BOT_TOKEN")
except EnvValidationError:
    BOT_TOKEN = os.environ['BOT_TOKEN']