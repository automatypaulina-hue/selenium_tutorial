from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
DATA_EMAIL = "kowalski@spam.pl"

#stworzenie instalacji klasy Chrome
#(to otworzy przegladarke)
driver = Chrome()
#Otwarcie strony
driver.get("https://automationpractice.techwithjatin.com/")
#Maksymalizacja okna
driver.maximize_window()

#Znajdzelement Sign in
sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
#kliknij w odnaleziony element
sign_in_a.click()
driver.find_element(By.ID, "email_create").send_keys(DATA_EMAIL)

print(type(sign_in_a))
sleep(3)




