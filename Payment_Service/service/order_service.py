import time
import requests
from model.order import Order
from model.orderStatus import OrderStatus
from fastapi.background import BackgroundTasks
from model.order import redis

stream_key = "order_completed"

async def create_Order(pk:str, quantity: int, backgrount_task: BackgroundTasks):
        try:
            req = requests.get(f"http://localhost:8000/products/{pk}" )

            productDetails = req.json()
            order = Order(
                product_id = pk,
                price = productDetails['price'],
                fee = 0.2 * productDetails['price'],
                total = 1.2 * productDetails['price'],
                quantity = quantity,
                status = OrderStatus.PENDING.name
            )

            order.save()

            backgrount_task.add_task(order_completed, order)

            return order
        except Exception as err:
            print(f"ERROR When fetching Product Details for PK : {pk}")
            return f"ERROR When fetching Product Details for PK : {pk} Err : {err}"

def order_completed(order: Order):
     time.sleep(5)
     order.status = OrderStatus.COMPLETED.name
     order.save()
     checkIfRedisStreamExists()
     redis.xadd(stream_key, order.dict(), '*')

def getOrderByPkId(pk: str):
    try:
        return Order.get(pk)
    except: 
        return f"ERROR When fetching Order Details for PK : {pk}"
    
def checkIfRedisStreamExists():
     if not redis.exists(stream_key):
        redis.xadd(stream_key, {"message": "initial"})
