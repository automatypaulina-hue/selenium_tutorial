from selenium.webdriver import Chrome
from time import sleep

#stworzenie instalacji klasy Chrome
#(to otworzy przegladarke)
driver = Chrome()
#Otwarcie strony
driver.get("https://www.kozminski.edu.pl/pl")
#Maksymalizacja okna
driver.maximize_window()
sleep(5)
driver.quit()

