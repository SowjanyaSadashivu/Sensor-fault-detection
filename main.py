from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant import training_pipeline
from sensor.exception import SensorException
import os, sys
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline

if __name__ == '__main__':
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
    

# def test_exception():
#     try:
#         logging.info("we are dividing 0 by 1")
#         x = 1/0
#     except Exception as e:
#         raise SensorException(e, sys)

# if __name__ == '__main__':

#     try:
#         test_exception()
#     except Exception as e:
#         print(e)

    # mongodb_client = MongoDBClient()
    # print(mongodb_client.database.list_collection_names())