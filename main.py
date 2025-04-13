from flask import Flask, request, make_response
import functions_framework

ALLOWED_ORIGIN = "https://obscure-fiesta-4j669jrqpvg7376qg-4200.app.github.dev"
external_url = "https://ical.booking.com/v1/export?t=219b9892-bf77-4998-b804-30590502eaf6"

@functions_framework.http
def fetch_and_store_data(request):
    origin = request.headers.get('Origin', '')
    cors_headers = {
        'Access-Control-Allow-Origin': ALLOWED_ORIGIN if origin == ALLOWED_ORIGIN else '',
        'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'Vary': 'Origin'
    }

    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return ('', 204, cors_headers)

    # Handle GET or POST request
    if request.method in ['POST', 'GET']:
        text_data = request.get_data(as_text=True) or "No data provided."
        response = make_response(f"Received text:\n{text_data}")
        response.headers.update(cors_headers)
        response.headers['Content-Type'] = 'text/plain'
        return response

    return make_response(("Method Not Allowed", 405, cors_headers))
