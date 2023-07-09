# product_bot
Написание асинхронного бота для интернет магазина. 

  Архитектура бота заключается в выборе товара с помощью кнопок в menu_heandlers.py, где клиент при выборе товара перемещается по кнопкам до онлайн - покупки. 
  Данные вносятся с помощью асинхронной ORM GINO, построенная поверх ядра SQLAlchemy, поддерживающая PostgreSQL(asyncpg) для Python asyncio.
Использованный стак: 
- python 3.10; 
- asyncio / aiohttp / aioredis; 
- PostgreSQL/gino/SQLAlchemy;
- docker-compose.
