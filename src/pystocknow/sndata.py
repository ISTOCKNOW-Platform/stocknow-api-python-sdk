
import requests
import json

# Custom Exception
class InvalidApiKeyError(Exception):
    """Custom exception for age-related validation"""
    pass

# StockNow APi Client
class SNClient:
    def __init__(self, apikey):
        """
        Initialize API client with API key
        """

        if apikey is None:
            raise InvalidApiKeyError("apikey cannot be null.")
        if not isinstance(apikey, str):
            raise InvalidApiKeyError("apikey must be string.")
        if apikey.strip() == "":
            raise InvalidApiKeyError("apikey cannot be empty.")

        self.apikey = apikey
        self.base_url = "https://api.stocknow.xyz"
        self.api_news = "/v1/AMZN/news"
        self.headers = {
            'API-Key': self.apikey,
            'Content-Type': 'application/json'
        }

    def get_news(self):
        """
        Make GET request to the API
        
        Args:
            endpoint (str): API endpoint path
        
        Returns:
            dict: Parsed JSON response
        
        Raises:
            requests.exceptions.RequestException: For network-related errors
            ValueError: For invalid JSON responses
        """
        try:
            # Construct full URL
            full_url = f"{self.base_url}/{self.api_news}"
            
            # Make GET request
            response = requests.get(full_url, headers=self.headers)
            
            # Raise an exception for bad HTTP responses
            response.raise_for_status()
            
            # Parse JSON response
            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP Error occurred: {http_err}")
            print(f"Response content: {response.text}")
            raise
        
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Error Connecting: {conn_err}")
            raise
        
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout Error: {timeout_err}")
            raise
        
        except requests.exceptions.RequestException as req_err:
            print(f"Something went wrong with the request: {req_err}")
            raise
        
        except json.JSONDecodeError as json_err:
            print(f"JSON Decoding Error: {json_err}")
            print(f"Response content: {response.text}")
            raise ValueError("Invalid JSON response")
