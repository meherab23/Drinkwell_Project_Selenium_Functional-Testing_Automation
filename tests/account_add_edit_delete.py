from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_account_add_edit_delete():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("http://13.214.1.75/#/login")

        time.sleep(2)

        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))
        )
        username_field.send_keys("ns.sa")

        time.sleep(1)

        password_field = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password_field.send_keys("1234")

        login_button = driver.find_element(By.XPATH, '//button')
        login_button.click()

        time.sleep(1)

        WebDriverWait(driver, 20).until(EC.url_contains("/home"))

        time.sleep(2)


        account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='menu-label d-flex align-items-center mt-2' and text()=' Account ']"))
        )
        account_button.click()

        time.sleep(1)

        WebDriverWait(driver, 20).until(
            EC.url_contains("/account")
        )
        time.sleep(2)

        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary' and text()='Search']"))
        )
        search_button.click()

        time.sleep(2)

        action_dropdown = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-search-account/div[1]/div/div/div[2]/div[2]/table/tbody/tr[3]/td[10]/select"))
        )
        select = Select(action_dropdown)
        select.select_by_visible_text("Edit")

        WebDriverWait(driver, 20).until(
            EC.url_contains("/edit")
        )
        time.sleep(1)

        delete_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-add-account/div/div/div/form/div[2]/div[4]/button[1]"))
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", delete_button)
        time.sleep(2)

        delete_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-add-account/div/div/div/form/div[2]/div[4]/button[1]"))
        )
        delete_button.click()

        time.sleep(2)

        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

        time.sleep(2)

        WebDriverWait(driver, 20).until(
            EC.url_contains("/account")
        )
        time.sleep(2)

        action_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select[@class='form-control' and @name='name625996251']"))
        )
        select = Select(action_dropdown)
        select.select_by_visible_text("Edit")

        WebDriverWait(driver, 20).until(
            EC.url_contains("/edit")
        )
        time.sleep(2)

        name_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='customerName']"))
        )
        name_field.clear()
        name_field.send_keys("Rakib Khan")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        update_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Update Account']"))
        )
        update_button.click()


        add_new_account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-search-account/div[1]/div/div/div[2]/div[1]/div[1]/a"))
        )
        add_new_account_button.click()
        time.sleep(2)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-add-account/div/div/div/form"))
        )
        time.sleep(2)

        card_number_field = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-add-account/div/div/div/form/div[2]/div[1]/div[1]/div[1]/div[1]/input")
        card_number_field.send_keys("1215346770")
        time.sleep(1)

        customer_name_field = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-add-account/div/div/div/form/div[2]/div[1]/div[1]/div[2]/div/input[1]")
        customer_name_field.send_keys("Riyan Chowdhury")
        time.sleep(1)

        identity_dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-add-account/div/div/div/form/div[2]/div[1]/div[1]/div[2]/div/select[1]"))
        )
        identity_dropdown.click()
        time.sleep(1)

        identity_option = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//option[text()='Nid']"))
        )
        identity_option.click()
        time.sleep(1)

        identity_no_field = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-add-account/div/div/div/form/div[2]/div[1]/div[1]/div[2]/div/input[2]")
        identity_no_field.send_keys("987654321")
        time.sleep(2)

        mobile_no_field = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-add-account/div/div/div/form/div[2]/div[1]/div[1]/div[2]/div/input[3]")
        mobile_no_field.send_keys("0123456789")
        time.sleep(2)

        gender_dropdown = Select(driver.find_element(By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-add-account/div/div/div/form/div[2]/div[1]/div[1]/div[2]/div/select[2]"))
        gender_dropdown.select_by_visible_text("Male")
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        create_account_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/app-root/app-layout/div/section/app-add-account/div/div/div/form/div[2]/div[4]/button"))
        )
        create_account_button.click()
        time.sleep(3)

        WebDriverWait(driver, 20).until(EC.url_contains("/account"))
        time.sleep(4)

    finally:
        input("Press Enter to close the browser")
        driver.quit()

test_account_add_edit_delete()
