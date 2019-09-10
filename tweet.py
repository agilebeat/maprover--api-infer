try:
  import unzip_requirements
  import json
  import boto3
  from botocore.errorfactory import ClientError
  import base64
  import string
  import random
  from io import BytesIO
  import tweetsdata
except ImportError:
  pass



def create_response():
    response = {
        "statusCode": 200,
        "headers": {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        "body": json.dumps(tweetsdata.tweet_data_set)
    }
    return response


def create_debug_response(event):
  response = {
    "statusCode": 200,
    "headers": {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
    "body": json.dumps(event['body'])
  }
  return response

def tweetHandler(event, context):

    response = create_response()
    return response












