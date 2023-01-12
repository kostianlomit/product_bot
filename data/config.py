import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))


admins = [
    os.getenv("ADMIN_ID"),
]

PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

ip = os.getenv("ip")

POSTGRES_URI = f"postgresql://{PGUSER}: {PGPASSWORD}@{ip}/{DATABASE}"

aiogrem_redis = {
    "host": ip,
}