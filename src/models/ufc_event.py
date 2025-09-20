class UFC_Event:
  def set_name(self, name):
    self.name = name
    
  def set_date(self, date):
    self.date = date.replace('DATE: ', '')

  def set_fighters(self, fighters):
    self.red_name = fighters['red']
    self.blue_name = fighters['blue']

  def __str__(self):
    return f'"{self.name}","{self.date}","{self.red_name}","{self.blue_name}"'