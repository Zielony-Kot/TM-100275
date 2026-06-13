# 📱 Mobile Automation & Cloud-Ready Testing Suite

**Prowadzący:** mgr Mariusz Dworniczak
**Student:** Magdalena Kitzol
**Numer Albumu:** 100275

---

## 🏗️ Architektura Projektu (Marketing & Tech Stack)
Ten projekt to kompletny ekosystem testowy oparty na podejsciu **Cloud-Ready / Headless**. Zamiast polegać na ciężkich emulatorach, skupiamy się na narzędziach CLI, analizie statycznej, konteneryzacji (Docker) oraz automatyzacji procesów (Pipeline).

**Główne technologie:**
* **Język:** Python 3.10+
* **Automatyzacja UI:** Appium 2.x (Mobile Engine)
* **Infrastruktura:** Docker & Docker Compose
* **Raportowanie:** Allure Framework
* **Analiza:** MobSF (Static Analysis) & ADB CLI

---

## 📅 PRZEBIEG LABORATORIUM (Kamienie Milowe)

### 🔹 BLOK 1: Tooling & Environment (Infrastruktura)
Przygotowanie bazy narzędziowej w modelu kontenerowym.
* **Co zrobiono:** Pobranie i konfiguracja obrazów `appium`, `android-sdk` oraz `mobsf`.
* **Wniosek:** Dlaczego używamy obrazów Docker zamiast instalować wszystko lokalnie?
* **Używamy obrazów Docker zamiast instalacji lokalnej, aby zagwarantować identyczne, odizolowane środowisko uruchomieniowe na każdym komputerze, niezależnie od konfiguracji systemów operacyjnych.

### 🔹 BLOK 2: Debugowanie i Analiza Statyczna (MobSF)
Zrozumienie "wnętrza" aplikacji mobilnej przed przystąpieniem do testów.
* **Co zrobiono:** Wykorzystanie MobSF do skanowania plików APK pod kątem podatności i uprawnień.
* **Wniosek:** Co daje testerowi analiza statyczna kodu APK?
* **Analiza statyczna kodu APK pozwala na szybkie wykrycie luk bezpieczeństwa, błędów w architekturze oraz ukrytych wad w kodzie źródłowym aplikacji bez konieczności jej uruchamiania.

### 🔹 BLOK 3-4: Fundamenty Skryptowania (Python for QA)
Budowa logiki testowej w języku Python.
* **Co zrobiono:**
* **Wykorzystano słowniki i bibliotekę json w Pythonie do automatycznej ekstrakcji metadanych XML oraz generowania raportów z testów. Napisane funkcje pozwoliły na analizę unikalności selektorów.

### 🔹 BLOK 5-7: Hybrydowe Testowanie API (Requests & Pytest)
Weryfikacja warstwy backendowej aplikacji mobilnej.
* **Co zrobiono:** Testowanie endpointów REST (JSONPlaceholder), obsługa kodów HTTP i asercja danych JSON.
* **Wniosek:** Testowanie API pozwala wyłapać błędy zanim uruchomimy ciężkie testy UI.

### 🔹 BLOK 8: Appium UI Automation (Deep Dive)
Automatyzacja interakcji z interfejsem użytkownika.
* **Co zrobiono:**
* **Statyczna Analiza Bezpieczeństwa (MobSF) - audyt uprawnień z pliku AndroidManifest.xml z wygenerowanym raportem technicznym, skaner wycieków danych(hardcoded secrets - kluczy API, tokenów) z wygenerowanym skryptem txt wykrytych danych, symulacja wykrycia podatności w pliku, obliczenie klasyfikacji ryzyka (security score). Finałowo: dokument zbiorczy audytu.

### 🔹 BLOK 9: Konteneryzacja Serwera (Docker Compose)
Izolacja silnika Appium od systemu operacyjnego.
* **Co zrobiono:** Stworzenie pliku `docker-compose.yml` zarządzającego serwerem Appium i sterownikami.

### 🔹 BLOK 10: MASTER PIPELINE (Capstone Project) 🏆
Finałowa automatyzacja całego procesu testowego.
* **Co zrobiono:** Stworzenie skryptu `pipeline.py`, który w jednym cyklu:
1. Rezerwuje zasoby i stawia infrastrukturę Docker.
2. Wykonuje testy hybrydowe (API + UI).
3. Generuje profesjonalny raport Allure z metadanymi.
4. Czyści środowisko po zakończonej pracy.

---

## 📊 Raportowanie Wyników (Allure)
Projekt wykorzystuje zaawansowane raportowanie Allure, które pozwala na:
* Śledzenie kroków testowych (`@allure.step`).
* Analizę błędów wraz z załącznikami (zrzuty ekranu, logi JSON).
* Dokumentowanie środowiska wykonawczego w sekcji **Environment**.

![Allure](Artefakt10/allure.png)

---

## 🚀 Jak uruchomić cały proces?
```bash
# Wejdź do folderu finałowego
cd Artefakt10

# Uruchom wszystko jednym poleceniem
python3 pipeline.py

# Po zakończeniu zobacz raport
allure serve allure-results

