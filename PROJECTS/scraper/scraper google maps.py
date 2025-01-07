from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import csv
import time

# Funkcja do zapisywania danych do pliku CSV
def save_to_csv(data, filename="business_data.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Categories", "Full Address", "Phone", "Website", "Google Maps URL"])
        writer.writerows(data)

# Funkcja do pobierania szczegółowych danych biznesów
def scrape_businesses(search_query, location):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Przejdź do Google Maps
        driver.get("https://www.google.com/maps")
        time.sleep(3)

        # Obsłuż okno z plikami cookie
        try:
            reject_cookies_button = driver.find_element(By.NAME, "Zaakceptuj wszystko")
            
            reject_cookies_button.click()
            time.sleep(2)
        except Exception as e:
            print("Nie znaleziono okna z plikami cookie lub przycisku:", e)

        # Poczekaj na załadowanie pola wyszukiwania
        search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "searchboxinput"))
        )
        search_box.send_keys(f"{search_query} {location}")
        search_box.send_keys(Keys.RETURN)

        time.sleep(5)

        # Pobieranie wyników
        business_data = []
        results = driver.find_elements(By.CLASS_NAME, "Nv2PK")
        for result in results:
            try:
                name = result.find_element(By.CLASS_NAME, "qBF1Pd").text
            except:
                name = "N/A"

            try:
                categories = result.find_element(By.CLASS_NAME, "ZzC4X").text
            except:
                categories = "N/A"

            try:
                full_address = result.find_element(By.CLASS_NAME, "W4Efsd").text
            except:
                full_address = "N/A"

            try:
                result.click()
                time.sleep(3)
                phone = driver.find_element(By.XPATH, "//button[@data-tooltip='Skopiuj numer telefonu']/following-sibling::span").text
            except:
                phone = "N/A"

            try:
                website = driver.find_element(By.XPATH, "//button[@data-tooltip='Przejdź do strony internetowej']/following-sibling::a").get_attribute("href")
            except:
                website = "N/A"

            try:
                gmaps_url = driver.current_url
            except:
                gmaps_url = "N/A"

            business_data.append([name, categories, full_address, phone, website, gmaps_url])

            driver.back()
            time.sleep(2)

        return business_data

    finally:
        driver.quit()

# Główna część programu
if __name__ == "__main__":
    search_query = input("Co chcesz wyszukać? (np. kawiarnie, restauracje): ")
    location = input("W jakiej lokalizacji? (np. Warszawa, Kraków): ")

    print("Rozpoczynam zbieranie danych...")
    data = scrape_businesses(search_query, location)

    print(f"Zapisuję dane do pliku CSV...")
    save_to_csv(data)
    print(f"Dane zostały zapisane w pliku 'business_data.csv'.")
