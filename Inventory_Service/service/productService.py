from model.product import Product

def getAll():
     return [format(pk) for pk in Product.all_pks() ]

def saveProduct(product: Product):
    recordSaved = product.save()
    return recordSaved

def getProductDetails(pk: str):
    try:
        return Product.get(pk)
    except: 
        return f"ERROR When fetching Product Details for PK : {pk}"

def deleteProductRecord(pk: str):
    try:
        recordDeleted =  Product.delete(pk)
        if recordDeleted == 1:
            return "Record Deleted"
        else:
            raise Exception
    except Exception as err: 
        return f"ERROR When Deleting Product Details for PK : {pk}"

def format(pk: str):
    product = Product.get(pk)
    return {
        "id": product.pk,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity
    }
    