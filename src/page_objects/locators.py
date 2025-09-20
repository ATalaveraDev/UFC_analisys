from selenium.webdriver.common.by import By

class EventsListPageLocators(object):
  ROWS = (By.CSS_SELECTOR, '.b-statistics__table-events tr.b-statistics__table-row')
  EVENT_LINK = (By.CSS_SELECTOR, 'i.b-statistics__table-content a')

class EventPageLocators(object):
  TITLE = (By.CSS_SELECTOR, '.b-content__title-highlight')
  DATE = (By.CSS_SELECTOR, '.b-list__info-box ul > li')
