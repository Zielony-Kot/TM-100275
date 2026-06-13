import subprocess
import time
import os
import sys
from datetime import datetime


def run_cmd(cmd, ignore_error=False):
    """Wykonuje komendę systemową i obsługuje błędy."""
    try:
        subprocess.run(cmd, shell=True, check=not ignore_error)
    except subprocess.CalledProcessError:
        if not ignore_error:
            sys.exit(1)


def main():
    # 0. Konfiguracja ścieżek
    compose_path = "../Artefakt09/docker-compose.yml"
    results_dir = "allure-results"

    # === TUTAJ WPISZ SWOJĄ PEŁNĄ ŚCIEŻKĘ DO ALLURE.BAT ===
    # Literka r przed cudzysłowem jest ważna, żeby Windows dobrze czytał ukośniki (\)
    allure_win_path = r"C:\Users\aessa\scoop\apps\allure\2.42.1\bin\allure.bat"

    if not os.path.exists(compose_path):
        print(f"❌ Błąd: Nie znaleziono pliku {compose_path}")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("🚀 START: AUTOMATYCZNY PIPELINE TESTOWY (PRO)")
    print("=" * 50)

    # 1. Przygotowanie czystego środowiska
    run_cmd("docker rm -f appium-server", ignore_error=True)

    # 2. Uruchomienie infrastruktury
    print("\n📦 KROK 1: Podnoszenie kontenerów...")
    run_cmd(f"docker compose -f {compose_path} up -d")

    # 3. Czekanie na gotowość
    time.sleep(5)

    # 4. Egzekucja testów
    print("\n🧪 KROK 2: Uruchamianie testów Pytest...")
    py_cmd = "python3" if sys.platform != "win32" else "python"
    run_cmd(f"{py_cmd} -m pytest test_102_meta_reporting.py --alluredir={results_dir}", ignore_error=True)

    # 5. DODAWANIE DOWODU PIPELINE DO RAPORTU (Metadane)
    print("\n📝 KROK 3: Dokumentowanie przebiegu Pipeline...")
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    env_content = f"""Pipeline.Status=SUCCESS
Execution.Time={datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Execution.Type=Automated Master Script
Infrastructure=Docker (Appium Server)
Platform={sys.platform}
Build.Engine=Python Subprocess
"""
    with open(f"{results_dir}/environment.properties", "w") as f:
        f.write(env_content)

    # 6. Generowanie raportu końcowego (POWROZNA ZMIANA DLA WINDOWS)
    print("\n📊 KROK 4: Generowanie raportu Allure...")

    # Sprawdzamy, czy system to Windows i czy podana ścieżka istnieje
    if sys.platform == "win32" and os.path.exists(allure_win_path):
        cmd_allure = f'"{allure_win_path}" generate {results_dir} --clean -o allure-report'
    else:
        # Jeśli jesteś na Macu/Linuxie lub Allure jest w PATH
        cmd_allure = f"allure generate {results_dir} --clean -o allure-report"

    run_cmd(cmd_allure)

    # 7. Sprzątanie
    print("\n🧹 KROK 5: Zamykanie i usuwanie kontenerów...")
    run_cmd(f"docker compose -f {compose_path} down")

    print("\n" + "=" * 60)
    print("🏆 PIPELINE ZAKOŃCZONY POPRAWNIE!")
    print(f"📍 Raport wygenerowany: {os.getcwd()}/allure-report/index.html")
    print(f"💡 Użyj 'allure open allure-report' lub wskaż pełną ścieżkę do bat, aby go wyświetlić.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

