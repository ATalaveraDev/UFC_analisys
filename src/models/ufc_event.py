class UFC_Event:
  def __init__(self, name, date):
    self.name = name
    self.date = date.replace('DATE: ', '')

  def __str__(self):
    return f'"{self.name}", "{self.date}"'