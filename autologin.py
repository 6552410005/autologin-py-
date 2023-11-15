from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# สร้าง WebDriver (ChromeDriver)
driver = webdriver.Chrome()

# เปิดเว็บไซต์
driver.get("https://cert.sau.ac.th:8090/")

# ค้นหา element และกรอกข้อมูล
element = driver.find_element("xpath", "//input[@id='username']")
element.send_keys("s6552410005")
element = driver.find_element("xpath", "//input[@id='password']")
element.send_keys("s6552410005")

# ตัวอย่างอื่น ๆ ที่คุณอาจต้องการทำ:
# - คลิกปุ่ม: element.click()
element.send_keys(Keys.RETURN)

# รอเว็บไซต์โหลดเสร็จสมบูรณ์
time.sleep(100)

# ปิดเบราว์เซอร์
#driver.quit()
