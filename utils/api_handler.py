import requests

def fetch_all_products():
    # Code from Task 3.1a
    try:
        response = requests.get('https://dummyjson.com/products?limit=100')
        return response.json().get('products', []) if response.status_code == 200 else []
    except: return []

def create_product_mapping(api_products):
    # Code from Task 3.1b
    return {p['id']: {'title': p['title'], 'category': p['category'], 'brand': p['brand'], 'rating': p['rating']} for p in api_products}
