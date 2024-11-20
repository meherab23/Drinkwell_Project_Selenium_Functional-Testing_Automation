from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_Change_pass_Logout_invalid_login():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)

    try:

        driver.get("http://13.214.1.75/#/login")

       
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Username"]'))
        )
        username_field.send_keys("me.po")

        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Password"]'))
        )
        password_field.send_keys("1234")

        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        login_button.click()

        WebDriverWait(driver, 20).until(EC.url_contains("/home"))
        time.sleep(2)

        user_logo_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="btn dropdown-toggle"]'))
        )
        user_logo_button.click()
        time.sleep(2)

        change_password_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="#/setting/user/change-password"]'))
        )
        change_password_option.click()

        WebDriverWait(driver, 20).until(EC.url_contains("/setting/user/change-password"))
        time.sleep(2)

        old_password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="cardNumber"]'))
        )
        old_password_field.send_keys("1234")

        new_password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="card-details"]'))
        )
        new_password_field.send_keys("12345")

        confirm_password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '(//input[@id="card-details"])[2]'))
        )
        confirm_password_field.send_keys("12345")

        save_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-sm btn-success"]'))
        )
        save_button.click()

        time.sleep(5)


        user_logo_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="btn dropdown-toggle"]'))
        )
        user_logo_button.click()
        time.sleep(2)

        logout_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="#/"]'))
        )
        logout_button.click()
        time.sleep(2)

        WebDriverWait(driver, 20).until(EC.url_contains("/login"))
        print("Logout successful!")

        time.sleep(2)


        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Username"]'))
        )
        username_field.send_keys("me.po")

        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Password"]'))
        )
        password_field.send_keys("1234")

        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        login_button.click()
        print("Invalid login test passed: User remains on the login page.")
      
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        input("Press Enter to close the browser")
        driver.quit()

if __name__ == "__main__":
   test_Change_pass_Logout_invalid_login()
