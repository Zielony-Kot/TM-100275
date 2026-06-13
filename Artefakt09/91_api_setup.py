import requests  # Jedyna dodatkowa biblioteka: pip -m install requests


def test_api_connectivity():
  print(">>> ZADANIE 9.1: TEST POŁĄCZENIA Z API BACKENDOWYM <<<")

  # Adres testowego API (symuluje backend aplikacji mobilnej)
  base_url = "https://jsonplaceholder.typicode.com/todos/1"

  try:
    # Wykonanie żądania GET
    response = requests.get(base_url, timeout=5)

    # Analiza inżynierska odpowiedzi
    status_code = response.status_code
    data = response.json()

    print(f"[DEBUG] Status Code: {status_code}")
    print(f"[DEBUG] Response Body: {data}")

    # Asercja (Serce testu)
    if status_code == 200:
      print(f"[SUCCESS] API jest dostępne. Tytuł zadania: {data['title']}")
    else:
      print(f"[ERROR] Serwer zwrócił błąd: {status_code}")

  except Exception as e:
    print(f"[FATAL] Brak łączności z API: {e}")


if __name__ == "__main__":
  test_api_connectivity()

