from .locators import FightDetailsPageLocator

class Table:
  def __init__(self, element):
    self.element = element

  def get_cells_of_column(self, index):
    cols = self.element.find_elements(*FightDetailsPageLocator.TOTALS_COLS)[index]
    return cols.find_elements(*FightDetailsPageLocator.COL_CONTENTS)
  
  def get_kds(self):
    cells = self.get_cells_of_column(1)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }
  
  def get_sig_str(self):
    cells = self.get_cells_of_column(2)
    return {
      'red': tuple(cells[0].text.split(' of ')),
      'blue': tuple(cells[1].text.split(' of '))
    }
  
  def get_sig_str_acc(self):
    cells = self.get_cells_of_column(3)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }
  
  def get_str(self):
    cells = self.get_cells_of_column(4)
    return {
      'red': tuple(cells[0].text.split(' of ')),
      'blue': tuple(cells[1].text.split(' of '))
    }
  
  def get_td(self):
    cells = self.get_cells_of_column(5)
    return {
      'red': tuple(cells[0].text.split(' of ')),
      'blue': tuple(cells[1].text.split(' of '))
    }
  
  def get_td_acc(self):
    cells = self.get_cells_of_column(6)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }
  
  def get_sub_att(self):
    cells = self.get_cells_of_column(7)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }
  
  def get_rev(self):
    cells = self.get_cells_of_column(8)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }
  
  def get_ctrl(self):
    cells = self.get_cells_of_column(9)
    return {
      'red': cells[0].text,
      'blue': cells[1].text
    }