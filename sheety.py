import requests

BEARER = "sugApp"
USERNAME = "99129d772f20552f38a3ef08f9a3f35d"

PROJECT = "sugApp"
SHEET = "feuilles"

base_url = "https://api.sheety.co"

def post_new_row(name, email, suggestion):
    endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
    url = base_url + endpoint_url

    headers = {
        "Authorization": f"Bearer {BEARER}"
    }

    body = {
        "feuille": {
            "name": name,
            "email": email,
            "suggestion": suggestion
        }
    }

    response = requests.post(url=url, headers=headers, json=body)
    response.raise_for_status()
    # print(response.text)
def get_customer_emails():
    customers_endpoint = "https://api.sheety.co/99129d772f20552f38a3ef08f9a3f35d/traker/users"
    headers = {
        "Authorization": f"Bearer {BEARER}"
    }
    response = requests.get(url=customers_endpoint, headers=headers)
    data = response.json()
    # print(data)
    customer_data = data["users"]
    return customer_data