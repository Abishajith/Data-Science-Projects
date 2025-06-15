# config/mongo.py

from pymongo import MongoClient

def get_db(database_name="sensor"):
    """
    Establishes a connection to MongoDB and returns the specified database.
    Default is 'sensor'.
    """
    # MongoDB connection string for local MongoDB
    client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB server at localhost:27017

    # Access the specified database, default is 'sensor'
    db = client[database_name]

    return db