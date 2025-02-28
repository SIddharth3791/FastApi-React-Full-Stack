
from redis_om import HashModel
from config.redisConfig import redis

class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str # Pending, Completed, Refresh

    class Meta:
        database = redis