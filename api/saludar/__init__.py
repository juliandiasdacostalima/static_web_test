import logging
import azure.functions as func
import requests
import json
import stripe

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Función "saludar" llamada.')

    # Llamado ficticio para demostrar uso de requests
    r = requests.get("https://api.chucknorris.io/jokes/random")
    data = r.json()

    return func.HttpResponse(
        json.dumps({"mensaje": f"Hola Julian! Chiste: {data['value']}"}),
        mimetype="application/json",
        status_code=200
    )
