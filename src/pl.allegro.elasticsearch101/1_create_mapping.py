import requests

mapping = {
    "mappings": {
        "properties": {
            "title": {"type": "text"},
            "description": {"type": "text"},
            "price": {"type": "integer"},
            "fabric": {"type": "text"},
            "color": {"type": "text"},
            "note": {"type": "keyword", "index": False}
        }
    }
}

url = 'http://localhost:9200/products'

requests.put(url, json=mapping)
