from config import BLUE, RED

class UFC_Event:
  def __init__(self, link):
    self.link = link
    self.rounds = {
      1: None,
      2: None,
      3: None
    }

  def set_name(self, name):
    self.name = name

  def set_round(self, round):
    self.rounds[round.index] = round
    
  def set_date(self, date):
    self.date = date.replace('DATE: ', '')

  def set_fighters(self, fighters):
    self.red_name = fighters[RED]
    self.blue_name = fighters[BLUE]
  
  def set_total_kds(self, kds):
    self.red_total_kds = kds[RED]
    self.blue_total_kds = kds[BLUE]

  def set_total_sig_str(self, sig_str):
    self.red_total_atmpd_sig_str = sig_str[RED][0]
    self.red_total_landed_sig_str = sig_str[RED][1]
    self.blue_total_atmpd_sig_str = sig_str[BLUE][0]
    self.blue_total_landed_sig_str = sig_str[BLUE][1]

  def set_total_sig_str_acc(self, sig_str_acc):
    self.red_total_sig_str_acc = sig_str_acc[RED].replace('%', '')
    self.blue_total_sig_str_acc = sig_str_acc[BLUE].replace('%', '')

  def set_total_str(self, total_str):
    self.red_total_atmpd_str = total_str[RED][0]
    self.red_total_landed_str = total_str[RED][1]
    self.blue_total_atmpd_str = total_str[BLUE][0]
    self.blue_total_landed_str = total_str[BLUE][1]

  def set_total_td(self, total_td):
    self.red_total_td_atmpd = total_td[RED][0]
    self.red_total_td_landed = total_td[RED][1]
    self.blue_total_td_atmpd = total_td[BLUE][0]
    self.blue_total_td_landed = total_td[BLUE][1]

  def set_total_td_acc(self, td_acc):
    self.red_total_td_acc = td_acc[RED].replace('%', '')
    self.blue_total_td_acc = td_acc[BLUE].replace('%', '')

  def set_total_sub_att(self, sub_att):
    self.red_total_sub_att = sub_att[RED]
    self.blue_total_sub_att = sub_att[BLUE]

  def set_total_rev(self, rev):
    self.red_total_rev = rev[RED]
    self.blue_total_rev = rev[BLUE]
  
  def set_total_ctrl(self, ctrl):
    self.red_total_ctrl = ctrl[RED]
    self.blue_total_ctrl = ctrl[BLUE]

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

  def get_totals(self):
    return f'{self.name},"{self.date}",{self.red_name},{self.blue_name},{self.red_total_kds},{self.blue_total_kds},{self.red_total_atmpd_sig_str},{self.red_total_landed_sig_str},{self.blue_total_atmpd_sig_str},{self.blue_total_landed_sig_str},{self.red_total_sig_str_acc},{self.blue_total_sig_str_acc},{self.red_total_atmpd_str},{self.red_total_landed_str},{self.blue_total_atmpd_str},{self.blue_total_landed_str},{self.red_total_td_atmpd},{self.red_total_td_landed},{self.blue_total_td_atmpd},{self.blue_total_td_landed},{self.blue_total_td_acc},{self.blue_total_td_acc},{self.red_total_sub_att},{self.blue_total_sub_att},{self.red_total_rev},{self.blue_total_rev},{self.red_total_ctrl},{self.blue_total_ctrl}'
  
  def get_rounds(self):
    result = ''
    for round in self.rounds.values():
      if round is not None:
        result += round.__str__()
      else:
        result += 
    return result

  def __str__(self):
    return f'{self.get_totals()}{self.get_rounds()}\n'