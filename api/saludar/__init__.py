import requests

def main(req):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": {"mensaje": "Hola desde Python con requests!"}
    }
