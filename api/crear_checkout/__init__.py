import os
import json
import stripe
import azure.functions as func

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

PRODUCTS = {
    "burger": {"name": "Hamburguesa", "price": 500},
    "fries": {"name": "Papas", "price": 200},
    "drink": {"name": "Bebida", "price": 150}
}

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        items = body.get("items", [])

        line_items = []
        for item in items:
            prod = PRODUCTS[item["id"]]
            line_items.append({
                "price_data": {
                    "currency": "eur",
                    "product_data": {"name": prod["name"]},
                    "unit_amount": prod["price"]
                },
                "quantity": 1
            })

        YOUR_DOMAIN = "https://lively-wave-0e7faf71e.6.azurestaticapps.net"

        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )

        return func.HttpResponse(
            json.dumps({"url": checkout_session.url}),
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )