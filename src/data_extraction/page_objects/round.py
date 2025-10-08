from .page import BasePage
from .table import Table
from .locators import FightDetailsPageLocator

class Round(BasePage):
  def __init__(self, driver, round_index):
    super().__init__(driver)
    self.index = round_index
    self.section = self.driver.find_elements(*FightDetailsPageLocator.TABLE_SECTION)[2]
    self.row = Table(self.section.find_elements(*FightDetailsPageLocator.ROUND_BODY)[self.index].find_element(*FightDetailsPageLocator.ROUND_ROW))

  def open(self):
    self.section.click()
  
  def get_kds(self):
    return self.row.get_kds()
  
  def get_sig_str(self):
    return self.row.get_sig_str()
  
  def get_sig_str_acc(self):
    return self.row.get_sig_str_acc()
  
  def get_str(self):
    return self.row.get_str()

  def get_td(self):
    return self.row.get_td()
  
  def get_td_acc(self):
    return self.row.get_td_acc()

  def get_sub_att(self):
    return self.row.get_sub_att()

  def get_rev(self):
    return self.row.get_rev()

  def get_ctrl(self):
    return self.row.get_ctrl()
  
  def get_stats(self):
    return self.get_kds(), self.get_sig_str(), self.get_sig_str_acc(), self.get_str(), self.get_td(), self.get_td_acc(), self.get_sub_att(), self.get_rev(), self.get_ctrl()