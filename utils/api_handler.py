import requests

def fetch_all_products():
    """Fetches products from API with descriptive error handling."""
    url = 'https://dummyjson.com/products?limit=100'
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json().get('products', [])
        else:
            # More descriptive error based on status code
            print(f"API Error: Server returned status {response.status_code}. Please check the URL.")
            return []
    except requests.exceptions.ConnectionError:
        print("API Connection failed: Please check your internet connection.")
        return []
    except requests.exceptions.Timeout:
        print("API Error: The request timed out. The server might be busy.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def create_product_mapping(api_products):
    """Creates a mapping of product IDs to info."""
    return {p['id']: {'title': p['title'], 'category': p['category'], 'brand': p['brand'], 'rating': p['rating']} for p in api_products}
