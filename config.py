import os
import dotenv

dotenv.load_dotenv()

class Settings:
    TG_TOKEN: str = os.getenv("TG_BOT_TOKEN")


settings = Settings()