from sqlalchemy import Column, BigInteger, String, sql
from sqlalchemy.sql import expression

from utils.db_api.db_gino import TimedBaseModel, db, BaseModel

class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    name = Column(String(200), primary_key=True)
    update_name = Column(String(50), primary_key=True)

    quary: sql.select