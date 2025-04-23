import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        items = data.get("items", [])

        total = sum(item["price"] for item in items)

        return func.HttpResponse(
            json.dumps({"total": total}),
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
