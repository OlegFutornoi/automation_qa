from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def open (self):
        self.driver.get(self.url)


    def element_is_visible(self, locator, timeouts=5):
        return wait(self.driver, timeouts).until(EC.visibility_of_element_located(locator))

    def elements_ar_visible(self, locator, timeouts=5):
        return wait(self.driver, timeouts).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeouts=5):
        return wait(self.driver, timeouts).until(EC.presence_of_element_located(locator))

    def element_is_not_visible(self, locator, timeouts=5):
        return wait(self.driver, timeouts).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeouts=5):
        return wait(self.driver, timeouts).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollInfoView();", element)






