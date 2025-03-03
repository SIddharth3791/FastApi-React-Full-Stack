
from fastapi import BackgroundTasks, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from service.order_service import create_Order, getOrderByPkId
import faulthandler

faulthandler.enable()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
  allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    )

@app.get("/orders/{pk}")
def getOrderByPk(pk: str):
    return getOrderByPkId(pk)


@app.post("/orders")
async def createOrder(request: Request, backgrount_task: BackgroundTasks):
    body = await request.json()
    return await create_Order(body["id"], body["quantity"], backgrount_task)
