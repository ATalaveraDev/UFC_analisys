from selenium import webdriver
from models.ufc_event import UFC_Event
from page_objects.page import EventPage, EventsListPage
from csv_writer import CsvWriter
from config import HEADERS, ENDPOINT
from page_objects.fight_details_page import FightDetailsPage
from page_objects.round import Round

csv_writer = CsvWriter()
csv_writer.set_headers(HEADERS)

driver = webdriver.Chrome()
driver.get(ENDPOINT)

ufc_events_page = EventsListPage(driver)
events_links = ufc_events_page.get_events_links()
for event_link in events_links[0:3]:
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
    ufc_event.set_totals(fight_page.get_totals())

    striking_rounds = fight_page.get_striking_rounds()

    if len(striking_rounds):
      for i in range(len(striking_rounds)):
        round = Round(driver, i+1)
        round.section.click()
        ufc_event.set_round_kds(i+1, round.get_kds())

    csv_writer.write_row(ufc_event.__str__())
    driver.execute_script("window.history.go(-1)")
  
  driver.execute_script("window.history.go(-1)")