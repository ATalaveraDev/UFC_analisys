

from .locators import EventPageLocators, EventsListPageLocators, FightDetailsPageLocator

class BasePage(object):
  def __init__(self, driver):
    self.driver = driver

class EventsListPage(BasePage):
  def get_events_links(self):
    rows = self.driver.find_elements(*EventsListPageLocators.ROWS)
    return [row.get_attribute('href') for row in rows]

class EventPage(BasePage):
  def get_title(self):
    return self.driver.find_element(*EventPageLocators.TITLE).text
  
  def get_date(self):
    return self.driver.find_element(*EventPageLocators.DATE).get_attribute('innerText')
  
  def get_fights_links(self):
    rows = self.driver.find_elements(*EventPageLocators.FIGHTS)
    return [row.get_attribute('data-link') for row in rows]
  
class FightDetailsPage(BasePage):
  def get_fighters(self):
    fighters = self.driver.find_elements(*FightDetailsPageLocator.FIGHTERS)
    return {
      'red': fighters[0].find_element(*FightDetailsPageLocator.FIGHTER_NAME).text,
      'blue': fighters[1].find_element(*FightDetailsPageLocator.FIGHTER_NAME).text
    }
  
