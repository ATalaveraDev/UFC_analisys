

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
  def __init__(self, driver):
    super().__init__(driver)
    self.totals_section = self.driver.find_elements(*FightDetailsPageLocator.TOTALS_SECTION)[1]

  def get_fighters(self):
    fighters = self.driver.find_elements(*FightDetailsPageLocator.FIGHTERS)
    return {
      'red': fighters[0].find_element(*FightDetailsPageLocator.FIGHTER_NAME).text,
      'blue': fighters[1].find_element(*FightDetailsPageLocator.FIGHTER_NAME).text
    }
  
  def get_cells_of_column(self, index):
    cols = self.totals_section.find_elements(*FightDetailsPageLocator.TOTALS_COLS)[index]
    return cols.find_elements(*FightDetailsPageLocator.COL_CONTENTS)
  
  def get_total_kds(self):
    cells = self.get_cells_of_column(1)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }
  
  def get_total_sig_str(self):
    cells = self.get_cells_of_column(2)
    return {
      'red': tuple(cells[0].text.split(' of ')),
      'blue': tuple(cells[1].text.split(' of '))
    }

  def get_total_sig_str_acc(self):
    cells = self.get_cells_of_column(3)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }
  
  def get_total_str(self):
    cells = self.get_cells_of_column(4)
    return {
      'red': tuple(cells[0].text.split(' of ')),
      'blue': tuple(cells[1].text.split(' of '))
    }

  def get_total_td(self):
    cells = self.get_cells_of_column(5)
    return {
      'red': tuple(cells[0].text.split(' of ')),
      'blue': tuple(cells[1].text.split(' of '))
    }
  
  def get_total_td_acc(self):
    cells = self.get_cells_of_column(6)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }

  def get_total_sub_att(self):
    cells = self.get_cells_of_column(7)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }

  def get_total_rev(self):
    cells = self.get_cells_of_column(8)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }

  def get_total_ctrl(self):
    cells = self.get_cells_of_column(9)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }
    
  
