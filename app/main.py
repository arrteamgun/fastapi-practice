from fastapi import FastAPI
from .models.models import Product
from .models.sample import sample_products

app = FastAPI()

lst = []


@app.get("/product/search")
def search(keyword: str, category: str = None, limit: int = 10):

    result = list(filter(lambda item: keyword.lower()
                  in item['name'].lower(), sample_products))
    print(result)
    if category:
        result = list(
            filter(lambda item: item["category"] == category, result))

    return result[:limit]


@app.get("/product/{product_id}")
async def get_product_by_id(product_id: int) -> Product:
    return [i for i in sample_products if i["product_id"] == product_id][0]
