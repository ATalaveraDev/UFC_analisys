from .round import Round
from .table import Table
from .page import BasePage
from .locators import FightDetailsPageLocator

class FightDetailsPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.totals_section = Table(self.driver.find_elements(*FightDetailsPageLocator.TABLE_SECTION)[1])
    self.striking_rounds_section = Table(self.driver.find_elements(*FightDetailsPageLocator.TABLE_SECTION)[2])

  def get_fighters(self):
    fighters = self.driver.find_elements(*FightDetailsPageLocator.FIGHTERS)
    return {
      'red': fighters[0].find_element(*FightDetailsPageLocator.FIGHTER_NAME).text,
      'blue': fighters[1].find_element(*FightDetailsPageLocator.FIGHTER_NAME).text
    }
  
  def get_cells_of_column(self, index):
    return self.totals_section.get_cells_of_column(index)
  
  def get_total_kds(self):
    return self.totals_section.get_kds()
  
  def get_total_sig_str(self):
    return self.totals_section.get_sig_str()

  def get_total_sig_str_acc(self):
    return self.totals_section.get_sig_str_acc()
  
  def get_total_str(self):
    return self.totals_section.get_str()

  def get_total_td(self):
    return self.totals_section.get_td()
  
  def get_total_td_acc(self):
    return self.totals_section.get_td_acc()

  def get_total_sub_att(self):
    return self.totals_section.get_sub_att()

  def get_total_rev(self):
    return self.totals_section.get_rev()

  def get_total_ctrl(self):
    return self.totals_section.get_ctrl()
  
  def get_striking_rounds(self, index):
    try:
      return [Round(self.driver, i+1) for i in range(len(self.striking_rounds_section.element.find_elements(*FightDetailsPageLocator.ROUND_HEADER)))][index]
    except:
      return None
  
  def get_totals(self):
    return self.get_total_kds(), self.get_total_sig_str(), self.get_total_sig_str_acc(), self.get_total_str(), self.get_total_td(), self.get_total_td_acc(), self.get_total_sub_att(), self.get_total_rev(), self.get_total_ctrl()