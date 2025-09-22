from .page import BasePage
from .locators import FightDetailsPageLocator

class FightDetailsPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.totals_section = self.driver.find_elements(*FightDetailsPageLocator.TABLE_SECTION)[1]
    self.rounds_section = self.driver.find_elements(*FightDetailsPageLocator.TABLE_SECTION)[2]

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
    