# Save data to an AWS bucket

from typing import Dict

#import aws_lib
import pymongo

aws_access_key_id = 'AKIAZ7TBUSG3OHWZIQPF'
aws_secret_access_key = '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'


def aws_upload(data: Dict):
    database = aws_lib.connect(aws_access_key_id, aws_secret_access_key)
    database.push(data)


def transform_data(es_data: Dict) -> Dict:
    es_data = {**data, "origin": "ES"}

MONGO_URI = "mongodb+srv://testuser:hub24aoeu@gg-is-awesome-gg273.mongodb.net/test?retryWrites=true&w=majority"

def pull_data_from_mongo(query: Dict):
    return pymongo.connect(MONGO_URI).fetch(query)


def push_mongo_to_s3(query):
    for element in pull_data_from_mongo(query):
        upload(element)
