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
    self.red_sig_str_acc = "---"
    self.blue_sig_str_acc = "---" 
    self.red_atmpd_str = "---"
    self.red_landed_str = "---"
    self.blue_atmpd_str = "---"
    self.blue_landed_str = "---"  
    self.red_td_atmpd = "---"
    self.red_td_landed = "---"
    self.blue_td_atmpd = "---"
    self.blue_td_landed = "---"
    self.red_td_acc = "---"
    self.blue_td_acc = "---"
    self.red_sub_att = "---"
    self.blue_sub_att = "---"
    self.red_rev = "---"
    self.blue_rev = "---"
    self.red_ctrl = "---"
    self.blue_ctrl = "---"

  def get_sig_strikes(self):
    return f",{self.red_atmpd_sig_strikes},{self.red_landed_sig_strikes},{self.blue_atmpd_sig_strikes},{self.blue_landed_sig_strikes}"
  
  def get_sig_strikes_acc(self):
    return f",{self.red_sig_str_acc},{self.blue_sig_str_acc}"
  
  def get_kds(self):
    return f",{self.red_kds},{self.blue_kds}"

  def get_atmpd_landed_str(self):
    return f",{self.red_atmpd_str},{self.red_landed_str},{self.blue_atmpd_str},{self.blue_landed_str}"

  def get_atmpd_landed_td(self):
    return f",{self.red_td_atmpd},{self.red_td_landed},{self.blue_td_atmpd},{self.blue_td_landed}"

  def get_td_acc(self):
    return f",{self.red_td_acc},{self.blue_td_acc}"

  def get_sub_att(self):
    return f",{self.red_sub_att},{self.blue_sub_att}"

  def get_rev(self):
    return f",{self.red_rev},{self.blue_rev}"

  def get_ctrl(self):
    return f",{self.red_ctrl},{self.blue_ctrl}"
  
  def set_sig_strikes(self, data):
    self.red_atmpd_sig_strikes = data[RED][0]
    self.red_landed_sig_strikes = data[RED][1]
    self.blue_atmpd_sig_strikes = data[BLUE][0]
    self.blue_landed_sig_strikes = data[BLUE][1]

  def set_sig_str_acc(self, sig_str_acc):
    self.red_sig_str_acc = sig_str_acc[RED].replace('%', '')
    self.blue_sig_str_acc = sig_str_acc[BLUE].replace('%', '')

  def set_kds(self, data):
    self.red_kds = data[RED]
    self.blue_kds = data[BLUE]

  def set_str(self, str):
    self.red_atmpd_str = str[RED][0]
    self.red_landed_str = str[RED][1]
    self.blue_atmpd_str = str[BLUE][0]
    self.blue_landed_str = str[BLUE][1]

  def set_td(self, td):
    self.red_td_atmpd = td[RED][0]
    self.red_td_landed = td[RED][1]
    self.blue_td_atmpd = td[BLUE][0]
    self.blue_td_landed = td[BLUE][1]

  def set_td_acc(self, td_acc):
    self.red_td_acc = td_acc[RED].replace('%', '')
    self.blue_td_acc = td_acc[BLUE].replace('%', '')

  def set_sub_att(self, sub_att):
    self.red_sub_att = sub_att[RED]
    self.blue_sub_att = sub_att[BLUE]

  def set_rev(self, rev):
    self.red_rev = rev[RED]
    self.blue_rev = rev[BLUE]
  
  def set_ctrl(self, ctrl):
    self.red_ctrl = ctrl[RED]
    self.blue_ctrl = ctrl[BLUE]

  def set_stats(self, kds, sig_str, sig_str_acc, strikes, tds, tds_acc, sub_att, rev, ctrl):
    self.set_kds(kds)
    self.set_sig_strikes(sig_str)
    self.set_sig_str_acc(sig_str_acc)
    self.set_str(strikes)
    self.set_td(tds)
    self.set_td_acc(tds_acc)
    self.set_sub_att(sub_att)
    self.set_rev(rev)
    self.set_ctrl(ctrl)
    
  def __str__(self):
    return f"{self.get_kds()}{self.get_sig_strikes()}{self.get_sig_strikes_acc()}{self.get_atmpd_landed_str()}{self.get_atmpd_landed_td()}{self.get_td_acc()}{self.get_sub_att()}{self.get_rev()}{self.get_ctrl()}"