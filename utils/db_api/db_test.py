import asyncio

from utils.db_api import quick_commands as commands
from utils.db_api.db_gino import db
from data import config

async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1, "Kostya", "NO")
    await commands.add_user(4321, "K", "What")
    await commands.add_user(1234, "O", "123")
    await commands.add_user(1, "Kos", "NO")
    await commands.add_user(1, "ostya", "NO")
    await commands.add_user(1, "Kotya", "NO")

    users = await commands.select_all_users()
    print(users)

    count = await commands.count_users()
    print(count)

    user = await commands.select_user(1)
    print(user)

    await commands.update_user_name(1, "New_Kostya")

    user = await commands.select_user(1)
    print(user)

loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())