import sys
import requests


def main():
    if len(sys.argv) == 2:
        try:
            x = float(sys.argv[1])
            print(bit_coin_price(x))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


def bit_coin_price(num):
    try:
        link = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
        result = link.json()
        price = result["bpi"]["USD"]["rate_float"]
        total = price * num
        return f"${total:,.4f}"
    except request.RequestException:
        return None


main()
