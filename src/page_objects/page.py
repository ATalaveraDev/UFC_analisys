

from .locators import EventPageLocators, EventsListPageLocators
from models.ufc_event import UFC_Event

class BasePage(object):
  def __init__(self, driver):
    self.driver = driver

class EventsListPage(BasePage):
  def get_events(self):
    return self.driver.find_elements(*EventsListPageLocators.ROWS)[2:]
  
  def get_event_details(self, event):
    event.find_element(*EventsListPageLocators.EVENT_LINK).click()
    event_page = EventPage(self.driver)
    event = UFC_Event(event_page.get_title(), event_page.get_date())
    print(event)
    self.driver.execute_script("window.history.go(-1)")

class EventPage(BasePage):
  def get_title(self):
    return self.driver.find_element(*EventPageLocators.TITLE).text
  
  def get_date(self):
    return self.driver.find_element(*EventPageLocators.DATE).get_attribute('innerText')