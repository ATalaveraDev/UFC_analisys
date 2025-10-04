class UFC_Event:
  RED = 'red'
  BLUE = 'blue'

  def __init__(self, link):
    self.link = link

  def set_name(self, name):
    self.name = name
    
  def set_date(self, date):
    self.date = date.replace('DATE: ', '')

  def set_fighters(self, fighters):
    self.red_name = fighters[self.RED]
    self.blue_name = fighters[self.BLUE]
  
  def set_total_kds(self, kds):
    self.red_total_kds = kds[self.RED]
    self.blue_total_kds = kds[self.BLUE]

  def set_total_sig_str(self, sig_str):
    self.red_total_atmpd_sig_str = sig_str[self.RED][0]
    self.red_total_landed_sig_str = sig_str[self.RED][1]
    self.blue_total_atmpd_sig_str = sig_str[self.BLUE][0]
    self.blue_total_landed_sig_str = sig_str[self.BLUE][1]

  def set_total_sig_str_acc(self, sig_str_acc):
    self.red_total_sig_str_acc = sig_str_acc[self.RED].replace('%', '')
    self.blue_total_sig_str_acc = sig_str_acc[self.BLUE].replace('%', '')

  def set_total_str(self, total_str):
    self.red_total_atmpd_str = total_str[self.RED][0]
    self.red_total_landed_str = total_str[self.RED][1]
    self.blue_total_atmpd_str = total_str[self.BLUE][0]
    self.blue_total_landed_str = total_str[self.BLUE][1]

  def set_total_td(self, total_td):
    self.red_total_td_atmpd = total_td[self.RED][0]
    self.red_total_td_landed = total_td[self.RED][1]
    self.blue_total_td_atmpd = total_td[self.BLUE][0]
    self.blue_total_td_landed = total_td[self.BLUE][1]

  def set_total_td_acc(self, td_acc):
    self.red_total_td_acc = td_acc[self.RED].replace('%', '')
    self.blue_total_td_acc = td_acc[self.BLUE].replace('%', '')

  def set_total_sub_att(self, sub_att):
    self.red_total_sub_att = sub_att[self.RED]
    self.blue_total_sub_att = sub_att[self.BLUE]

  def set_total_rev(self, rev):
    self.red_total_rev = rev[self.RED]
    self.blue_total_rev = rev[self.BLUE]
  
  def set_total_ctrl(self, ctrl):
    self.red_total_ctrl = ctrl[self.RED]
    self.blue_total_ctrl = ctrl[self.BLUE]

  def set_totals(self, kds, sig_str, sig_str_acc, strikes, tds, tds_acc, sub_att, rev, ctrl):
    self.set_total_kds(kds)
    self.set_total_sig_str(sig_str)
    self.set_total_sig_str_acc(sig_str_acc)
    self.set_total_str(strikes)
    self.set_total_td(tds)
    self.set_total_td_acc(tds_acc)
    self.set_total_sub_att(sub_att)
    self.set_total_rev(rev)
    self.set_total_ctrl(ctrl)

  def set_round_kds(self, round, kds):
    if round == 1:
      self.red_r1_kds = kds[self.RED]
      self.blue_r1_kds = kds[self.BLUE]
    if round == 2:
      self.red_r2_kds = kds[self.RED]
      self.blue_r2_kds = kds[self.BLUE]
    if round == 3:
      self.red_r3_kds = kds[self.RED]
      self.blue_r3_kds = kds[self.BLUE]
  
  def get_rounds_kds(self):
    res = ''
    if hasattr(self, 'red_r1_kds') and hasattr(self, 'blue_r1_kds'):
      res += f'{self.red_r1_kds},{self.blue_r1_kds}'
    else:
      res += 'null,null'
    if hasattr(self, 'red_r2_kds') and hasattr(self, 'blue_r2_kds'):
      res += f',{self.red_r2_kds},{self.blue_r2_kds}'
    else:
      res += 'null,null'
    if hasattr(self, 'red_r3_kds') and hasattr(self, 'blue_r3_kds'):  
      res += f',{self.red_r3_kds},{self.blue_r3_kds}'
    else:
      res += 'null,null'
    return res

  def get_totals(self):
    return f'{self.name},"{self.date}",{self.red_name},{self.blue_name},{self.red_total_kds},{self.blue_total_kds},{self.red_total_atmpd_sig_str},{self.red_total_landed_sig_str},{self.blue_total_atmpd_sig_str},{self.blue_total_landed_sig_str},{self.red_total_sig_str_acc},{self.blue_total_sig_str_acc},{self.red_total_atmpd_str},{self.red_total_landed_str},{self.blue_total_atmpd_str},{self.blue_total_landed_str},{self.red_total_td_atmpd},{self.red_total_td_landed},{self.blue_total_td_atmpd},{self.blue_total_td_landed},{self.blue_total_td_acc},{self.blue_total_td_acc},{self.red_total_sub_att},{self.blue_total_sub_att},{self.red_total_rev},{self.blue_total_rev},{self.red_total_ctrl},{self.blue_total_ctrl}'

  def __str__(self):
    return f'{self.get_totals()},{self.get_rounds_kds()}\n'