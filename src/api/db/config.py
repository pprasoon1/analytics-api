from decouple import config as decoupple_config

DATABASE_URL = decoupple_config("DATABASE_URL", default="")
