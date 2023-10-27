import os
from typing import Union
import contextlib
from datetime import datetime, timezone
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
import dataclasses
from dataclasses import asdict
from typing import Optional
from dotenv import load_dotenv
load_dotenv()


class Mongo(contextlib.AbstractContextManager):
    __collection__ = ""
    __db__ = ""

    def __init__(self, coll, db):
        self.__db__ = db
        self.connection_string = os.getenv('MONGO_URL')
        self.__collection__ = coll
        self.conn: Union[MongoClient, Collection, Database, None] = None

    def __enter__(self):
        self.conn = MongoClient(self.connection_string)
        self.conn = self.conn[self.__db__]
        return self.conn[self.__collection__]

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.client.close()


class Base:
    __collection__ = ""
    __db__ = ""

    def insert_record(self):
        data = asdict(self)
        data["created_at"] = datetime.now(timezone.utc)
        with Mongo(self.__collection__, self.__db__) as mongo:
            mongo.insert_one(data)
            return None

    @classmethod
    def update_record(cls, query: dict, data: dict):
        with Mongo(cls.__collection__, cls.__db__) as mongo:
            mongo.update_one(query, {"$set": data}, upsert=True)
            return None

    @classmethod
    def get_record(self, query):
        with Mongo(self.__collection__, self.__db__) as mongo:
            return mongo.find_one(query)

    @classmethod
    def get_records(cls, query):
        with Mongo(cls.__collection__, cls.__db__) as mongo:
            return mongo.find(query)


@dataclasses.dataclass
class Comments(Base):
    __db__ = "the_onahs"
    __collection__ = "comments"

    name: Optional[str] = None
    email: Optional[str] = None
    comment: Optional[str] = None
    date: Optional[str] = None
