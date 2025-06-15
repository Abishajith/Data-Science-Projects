import sys
from typing import Optional
import numpy as np
import pandas as pd
import json
from sensor.configuration.mongo_db_connection import get_db
from sensor.exception import SensorException

class SensorData:
    """
    This class helps to export entire MongoDB records as a pandas DataFrame.
    """

    def __init__(self, database_name: str = "sensor"):
        """
        Initializes the connection to the MongoDB database.
        """
        try:
            # Initialize the MongoDB client and get the database
            self.db = get_db(database_name)  # Get the database, not a specific collection
        except Exception as e:
            raise SensorException(e, sys)

    def save_csv_file(self, file_path: str, collection_name: str, database_name: Optional[str] = None):
        """
        Saves data from a CSV file to MongoDB collection.
        """
        try:
            # Read CSV and convert it to a DataFrame
            data_frame = pd.read_csv(file_path)
            data_frame.reset_index(drop=True, inplace=True)

            # Convert DataFrame to list of dictionaries
            records = list(json.loads(data_frame.T.to_json()).values())

            # Get the appropriate collection
            if database_name is None:
                collection = self.db[collection_name]
            else:
                collection = get_db(database_name)[collection_name]

            # Insert records into the collection
            collection.insert_many(records)

            return len(records)

        except Exception as e:
            raise SensorException(e, sys)

    def export_collection_as_dataframe(
        self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Exports the entire collection from MongoDB as a pandas DataFrame.
        """
        try:
            # Get the appropriate collection
            if database_name is None:
                collection = self.db[collection_name]
            else:
                collection = get_db(database_name)[collection_name]

            # Query all documents in the collection and convert them into a pandas DataFrame
            df = pd.DataFrame(list(collection.find()))

            # Drop the _id column (MongoDB's default document identifier)
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            # Replace 'na' values with np.nan (useful for handling missing data)
            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise SensorException(e, sys)