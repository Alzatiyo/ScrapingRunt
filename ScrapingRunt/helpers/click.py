import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click(driver, by, selector, timeout=15):

    elem = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, selector)))

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});", elem)

    time.sleep(0.3)
    elem.click()

    return elem