from .page import BasePage
from .locators import FightDetailsPageLocator

class Round(BasePage):
  def __init__(self, driver, round_index):
    super().__init__(driver)
    self.section = self.driver.find_elements(*FightDetailsPageLocator.TABLE_SECTION)[2]
    self.row = self.section.find_elements(*FightDetailsPageLocator.ROUND_BODY)[round_index].find_element(*FightDetailsPageLocator.ROUND_ROW)

  def get_cells_of_column(self, index):
    cols = self.row.find_elements(*FightDetailsPageLocator.TOTALS_COLS)[index]
    return cols.find_elements(*FightDetailsPageLocator.COL_CONTENTS)
  
  def get_kds(self):
    cells = self.get_cells_of_column(1)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }