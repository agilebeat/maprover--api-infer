try:
  import unzip_requirements
  import json
  import boto3
  from botocore.errorfactory import ClientError
  import base64
  import string
  import random
  from io import BytesIO
except ImportError:
  pass


mocked_geojson = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          174.9156190124816,
          -36.30215075678218
        ]
      },
      "properties": {
        "post": "@SahirSardarzada That's called paying respect for a dog which served &amp; saved lived. We all know 'wafadaari' is some… https://t.co/O9a87XugyW"
      }
    }, {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          175.48762192860363,
          -37.268162189409495
        ]
      },
      "properties": {
        "post": "4 weeks to lose my winter tum before Australia"
      }
    }
  ]
}

def create_response():
    response = {
        "statusCode": 200,
        "headers": {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        "body": json.dumps(mocked_geojson)
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












