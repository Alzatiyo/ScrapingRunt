import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def escribir(driver, by, selector, texto, timeout=15):

    elem = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, selector)))

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});", elem)

    time.sleep(0.2)
    elem.click()
    elem.clear()

    for char in texto:
        elem.send_keys(char)
        time.sleep(0.04)

    return elem