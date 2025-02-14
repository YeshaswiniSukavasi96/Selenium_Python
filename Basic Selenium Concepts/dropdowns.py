from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.amazon.com/")
# Refreshing page again because sometimes amazon page is displayed without dropdowns and search icon but displayed with GO icon which wont be passed through this program
driver.refresh()
driver.maximize_window()
#Selecting value from dropdown of departments in search bar
dropdown=driver.find_elements(By.CSS_SELECTOR,"#searchDropdownBox option")
for dp in dropdown:
    if dp.text=="Home & Kitchen":
        dp.click()
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mugs")
driver.find_element(By.ID,"nav-search-submit-button").click()
#sorting by best-selling Mugs
Select(driver.find_element(By.ID,"s-result-sort-select")).select_by_visible_text("Best Sellers")
mug_list = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")
print("Total Mugs in the page loaded:", len(mug_list))
print("Displaying Top 5 Best Selling Mugs:")
cnt = 0
#looping through all mugs displayed in the page and getting top 5 best-selling mugs
for mugs in mug_list:
    name = mugs.find_element(By.CSS_SELECTOR, "h2")
    price=mugs.find_element(By.CSS_SELECTOR,"span[class='a-price'] span")
    cnt = cnt + 1
    print("Mug", cnt, "\nName :",name.text,"\nPrice :",price.get_attribute("innerHTML"))
    if cnt == 5:
        break
driver.close()
