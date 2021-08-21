import requests

products = [
    {"title": "sweater with long sleeves",
     "description": "Lorem ipsum",
     "price": 100,
     "fabric": "lamb wool",
     "color": "white"
     },
	{"title": "sweater with amazing sleeves",
     "description": "Lorem ipsum",
     "price": 100,
     "fabric": "lamb wool",
     "color": "white"
     },
    {"title": "shirt with short sleeves",
     "description": "Lorem ipsum",
     "price": 40,
     "fabric": "cotton",
     "color": "red"
     },
    {"title": "one piece swimsuit",
     "description": "Lorem ipsum",
     "price": 120,
     "fabric": "baby alpaca",
     "color": "green"
     },
    {"title": "two piece swimsuit",
     "description": "Lorem ipsum",
     "price": 140,
     "fabric": "baby alpaca",
     "color": "red"
     },
    {"title": "winter coat with hood",
     "description": "winter coat knitted during long winter nights",
     "price": 120,
     "fabric": "lamb wool shining in blue",
     "color": "yellow"
     }
]

for product in products:
    response = requests.post("http://localhost:9200/products/_doc", json=product)
    print(response.status_code)

