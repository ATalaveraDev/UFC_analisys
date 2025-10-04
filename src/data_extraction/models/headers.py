class Headers:
  def __init__(self):
    self.total_headers = [
      'event_name',
      'event_date',
      'red_name',
      'blue_name',
      'red_total_kds',
      'blue_total_kds',
      'red_total_atmpd_sig_str',
      'red_total_landed_sig_str',
      'blue_total_atmpd_sig_str',
      'blue_total_landed_sig_str',
      'red_total_sig_str_acc',
      'blue_total_sig_str_acc',
      'red_total_atmpd_str',
      'red_total_landed_str',
      'blue_total_atmpd_str',
      'blue_total_landed_str',
      'red_total_td_atmpd',
      'red_total_td_landed',
      'blue_total_td_atmpd',
      'blue_total_td_landed',
      'red_total_td_acc',
      'blue_total_td_acc',
      'red_total_sub_att',
      'blue_total_sub_att',
      'red_total_rev',
      'blue_total_rev',
      'red_total_ctrl',
      'blue_total_ctrl'
    ]
    self.rounds_headers = self.build_rounds_headers()

  def build_rounds_headers(self):
    result = []
    for i in range(1, 6):
      result += [
        f"red_r{i}_kds",
        f"blue_r{i}_kds",
        f"red_r{i}_atmpd_sig_strikes",
        f"red_r{i}_landed_sig_strikes",
        f"blue_r{i}_atmpd_sig_strikes",
        f"blue_r{i}_landed_sig_strike"
      ]
    return result
  
  def get_all(self):
    return self.total_headers + self.rounds_headers