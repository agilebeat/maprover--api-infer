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

def check_if_point_within_polygon(point, polygon):
    point_x = point["geometry"]["coordinates"][0]
    point_y = point["geometry"]["coordinates"][1]

    polygon_max_x, polygon_max_y = max(polygon["geometry"]["coordinates"][0])
    polygon_min_x, polygon_min_y = min(polygon["geometry"]["coordinates"][0])

    if polygon_min_x < point_x < polygon_max_x and polygon_min_y < point_y < polygon_max_y:
        return True
    return False


def get_tweets_selection(selection):
    tweets = tweetsdata.tweet_data_set
    selected_tweets = { "type" : "FeatureCollection", "features": []}
    features = selected_tweets["features"]

    try:
        for sf in selection["features"]:
            for tf in tweets["features"]:
                if check_if_point_within_polygon(tf, sf):
                    features.append(tf)
    except:
        pass
    return selected_tweets



def create_response(event):
    selection = json.loads(event['body'])
    selected_tweets = get_tweets_selection(selection)
    response = {
        "statusCode": 200,
        "headers": {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        "body": json.dumps(selected_tweets)
    }
    return response


def filterTweetHandler(event, context):
    response = create_response(event)
    return response
