from selenium.webdriver.common.by import By
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS

from selenium_ui.base_page import BasePage
import random


def app_specific_action(webdriver, datasets):
    sprint_page = BasePage(webdriver)

    sprint = random.choice(datasets["sprints"])
    sprint_id = sprint[0]
    board_id = sprint[1]

    @print_timing("selenium_view_sprint")
    def measure():
        webdriver.get(f"{JIRA_SETTINGS.server_url}/secure/RapidBoard.jspa?rapidView={board_id}&sprint={sprint_id}")
        sprint_page.wait_until_present((By.CSS_SELECTOR, "a[data-item-id='all']"))
    measure()

