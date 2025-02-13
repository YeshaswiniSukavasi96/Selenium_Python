from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.com/")
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox").send_keys("mug")
driver.find_element(By.ID,"nav-search-submit-button").click()
mug_list=driver.find_elements(By.CSS_SELECTOR,"div[role='listitem']")
print("Mugs Count:",len(mug_list))
cnt=0
for mugs in mug_list:
   name= mugs.find_element(By.CSS_SELECTOR,"h2")
   cnt=cnt+1
   print("Mug ",cnt,":",name.text)
   if cnt==5:
       break

