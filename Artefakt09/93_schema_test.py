import requests
from jsonschema import validate
import json


def test_api_schema():
    print(">>> ZADANIE 9.3: WALIDACJA STRUKTURY JSON (KONTRAKT) <<<")

    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    data = response.json()

    # DEFINICJA SCHEMATU (Nasz "odlew" danych)
    # Określamy, że userId i id MUSZĄ być liczbami, a title i body tekstami
    expected_schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title"]  # Te pola są obowiązkowe
    }

    try:
        # Próba dopasowania danych z API do naszego schematu
        validate(instance=data, schema=expected_schema)
        print("[SUCCESS] Kontrakt zachowany. Struktura JSON jest poprawna.")
        print(f"[DEBUG] Zweryfikowano pola dla obiektu ID: {data['id']}")

    except Exception as e:
        print(f"[FAIL] BŁĄD KONTRAKTU! Serwer przysłał błędny format danych.")
        print(f"[REASON] {e.message}")


if __name__ == "__main__":
    test_api_schema()
