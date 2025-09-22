from selenium import webdriver
from models.ufc_event import UFC_Event
from page_objects.page import EventPage, EventsListPage
from csv_writer import CsvWriter
from config import HEADERS, ENDPOINT
from page_objects.fight_details_page import FightDetailsPage

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
    ufc_event.set_total_kds(fight_page.get_total_kds())
    ufc_event.set_total_sig_str(fight_page.get_total_sig_str())
    ufc_event.set_total_sig_str_acc(fight_page.get_total_sig_str_acc())
    ufc_event.set_total_str(fight_page.get_total_str())
    ufc_event.set_total_td(fight_page.get_total_td())
    ufc_event.set_total_td_acc(fight_page.get_total_td_acc())
    ufc_event.set_total_sub_att(fight_page.get_total_sub_att())
    ufc_event.set_total_rev(fight_page.get_total_rev())
    ufc_event.set_total_ctrl(fight_page.get_total_ctrl())

    csv_writer.write_row(ufc_event.__str__())
    driver.execute_script("window.history.go(-1)")
  
  driver.execute_script("window.history.go(-1)")