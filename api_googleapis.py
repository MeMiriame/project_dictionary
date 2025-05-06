import requests

def search_google_books(query):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={query}")
    data = response.json()
    items = data["items"]
    total_items = len(items)
    print(f"Nalezeno knih: {total_items}")
    for page in range(total_items):
        if "items" in data:
            book = data["items"][page]["volumeInfo"]
            print("Název:", book.get("title"))
            print("Autor:", book.get("authors", ["Neznámý"])[0])
            print("Datum vydání:", book.get("publishedDate"))
            print("ISBN:", book.get("industryIdentifiers", [0]))
        else:
            print("Kniha nenalezena.")

search_google_books("1984")  # ISBN jako hledání



