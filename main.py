import functions_framework
import requests
import json

@functions_framework.http
def fetch_and_store_data(request):

    # URL of the external resource
    external_url = "https://ical.booking.com/v1/export?t=219b9892-bf77-4998-b804-30590502eaf6"

    try:
        # Fetch data from external source
        response = requests.get(external_url)
        response.raise_for_status()
        data = response.text
        print(data)

        # Return the fetched data
        return {
            "statusCode": 200,
            "body": data,
            "headers": {
                "Content-Type": "text/html"
            }
        }

    except requests.RequestException as e:
        return {
            "statusCode": 502,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json"
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json"
            }
        }

if __name__ == '__main__':
    fetch_and_store_data(None)