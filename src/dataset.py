from selenium import webdriver

from page_objects.page import EventsListPage

driver = webdriver.Chrome()
driver.get('http://ufcstats.com/statistics/events/completed?page=all')

events_page = EventsListPage(driver)
events = events_page.get_events()

for e in events[0:3]:
  events_page.get_event_details(e)