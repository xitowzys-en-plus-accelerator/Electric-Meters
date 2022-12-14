from environs import Env

env = Env()
env.read_env()

TOLOKA_OAUTH_TOKEN = env.str("TOLOKA_OAUTH_TOKEN")
OWN_CLOUD_HOST = env.str("OWN_CLOUD_HOST")
OWN_CLOUD_ID_PRIVATE_STORAGE = env.str("OWN_CLOUD_ID_PRIVATE_STORAGE")
OWN_CLOUD_ID_PUBLIC_STORAGE = env.str("OWN_CLOUD_ID_PUBLIC_STORAGE")
OWN_CLOUD_PASSWORD_PRIVATE_STORAGE = env.str("OWN_CLOUD_PASSWORD_PRIVATE_STORAGE")
