import requests


def convert_currency(from_currency, to_currency, amount):

    try:
        url = (
            f"https://open.er-api.com/v6/latest/{from_currency}"
        )

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        rates = data.get("rates", {})

        if to_currency not in rates:
            return None

        converted_amount = amount * rates[to_currency]

        return converted_amount

    except Exception:
        return None