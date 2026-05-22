import requests


def get_country_data(country):

    try:
        url = f"https://restcountries.com/v3.1/name/{country}"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()[0]

        currencies = data.get("currencies", {})

        currency_code = (
            list(currencies.keys())[0]
            if currencies
            else "N/A"
        )

        return {
            "name": data["name"]["common"],
            "capital": data.get("capital", ["N/A"])[0],
            "population": data["population"],
            "region": data["region"],
            "currency": currency_code,
            "flag": data["flags"]["png"]
        }

    except Exception:
        return None