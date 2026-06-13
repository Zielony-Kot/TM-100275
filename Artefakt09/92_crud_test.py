import requests
import json


def test_create_resource():
    print(">>> ZADANIE 9.2: TEST TWORZENIA ZASOBU (POST) <<<")

    url = "https://jsonplaceholder.typicode.com/posts"

    # Dane, które "aplikacja mobilna" wysyła do serwera
    new_post = {
        "title": "Test Mobilny Blok 9",
        "body": "Automatyzacja API jest szybsza niż UI",
        "userId": 1
    }

    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    print(f"[INFO] Wysyłanie żądania POST do: {url}")

    response = requests.post(url, data=json.dumps(new_post), headers=headers)

    # Weryfikacja inżynierska
    status = response.status_code
    result_data = response.json()

    print(f"[DEBUG] Status Code: {status}")  # Oczekiwane 201
    print(f"[DEBUG] Server Response: {result_data}")

    if status == 201:
        print(f"[SUCCESS] Zasób stworzony pomyślnie! ID nowego obiektu: {result_data['id']}")
    else:
        print(f"[FAIL] Serwer nie stworzył zasobu. Status: {status}")


if __name__ == "__main__":
    test_create_resource()

