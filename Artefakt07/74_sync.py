import sys
import os
import time

# Połączenie z bazą POM
sys.path.append(os.path.abspath("../Artefakt06"))
from MainPage import MainPage

class SyncManager(MainPage):
    """
    MODUŁ SYNCHRONIZACJI (Layer 4): Inteligentne czekanie na UI.
    """
    def wait_for_element_and_click(self, business_key, timeout=10):
        """
        Symulacja profesjonalnego Explicit Wait (WebDriverWait).
        """
        selector = self.find_id(business_key)
        if not selector:
            return f"BŁĄD: Brak klucza '{business_key}' w mapie!"
        print(f"[SYNC] Rozpoczynam oczekiwanie na: {selector} (max {timeout}s)")
        # Symulacja pętli sprawdzającej obecność elementu (Polling)
        start_time = time.time()
        found = False
        # W rzeczywistym Appium:
        # element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(...))
        time.sleep(1.5) # Symulacja opóźnienia ładowania aplikacji
        found = True
        end_time = time.time()
        duration = round(end_time - start_time, 2)

        if found:
            return f"SUKCES: Element '{selector}' odnaleziony i kliknięty po {duration}s."
        return f"TIMEOUT: Element '{selector}' nie pojawił się w ciągu {timeout}s!"

if __name__ == "__main__":
    sm = SyncManager()
    print(">>> ZADANIE 7.4: TESTY SYNCHRONIZACJI DYNAMICZNEJ <<<")
    print("-" * 50)

    # Testujemy poprawne czekanie
    print(sm.wait_for_element_and_click("ADD"))

    # Testujemy timeout (dla nieistniejącego klucza)
    print(sm.wait_for_element_and_click("NON_EXISTENT_BUTTON"))

    print("-" * 50)