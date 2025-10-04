RED = 'red'
BLUE = 'blue'

HEADERS = [
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
  'blue_total_ctrl',
  'red_r1_kds',
  'blue_r1_kds',
  'red_r2_kds',
  'blue_r2_kds',
  'red_r3_kds',
  'blue_r3_kds'
]

ROUNDS_SIG_STRIKES_HEADERS = [
  'red_r1_atmpd_sig_strikes',
  'red_r1_landed?sig_strikes',
  'blue_r1_atmpd_sig_strikes',
  'blue_r1_landed_sig_strikes',
  'red_r2_atmpd_sig_strikes',
  'red_r2_landed_sig_strikes',
  'blue_r2_atmpd_sig_strikes',
  'blue_r2_landed_sig_strikes',
  'red_r3_atmpd_sig_strikes',
  'red_r3_landed_sig_strikes',
  'blue_r3_atmpd_sig_strikes',
  'blue_r3_landed_sig_strikes'
]

ENDPOINT = 'http://ufcstats.com/statistics/events/completed?page=all'