from selenium import webdriver
from models.ufc_event import UFC_Event
from page_objects.page import EventPage, EventsListPage, FightDetailsPage
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://ufcstats.com/statistics/events/completed?page=all')

ufc_events_page = EventsListPage(driver)
events_links = ufc_events_page.get_events_links()

for event_link in events_links[0:3]:
  ufc_event = UFC_Event()
  
  driver.get(event_link)
  details_page: EventPage = EventPage(driver)
  ufc_event.set_name(details_page.get_title())
  ufc_event.set_date(details_page.get_date())

  fights_links = details_page.get_fights_links()
  
  for fight_link in fights_links:
    driver.get(fight_link)
    fight_page: FightDetailsPage = FightDetailsPage(driver)
    ufc_event.set_fighters(fight_page.get_fighters())
    
    print(ufc_event)
    driver.execute_script("window.history.go(-1)")
  
  driver.execute_script("window.history.go(-1)")