from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_Setting():
    options = Options()
    options.headless = False
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.set_page_load_timeout(60)
        driver.get("http://13.214.1.75/#/login")

        print("Step 1: Logging in")
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))
        )
        username_field.send_keys("ns.sa")
        
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))
        )
        password_field.send_keys("1234")
        
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button'))
        )
        login_button.click()

        WebDriverWait(driver, 20).until(EC.url_contains("/home"))
        print("Step 2: Landed on Home Page")

        settings_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Setting"]'))
        )
        settings_button.click()

        time.sleep(2)

        zone_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@routerlink='/setting/zone' and contains(text(), 'Zone')]"))
        )
        zone_button.click()

        time.sleep(2)

        add_new_zone_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='btn btn-sm btn-primary' and text()='Add New Zone']"))
        )
        add_new_zone_button.click()

        time.sleep(2)

        zone_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Zone Name']"))
        )
        zone_name_input.send_keys("New Zone")

        time.sleep(1)

        zone_address_input = driver.find_element(By.XPATH, "//textarea[@placeholder='Zone Address']")
        zone_address_input.send_keys("Shaymoli")
        time.sleep(1)

        zone_location_input = driver.find_element(By.XPATH, "//input[@placeholder='Zone Location']")
        zone_location_input.send_keys("Mirpur11")

        time.sleep(3)

        save_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-sm btn-success']"))
        )
        save_button.click()

        time.sleep(3)

        settings_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='px-3' and text()='Setting']"))
        )
        settings_button.click()

        time.sleep(2)

        vendor_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@routerlink='/setting/vendor' and contains(text(), 'Vendor')]"))
        )
        vendor_button.click()

        time.sleep(2)

        add_new_vendor_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='btn btn-sm btn-primary' and text()='Add New Vendor']"))
        )
        add_new_vendor_button.click()

        vendor_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Vendor Name']"))
        )
        vendor_name_input.send_keys("New Vendoe")

        time.sleep(2)

        vendor_description_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Vendor Description']"))
        )
        vendor_description_input.send_keys("Vendor BC.")

        time.sleep(2)

        vendor_address_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Vendor Address']"))
        )
        vendor_address_input.send_keys("Main Street")

        time.sleep(2)

        save_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-sm btn-success']"))
        )
        save_button.click()

        time.sleep(4)

        print("Test completed successfully and new vendor saved.")

        print("Step 4: Navigating to Pump Settings")
        pump_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@routerlink="/setting/booth"]'))
        )
        pump_button.click()

        print("Step 5: Clicking Add New Pump Button")
        add_new_pump_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@routerlink="/setting/booth/new"]'))
        )
        add_new_pump_button.click()

        print("Step 6: Filling Add New Pump Form")

        time.sleep(2)

        zone_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/app-root/app-layout/div/section/app-setting-layout/div/div/div/app-pump-edit/div/div/div/div[2]/div/div[2]/div[1]/div[1]/select'))
        )
        Select(zone_dropdown).select_by_index(3)

        time.sleep(2)

        vendor_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/app-root/app-layout/div/section/app-setting-layout/div/div/div/app-pump-edit/div/div/div/div[2]/div/div[2]/div[1]/div[2]/select'))
        )
        Select(vendor_dropdown).select_by_index(2)

        time.sleep(2)

        name_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/app-root/app-layout/div/section/app-setting-layout/div/div/div/app-pump-edit/div/div/div/div[2]/div/div[2]/div[1]/div[7]/input'))
        )
        name_field.send_keys("Test Pump 220")

        time.sleep(2)

        print("Step 7: Scrolling to Save Button")
        save_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/app-root/app-layout/div/section/app-setting-layout/div/div/div/app-pump-edit/div/div/div/div[2]/div/div[2]/div[2]/button'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", save_button) 
        
        time.sleep(2)

        print("Step 8: Saving the Pump Data")
        save_button.click()

        time.sleep(3)


        settings_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='px-3' and text()='Setting']"))
        )
        settings_button.click()

        time.sleep(2)

        print("Step 4: Navigating to ATM Settings")
        atm_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/app-root/app-layout/app-header/app-sidebar/aside/div/section/ul/li[10]/ul/li[4]/a'))
        )
        atm_button.click()

        WebDriverWait(driver, 20).until(EC.url_contains("/setting/device"))

        time.sleep(2)
        print("Step 5: Navigating to Add New ATM Page")
        new_atm_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/app-root/app-layout/div/section/app-setting-layout/div/div/div/app-atm/div[2]/div[1]/div[1]/a'))
        )
        new_atm_button.click()

        time.sleep(2)

        WebDriverWait(driver, 20).until(EC.url_contains("setting/device/new"))

        print("Step 6: Filling out the Add ATM Form")

        pump_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/app-root/app-layout/div/section/app-setting-layout/div/div/div/app-atm-edit/form/div/div[1]/div[1]/div/select'))
        )
        Select(pump_dropdown).select_by_index(1) 

        time.sleep(2)
    
        serial_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/app-root/app-layout/div/section/app-setting-layout/div/div/div/app-atm-edit/form/div/div[1]/div[2]/div/input'))
        )
        serial_field.send_keys("DVB1113")

        time.sleep(2)

        calibration_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/app-root/app-layout/div/section/app-setting-layout/div/div/div/app-atm-edit/form/div/div[1]/div[7]/div/input'))
        )
        calibration_field.send_keys("0.89")

        time.sleep(2)

        save_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/app-root/app-layout/div/section/app-setting-layout/div/div/div/app-atm-edit/form/div/div[3]/button'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
        time.sleep(2)

        print("Step 7: Saving the New ATM")
        save_button.click()

        time.sleep(2)

        WebDriverWait(driver, 20).until(EC.url_contains("/setting/booth"))
        print("ATM added successfully!")

        time.sleep(2)


        user_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@routerlink='/setting/user' and contains(text(), 'User')]"))
        )
        user_button.click()

        WebDriverWait(driver, 20).until(
            EC.url_contains("/setting/user")
        )
        time.sleep(3)

        create_new_user_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@routerlink='/setting/user/new' and contains(text(), 'Create new user')]"))
        )
        time.sleep(1)
        create_new_user_button.click()

        WebDriverWait(driver, 20).until(
            EC.url_contains("/setting/user/new")
        )
        time.sleep(1)

        name_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='Name']"))
        )
        name_input.send_keys("Riyan Meherab")

        time.sleep(2)

        surname_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='Surname']"))
        )
        surname_input.send_keys("Khan")

        time.sleep(2)

        username_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='UserName']"))
        )
        username_input.send_keys("mehe.GG")

        time.sleep(2)

        cellphone_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='CellPhone']"))
        )
        cellphone_input.send_keys("01860668740")

        time.sleep(2)

        email_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='Email']"))
        )
        email_input.send_keys("meherab25@example.com")

        time.sleep(2)

        password_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']"))
        )
        password_input.send_keys("pass1234")

        time.sleep(2)

        user_type_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='UserTypeId']"))
        )
        select_user_type = Select(user_type_select)
        select_user_type.select_by_value("2")  

        time.sleep(2)

       
        status_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='Status']"))
        )
        select_status = Select(status_select)
        select_status.select_by_value("1") 

        time.sleep(2)

     
        save_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-sm btn-success']"))
        )
        save_button.click()

        time.sleep(4)

        print("Test completed successfully and new user saved.")


        cost_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@routerlink='/setting/cost' and contains(text(), 'Cost')]"))
        )
        cost_button.click()

        WebDriverWait(driver, 20).until(
            EC.url_contains("/setting/cost")
        )
        time.sleep(2)

        edit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-pencil']"))
        )
        edit_button.click()
        time.sleep(2)

        update_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-sm btn-success']"))
        )
        update_button.click()

        time.sleep(2)

        modal = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']"))
        )

        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password' and @type='password']"))
        )

        time.sleep(2)

        ActionChains(driver).move_to_element(password_input).click().perform()
        password_input.send_keys("1234") 
        time.sleep(2) 

        ok_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success' and @type='submit' and text()='Ok']"))
        )
        ok_button.click()

        time.sleep(3)
        print("Cost updated and password assigned successfully.")

       
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        input("Press Enter to exit and close the browser")
        driver.quit()

if __name__ == "__main__":
    test_Setting()
