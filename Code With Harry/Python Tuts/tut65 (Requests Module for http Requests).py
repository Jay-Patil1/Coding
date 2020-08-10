# REQUESTS MODULE FOR HTTP REQUESTS
import requests
r = requests.get("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=demo")
print(r.text)  # The content of the source ot he page ().
print(r.status_code)

# url = "www.something.com"
# data = {
#     "pi" : 4,
#     "p2" : 8
# }
#
# r2 = requests.post(url=url, data=data)
# The browser doesnt save this.
# This goes to the () and enters the data.
            # Goolge for more functions of requests.
