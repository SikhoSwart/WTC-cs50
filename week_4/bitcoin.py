import requests
import sys

try:
    #get the user input from the command-line
    n = float(sys.argv[1])
    #get the api, with api key
    r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=dafffed307fbc62512e44a154834aa76b00f499544ad26f22995ec9f5e2e6559')

except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
except requests.RequestException:
    pass
else:
    content = r.json()
    #get the current bitcoin price
    usd = float(content['data']['priceUsd'])

print(f"${n*usd:,.4f}")
