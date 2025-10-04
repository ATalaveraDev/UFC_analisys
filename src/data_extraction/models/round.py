from config import BLUE, RED

class Round:
  def __init__(self, index):
    self.index = index
    self.red_kds = "---"
    self.blue_kds = "---"
    self.red_atmpd_sig_strikes = "---"
    self.red_landed_sig_strikes = "---"
    self.blue_atmpd_sig_strikes = "---"
    self.blue_landed_sig_strikes = "---"

  def set_sig_strikes(self, data):
    self.red_atmpd_sig_strikes = data[RED][0]
    self.red_landed_sig_strikes = data[RED][1]
    self.blue_atmpd_sig_strikes = data[BLUE][0]
    self.blue_landed_sig_strikes = data[BLUE][1]

  def get_sig_strikes(self):
    return f",{self.red_atmpd_sig_strikes},{self.red_landed_sig_strikes},{self.blue_atmpd_sig_strikes},{self.blue_landed_sig_strikes}"
  
  def get_kds(self):
    return f",{self.red_kds},{self.blue_kds}"
  
  def set_kds(self, data):
    self.red_kds = data[RED]
    self.blue_kds = data[BLUE]
    
  def __str__(self):
    return f"{self.get_kds()}{self.get_sig_strikes()}"