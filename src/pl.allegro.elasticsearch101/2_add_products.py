import requests

products = [
    {"title": "Sweter z długim rękawem",
     "description": "Lorem ipsum",
     "price": 100,
     "fabric": "wełna owcza",
     "color": "biały"
     },
    {"title": "koszulka z krótkim rękawem",
     "description": "Lorem ipsum",
     "price": 40,
     "fabric": "bawełna",
     "color": "czerwony"
     },
    {"title": "strój kąpielowy jednoczęściowy",
     "description": "Lorem ipsum",
     "price": 120,
     "fabric": "baby alpaka",
     "color": "zielony"
     },
    {"title": "strój kąpielowy dwuczęściowy",
     "description": "Lorem ipsum",
     "price": 140,
     "fabric": "baby alpaka",
     "color": "czerwony"
     },
    {"title": "kurtka zimowa z kapturem",
     "description": "kurtka zimowa zrobiona na drutach podczas długich zimowych wieczorów",
     "price": 120,
     "fabric": "wełna owcza połyskująca na niebiesko",
     "color": "żółty"
     },
]

for product in products:
    response = requests.post("http://localhost:9200/products/_doc", json=product)
    print(response.status_code)

