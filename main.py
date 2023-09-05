from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = 'patrykbarnas@yahoo.com'
ACCOUNT_PASSWORD = 'Iampatty1996!'
# PHONE = 7083517684


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3704509790&distance=&f_AL=true&f_BE=&f_C=&f_CM=&f_CR=&f_CT=&f_E=&f_EA=&f_EL=&f_ES=&f_ET=&f_F=&f_FCE=&f_GC=&f_I=&f_JC=&f_JIYN=&f_JT=&f_LF=&f_PP=&f_SAL=&f_SB=&f_SB2=&f_SB3=&f_T=&f_TP=&f_TPR=r86400&f_WT=3%2C2&geoId=103644278&keywords=frontend%20developer&latLong=&location=United%20States&refresh=true&sortBy=&start=0")

# Click Reject Cookies Button
# time.sleep(2)
# reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
# reject_button.click()

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, value=".scaffold-layout__list-container li")

# Apply for Jobs
for listing in all_listings:
    # already_applied = driver.find_element(By.CSS_SELECTOR, value=".artdeco-inline-feedback--success")
    listing.click()
    time.sleep(2)

    try:
        #Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        # if phone.text == "":
        #     phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

            # Click Submit Button
            print("Submitting job application")

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        # abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()