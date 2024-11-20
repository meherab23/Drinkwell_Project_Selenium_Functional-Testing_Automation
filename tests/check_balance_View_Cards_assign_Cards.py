from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time 

def test_login_and_check_balance_view_cards_assign_Cards():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("http://13.214.1.75/#/login")

        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))
        )
        username_field.send_keys("me.po")

        password_field = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password_field.send_keys("1234")

        login_button = driver.find_element(By.XPATH, '//button')
        login_button.click()

        WebDriverWait(driver, 20).until(
            EC.url_contains("/home")
        )

        account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='menu-label d-flex align-items-center mt-2' and text()=' Account ']"))
        )
        account_button.click()

        WebDriverWait(driver, 20).until(
            EC.url_contains("/account")
        )

        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary' and text()='Search']"))
        )
        search_button.click()

        time.sleep(2) 

        action_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select[@class='form-control' and @name='name625996251']"))
        )
        time.sleep(1)
        select = Select(action_dropdown)
        select.select_by_visible_text("Check Balance")

        time.sleep(3)

        print("Test completed successfully and 'Check Balance' option selected.")


        action_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select[@class='form-control' and @name='name625996251']"))
        )
        time.sleep(1)
        select = Select(action_dropdown)
        select.select_by_visible_text("View Cards")

        time.sleep(2)

        action_dropdown = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-search-account/div[1]/div/div/div[2]/div[2]/table/tbody/tr[3]/td[10]/select"))
        )
        time.sleep(1)
        select = Select(action_dropdown)
        select.select_by_visible_text("Add Cards")

        time.sleep(2)

        modal = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']"))
        )
        print("Modal is visible.")
        time.sleep(1)

        card_input_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-search-account/div[4]/div/div/div[2]/div/div/div/input"))
        )

        time.sleep(2)
        ActionChains(driver).move_to_element(card_input_field).click().perform()
        card_input_field.send_keys("1215346755") 
        print("Card number entered.")

        time.sleep(2)

        assign_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-search-account/div[4]/div/div/div[3]/button[1]"))
        )
        ActionChains(driver).move_to_element(assign_button).click().perform()
        print("Assign button clicked.")

        time.sleep(2)
        print("Test completed successfully: Card added and assigned.")

    finally:
        input("Press Enter to exit and close the browser")
        driver.quit()

if __name__ == "__main__":
    test_login_and_check_balance_view_cards_assign_Cards()
