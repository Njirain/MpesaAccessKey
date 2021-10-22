# import request module for sending requests
import requests
# For authentication
from requests.auth import HTTPBasicAuth
# for converting data into a json object
import json


def funauthenticate():
    # pass in the key generated from your app
    key = 'your_key'
    # your secret key too
    secret = 'your_key'
    # an example API for authentication
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    # request(GET)
    mpesa_response = requests.get(api_url, auth=HTTPBasicAuth(key, secret))
    # retrieved string response
    str_response = mpesa_response.text
    # to dictionary using json module
    dictionary = json.loads(str_response)
    return dictionary['access_token']


if __name__ == '__main__':
    print('Token: {0}'.format(funauthenticate()))
