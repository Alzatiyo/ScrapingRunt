import time
from selenium.webdriver.common.by import By

def expandir_todos_los_paneles(driver):

    print("  Expandiendo todos los paneles...")

    for _ in range(3):

        cerrados = driver.find_elements(
            By.XPATH,
            "//mat-expansion-panel[not(contains(@class,'mat-expanded'))]//mat-expansion-panel-header"
        )

        if not cerrados:
            break

        for header in cerrados:

            try:
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", header)

                time.sleep(0.2)

                header.click()

                time.sleep(0.4)

            except Exception:
                pass

        time.sleep(1.5)

    print("  Paneles expandidos.")