from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://mongo-db:27017")
db = client.mydatabase

@app.get("/data")
def get_data():
    collection = db["test_collection"]
    return list(collection.find())
