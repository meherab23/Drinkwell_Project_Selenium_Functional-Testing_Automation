from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_add_new_card_recharge_card_assign_card_to_user():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("http://13.214.1.75/#/login")

        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))
        )
        username_field.send_keys("ns.sa")
        time.sleep(2)

        password_field = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password_field.send_keys("1234")
        time.sleep(2)

        login_button = driver.find_element(By.XPATH, '//button')
        login_button.click()

        WebDriverWait(driver, 20).until(
            EC.url_contains("/home")
        )
        time.sleep(2)
        card_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='menu-label d-flex align-items-center mt-2' and text()=' Card ']"))
        )
        card_button.click()

        time.sleep(3)

        add_new_card_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='btn btn-sm btn-primary' and text()='Add New Card']"))
    )
        add_new_card_button.click()

        time.sleep(3)

        card_number_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='cardNumber']"))
    )
        card_number_input.send_keys("1215346770")
        time.sleep(3)

        card_details_input = driver.find_element(By.XPATH, "//input[@id='card-details']")
        card_details_input.send_keys("Card 07")
        time.sleep(3)

        issue_date_input = driver.find_element(By.XPATH, "//input[@placeholder='Issue Date']")
        issue_date_input.send_keys("11/14/2024")

        expire_date_input = driver.find_element(By.XPATH, "//input[@placeholder='Expire Date']")
        expire_date_input.send_keys("12/15/2024")

        save_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-sm btn-success']"))
     )
        save_button.click()

        time.sleep(2)

        
        recharge_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@routerlink="/recharge"]'))
        )
        recharge_button.click()

        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Search"]'))
        )
        search_button.click()
        time.sleep(2)

        new_recharge_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@routerlink="/recharge/new"]'))
        )
        new_recharge_button.click()
        time.sleep(2)

        recharge_type_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//select[contains(@class, "form-control")][1]'))
        )
        Select(recharge_type_dropdown).select_by_visible_text("Hand Cash")

        ref_no_field = driver.find_element(By.XPATH, '(//input[@type="text"])[1]')
        ref_no_field.send_keys("REF12345")
        time.sleep(2)

        recharge_using_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '(//select[contains(@class, "form-control")])[2]'))
        )
        Select(recharge_using_dropdown).select_by_visible_text("Account No")
        time.sleep(2)

        recharge_to_field = driver.find_element(By.XPATH, '//input[@id="card-details"]')
        recharge_to_field.send_keys("1215346770")
        time.sleep(2)

        amount_field = driver.find_element(By.XPATH, '(//input[@type="text"])[3]')
        amount_field.send_keys("1")
        time.sleep(2)

        save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
        save_button.click()

        time.sleep(2)
        print("Recharge process completed successfully.")

        card_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@routerlink="/card"]'))
        )
        card_button.click()
        time.sleep(2)

        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Search"]'))
        )
        search_button.click()
        time.sleep(2)

        assign_to_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-target="#assignToModal"]'))
        )
        assign_to_button.click()
        time.sleep(2)


        account_number_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//label[text()="Account Number"]/following-sibling::div//input[@type="text"]')
            )
        )
        account_number_field.send_keys("1234567890")
        time.sleep(2)

        assign_button = driver.find_element(By.XPATH, '//div[@class="modal-footer"]//button[text()="Assign"]')
        assign_button.click()
        time.sleep(2)

        print("Card assignment process completed successfully.")


    finally:
        input("Press Enter to close the browser")
        driver.quit()

test_add_new_card_recharge_card_assign_card_to_user()
