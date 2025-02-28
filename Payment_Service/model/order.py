
from redis_om import get_redis_connection, HashModel

from model.orderStatus import OrderStatus

redis = get_redis_connection(
    host = "redis-16513.c61.us-east-1-3.ec2.redns.redis-cloud.com",
    port = 16513,
    password = "nzOgoFIy3aiacFEBDZKN8VZ5Ffx9bf3G",
    decode_responses=True
)

class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str # Pending, Completed, Refresh

    class Meta:
        database = redis