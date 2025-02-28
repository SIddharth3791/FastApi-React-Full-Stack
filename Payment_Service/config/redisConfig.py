from redis_om import get_redis_connection
import os
from dotenv import load_dotenv

load_dotenv()

class RedisConfig():
    def __init__(self):
        self.host = os.getenv("REDIS_HOST")
        self.port = os.getenv("REDIS_PORT")
        self.password = os.getenv("REDIS_PSWD")
        self.decode_responses=True
        self._redis_conn = None

    def redisConnection(self):
        if self._redis_conn is None:
            self._redis_conn = get_redis_connection(
                host =  self.host,
                port =  self.port,
                password =  self.password,
                decode_responses= self.decode_responses
            )
        return self._redis_conn

redis_config = RedisConfig()
redis = redis_config.redisConnection()