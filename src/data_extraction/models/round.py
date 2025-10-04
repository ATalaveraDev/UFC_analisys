from config import BLUE, RED

class Round:
  def __init__(self, index):
    self.index = index

  def set_kds(self, data):
    if self.index == 1:
      self.red_r1_kds = data[RED]
      self.blue_r1_kds = data[BLUE]
    if self.index == 2:
      self.red_r2_kds = data[RED]
      self.blue_r2_kds = data[BLUE]
    if self.index == 3:
      self.red_r3_kds = data[RED]
      self.blue_r3_kds = data[BLUE]

  def get_kds(self):
    res = ''
    if hasattr(self, 'red_r1_kds') and hasattr(self, 'blue_r1_kds'):
      res += f',{self.red_r1_kds},{self.blue_r1_kds}'
    else:
      res += ',null,null'
    if hasattr(self, 'red_r2_kds') and hasattr(self, 'blue_r2_kds'):
      res += f',{self.red_r2_kds},{self.blue_r2_kds}'
    else:
      res += ',null,null'
    if hasattr(self, 'red_r3_kds') and hasattr(self, 'blue_r3_kds'):  
      res += f',{self.red_r3_kds},{self.blue_r3_kds}'
    else:
      res += ',null,null'
    return res

  def set_sig_strikes(self, data):
    if self.index == 1:
      self.red_r1_atmpd_sig_strikes = data[RED][0]
      self.red_r1_landed_sig_strikes = data[RED][1]
      self.blue_r1_atmpd_sig_strikes = data[BLUE][0]
      self.blue_r1_landed_sig_strikes = data[BLUE][1]
    if self.index == 2:
      self.red_r2_atmpd_sig_strikes = data[RED][0]
      self.red_r2_landed_sig_strikes = data[RED][1]
      self.blue_r2_atmpd_sig_strikes = data[BLUE][0]
      self.blue_r2_landed_sig_strikes = data[BLUE][1]
    if self.index == 3:
      self.red_r3_atmpd_sig_strikes = data[RED][0]
      self.red_r3_landed_sig_strikes = data[RED][1]
      self.blue_r3_atmpd_sig_strikes = data[BLUE][0]
      self.blue_r3_landed_sig_strikes = data[BLUE][1]

  def get_sig_strikes(self):
    res = ''
    if hasattr(self, 'red_r1_atmpd_sig_strikes') and hasattr(self, 'blue_r1_atmpd_sig_strikes'):
      res += f',{self.red_r1_atmpd_sig_strikes},{self.red_r1_landed_sig_strikes},{self.blue_r1_atmpd_sig_strikes},{self.blue_r1_landed_sig_strikes}'
    else:
      res += ',---,---,---,---'
    if hasattr(self, 'red_r2_atmpd_sig_strikes') and hasattr(self, 'blue_r2_atmpd_sig_strikes'):
      res += f',{self.red_r2_atmpd_sig_strikes},{self.red_r2_landed_sig_strikes},{self.blue_r2_atmpd_sig_strikes},{self.blue_r2_landed_sig_strikes}'
    else:
      res += ',---,---,---,---'
    if hasattr(self, 'red_r3_atmpd_sig_strikes') and hasattr(self, 'blue_r3_atmpd_sig_strikes'):  
      res += f',{self.red_r3_atmpd_sig_strikes},{self.red_r3_landed_sig_strikes},{self.blue_r3_atmpd_sig_strikes},{self.blue_r3_landed_sig_strikes}'
    else:
      res += ',---,---,---,---'
    return res
  
  def __str__(self):
    return f"{self.get_kds()}{self.get_sig_strikes()}"