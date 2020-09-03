from selenium.webdriver.common.by import By
import random
from selenium_ui.conftest import print_timing
from util.conf import BITBUCKET_SETTINGS

from selenium_ui.base_page import BasePage
from selenium_ui.bitbucket.pages.pages import PopupManager, RepoNavigationPanel


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    repo = random.choice(datasets["repos_app"])
    project_key = repo[1]
    repo_slug = repo[0]

    @print_timing("selenium_view_archived_repo")
    def measure():
        page.go_to_url(f"{BITBUCKET_SETTINGS.server_url}/projects/{project_key}/repos/{repo_slug}/browse")
        nav_panel = RepoNavigationPanel(webdriver)
        nav_panel.wait_for_page_loaded()
        PopupManager(webdriver).dismiss_default_popup()
    measure()
