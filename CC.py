import requests

def get_credit_card_numbers(api_url, api_key):
    try:
        # Set up the headers with the API key
        headers = {'Authorization': f'Bearer {api_key}'}

        # Make a GET request to the API endpoint with the headers
        response = requests.get(api_url + '/creditcards/numbers', headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response content (assuming it returns JSON)
            print("Response:")
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    api_url = 'http://10.0.61.32'

    api_key = os.environ.get('API_KEY')

    get_credit_card_numbers(api_url, api_key)