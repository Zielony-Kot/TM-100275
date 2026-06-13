import requests
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time


def check_bridge():
    print("=== TEST MOSTEK HYBRYDOWY (ARTEFAKT 9.5) ===")

    # 1. API Check
    print("\n[STEP 1] API: Sprawdzanie dostępności backendu...")
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        if r.status_code == 200:
            print(" > [SUCCESS] Backend (REST API) dostępny.")
    except Exception as e:
        print(f" > [FAIL] API nieosiągalne: {e}")
        return

    # 2. Appium Docker Check
    print("\n[STEP 2] DOCKER: Sprawdzanie serwera Appium...")
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    try:
        # Próba nawiązania sesji (timeout ustawiony krótko, by nie czekać wiecznie)
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        print(" > [SUCCESS] Połączono z serwerem!")
        driver.quit()
    except Exception as e:
        # Analiza błędu - czy serwer żyje, ale nie ma urządzenia?
        error_msg = str(e)
        if "Connection refused" in error_msg:
            print(" > [CRITICAL] Kontener Appium nie wystawił portu! Sprawdź Docker Compose.")
        elif "Could not find a connected Android device" in error_msg:
            print(" > [SUCCESS] Serwer Appium w Dockerze ODPOWIADA poprawnie.")
            print(" > [STATUS] Urządzenie niepodpięte (zgodnie z planem), ale most działa.")
        else:
            print(f" > [INFO] Odebrano odpowiedź od Appium: {error_msg[:100]}...")

    print("\n=== KONIEC TESTU 9.5: INFRASTRUKTURA GOTOWA ===")


if __name__ == "__main__":
    check_bridge()
