from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.product import Product
from service.productService import deleteProductRecord, getAll, getProductDetails, saveProduct


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
    )


@app.get('/products')
def all():
    return getAll()

@app.post("/products")
def create(product: Product):
    return saveProduct(product)

@app.get("/products/{pk}")
def getProducts(pk:str):
    return getProductDetails(pk)

@app.delete("/products/{pk}")
def deleteProduct(pk: str):
    return deleteProductRecord(pk)
