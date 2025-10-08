from selenium import webdriver
from models.ufc_event import UFC_Event
from page_objects.page import EventPage, EventsListPage
from csv_writer import CsvWriter
from config import ENDPOINT
from page_objects.fight_details_page import FightDetailsPage
from models.round import Round
from models.headers import Headers

csv_writer = CsvWriter()

headers = Headers()
csv_writer.set_headers(headers.get_all())

driver = webdriver.Chrome()
driver.get(ENDPOINT)

ufc_events_page = EventsListPage(driver)
events_links = ufc_events_page.get_events_links()
for event_link in events_links[0:1]:
  ufc_event = UFC_Event(event_link)
  
  driver.get(ufc_event.link)
  details_page: EventPage = EventPage(driver)
  ufc_event.set_name(details_page.get_title())
  ufc_event.set_date(details_page.get_date())

  fights_links = details_page.get_fights_links()
  
  for fight_link in fights_links:
    driver.get(fight_link)
    fight_page: FightDetailsPage = FightDetailsPage(driver)
    ufc_event.set_fighters(fight_page.get_fighters())
    ufc_event.set_totals(*fight_page.get_totals())

    
    for index in range(5):
      round = Round(index)
      
      round_section = fight_page.get_striking_rounds(index)

      if round_section:
        round_section.open()
        round.set_stats(*round_section.get_stats())

      ufc_event.set_round(round)

    csv_writer.write_row(ufc_event.__str__())
    driver.execute_script("window.history.go(-1)")
  
  driver.execute_script("window.history.go(-1)")