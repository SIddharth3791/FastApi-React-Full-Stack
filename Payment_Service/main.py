
from fastapi import BackgroundTasks, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from service.order_service import create_Order, getOrderByPkId
  
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
    )

@app.get("/order/{pk}")
def getOrderByPk(pk: str):
    return getOrderByPkId(pk)


@app.get("/order")
async def createOrder(request: Request, backgrount_task: BackgroundTasks):
    body = await request.json()
    return await create_Order(body["id"], body["quantity"], backgrount_task)
