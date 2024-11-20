from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_Login_Reviewing_Info():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)  

    try:
        driver.get("http://13.214.1.75/#/login")

        time.sleep(1)

        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Username"]'))
        )
        username_field.send_keys("ns.sa")

        time.sleep(1)

        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Password"]'))
        )
        password_field.send_keys("1234")
        time.sleep(1)

        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        login_button.click()

        WebDriverWait(driver, 20).until(EC.url_contains("/home"))
        time.sleep(2)

        dashboard_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Dashboard']"))
        )
        dashboard_button.click()

        WebDriverWait(driver, 20).until(EC.url_contains("/dashboard"))
        time.sleep(3)

        daily_report_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Daily Report']"))
        )
        daily_report_button.click()


        WebDriverWait(driver, 20).until(EC.url_contains("/daily-report"))
        time.sleep(3)

        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Search']"))
        )
        search_button.click()
       
        time.sleep(3)
        print("Daily Report Search test completed successfully.")

        bkash_transaction_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='BKash Transaction']"))
        )
        bkash_transaction_button.click()

        time.sleep(3)


        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'text-right')]/button[text()='Search']"))
        )
        search_button.click()
        time.sleep(4)

        transaction_list_present = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'search-account')]"))
        )
        if transaction_list_present:
            print("Transaction list displayed successfully.")
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


        save_pdf_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Save Pdf']"))
        )
        save_pdf_button.click()
        time.sleep(5)

        download_csv_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Download CSV']"))
        )
        download_csv_button.click()
        time.sleep(5)

        print("BKash transaction export test completed successfully.")

        upay_transaction_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Upay Transaction']"))
        )
        upay_transaction_button.click()

        time.sleep(3)


        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'text-right')]/button[text()='Search']"))
        )
        search_button.click()
        time.sleep(3)

        transaction_list_present = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'search-account')]"))
        )
        if transaction_list_present:
            print("Upay Transaction list displayed successfully.")

        time.sleep(4)


        save_pdf_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Save Pdf']"))
        )
        save_pdf_button.click()
        time.sleep(5)

        download_csv_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Download CSV']"))
        )
        download_csv_button.click()
        time.sleep(5)

        print("Upay transaction export test completed successfully.")


    finally:
        input("Press Enter to close the browser")

if __name__ == "__main__":
    test_Login_Reviewing_Info()
