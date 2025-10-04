from selenium import webdriver
from models.ufc_event import UFC_Event
from page_objects.page import EventPage, EventsListPage
from csv_writer import CsvWriter
from config import HEADERS, ENDPOINT, ROUNDS_SIG_STRIKES_HEADERS
from page_objects.fight_details_page import FightDetailsPage
from models.round import Round

csv_writer = CsvWriter()
csv_writer.set_headers(HEADERS + ROUNDS_SIG_STRIKES_HEADERS)

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
    ufc_event.set_totals(*fight_page.get_totals())

    
    for round_section in fight_page.get_striking_rounds():
      round_section.open()
      round = Round(round_section.index)
      round.set_kds(round_section.get_kds())
      round.set_sig_strikes(round_section.get_sig_strikes())

      ufc_event.set_round(round)

    csv_writer.write_row(ufc_event.__str__())
    driver.execute_script("window.history.go(-1)")
  
  driver.execute_script("window.history.go(-1)")