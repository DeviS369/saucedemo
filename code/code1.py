from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
    driver.get("https://www.saucedemo.com/")
    username = "standard_user"
    password = "secret_sauce"
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    title = driver.title
    print(f"Webpage Title: {title}")
    current_url = driver.current_url
    print(f"Current URL: {current_url}")
    page_source = driver.page_source
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(page_source)
    print("Webpage content saved to 'Webpage_task_11.txt'")

finally:
    driver.quit()
