import requests

def lambda_handler(event, context):
    # Define the API URL
    api_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=400&page=1&sparkline=true&locale=en"  
    
    try:
        # Make a GET request to the API
        response = requests.get(api_url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()  # Assuming the API returns JSON data
            return {
                'statusCode': 200,
                'body': data
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': "API request failed"
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
