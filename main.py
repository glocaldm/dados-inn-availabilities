import functions_framework
import requests
import json

@functions_framework.http
def fetch_and_store_data(request):
     # Allow cross-origin requests
    allowed_origins = ["https:/glocaldm.github.io"]
    origin = request.headers.get("Origin")
    print(origin)

    headers = {"Access-Control-Allow-Origin": "*"}

    # Set CORS headers for the preflight request
    if request.method == "OPTIONS":
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
        }

        return ("", 204, headers)


    # URL of the external resource
    external_url = "https://ical.booking.com/v1/export?t=219b9892-bf77-4998-b804-30590502eaf6"

    try:
        # Fetch data from external source
        # response = requests.get(external_url)
        # response.raise_for_status()
        # data = response.text

        # Set CORS headers for the main request
        # Return the fetched data
        return {
            "statusCode": 200,
            "body": "hello world",
            "headers": headers
        }

    except requests.RequestException as e:
        return {
            "statusCode": 502,
            "body": json.dumps({"error": str(e)}),
            "headers": headers
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": headers
        }
