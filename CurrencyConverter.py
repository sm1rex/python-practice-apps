import requests

api_key = "1442d7591c664a068281f391272668e6"


def get_exancherate():
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    data = response.json()
    return data["rates"]


def convert_currency(amount, from_currency, to_currency):
    rates = get_exancherate()
    conversion_rate = rates[to_currency] / rates[from_currency]
    converted_amount = amount * conversion_rate
    return converted_amount


if __name__ == "__main__":
    amount = 200
    from_c = "UAH"
    to_c = "USD"
    converted_amount = convert_currency(amount, from_c, to_c)
    print(f"{amount} {from_c} = {converted_amount:.2f} {to_c}")
