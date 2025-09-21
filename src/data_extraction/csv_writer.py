import csv

class CsvWriter:
  def __init__(self):
    self.file_to_write = open('data/ufc_data.csv', mode='w', newline='')
    self.writer = csv.writer(self.file_to_write, delimiter=',')
    
  def set_headers(self, headers):
    self.writer.writerow(headers)
    self.file_to_write.close()

  def write_row(self, row):
    with open('data/ufc_data.csv', mode='a', newline='') as fd:
      fd.write(row)