from selenium.webdriver.common.by import By

class EventsListPageLocators(object):
  ROWS = (By.CSS_SELECTOR, '.b-statistics__table-events tr.b-statistics__table-row td i a')
  EVENT_LINK = (By.CSS_SELECTOR, 'i.b-statistics__table-content a')

class EventPageLocators(object):
  TITLE = (By.CSS_SELECTOR, '.b-content__title-highlight')
  DATE = (By.CSS_SELECTOR, '.b-list__info-box ul > li')
  FIGHTS = (By.CSS_SELECTOR, '.b-fight-details__table-body tr')

class FightDetailsPageLocator(object):
  FIGHTERS = (By.CSS_SELECTOR, '.b-fight-details__person')
  FIGHTER_NAME = (By.CSS_SELECTOR, '.b-fight-details__person-link')
  TABLE_SECTION = (By.CSS_SELECTOR, 'section.b-fight-details__section.js-fight-section')
  TOTALS_COLS = (By.CSS_SELECTOR, 'td.b-fight-details__table-col')
  COL = (By.CSS_SELECTOR, 'td.b-fight-details__table-col')
  COL_CONTENTS = (By.CSS_SELECTOR, 'p')
  ROUND_HEADER = (By.CSS_SELECTOR, 'thead.b-fight-details__table-row_type_head th')
  ROUND_BODY = (By.CSS_SELECTOR, 'tbody')
  ROUND_ROW = (By.CSS_SELECTOR, 'tr')