import requests

def search(query, api_key):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&q={query}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'items' in data:
                search_result = data['items'][0]['snippet']
                return search_result
            else:
                return "No results found."
        else:
            return "Failed to fetch search results."
    except Exception as e:
        return str(e)

def main():
    api_key = "AIzaSyAvmM4no4AP-ClN-QSwbEORvG7oqxaFpn4"

    print("Welcome to the Simple Chat Assistant!")
    print("You can ask me anything. Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        response = search(user_input, api_key)
        print("Assistant:", response)

if __name__ == "__main__":
    main()
