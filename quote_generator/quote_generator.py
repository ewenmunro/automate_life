import requests


def fetch_multiple_quotes(count=5):
    quotes = []
    for _ in range(count):
        try:
            response = requests.get("https://api.quotable.io/random")
            response.raise_for_status()  # Check for HTTP errors
            quote_data = response.json()
            quotes.append((quote_data['content'], quote_data['author']))
        except requests.exceptions.RequestException as e:
            quotes.append(("Error fetching quote", str(e)))
    return quotes


if __name__ == "__main__":
    number_of_quotes = 5
    quotes = fetch_multiple_quotes(number_of_quotes)
    for quote, author in quotes:
        print(f"\"{quote}\" - {author}")
