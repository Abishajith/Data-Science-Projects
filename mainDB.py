
 # main.py

from sensor.configuration.mongo_db_connection import get_db
###To connect the data this sheet (vs code)

def fetch_data():
    """
    Fetches and prints data from the 'train' collection in the 'sensor' database.
    """
    # Get the 'train' collection from the 'sensor' database
    collection = get_db()

    # Example: Fetch all documents from the 'train' collection
    documents = collection.find()

    # Print each document from the 'train' collection
    for doc in documents:
        print(doc)

   

if __name__ == "__main__":
    # Fetch data from MongoDB when the script is executed
    fetch_data()