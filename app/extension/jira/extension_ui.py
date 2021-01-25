import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS

'''
def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

    #@print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:MyUserManagerForJira_ filterUsers")
        def sub_measure1():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/myusermanagerforjira/adminusermanager")
            page.wait_until_visible((By.ID, "userTable"))  # Wait for userTable visible
        sub_measure1()
    measure()
'''
def app_specific_action_filterUsers(webdriver, datasets):
    page = BasePage(webdriver)
    @print_timing("selenium_app_custom_action_filterUsers")
    def measure():
        #@print_timing("selenium_app_custom_action:MyUserManagerForJira_ filterUsers")
        def sub_measure1():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/myusermanagerforjira/adminusermanager")
            page.wait_until_visible((By.ID, "userTable"))  # Wait for userTable visible
            #page.wait_until_visible((By.ID, "ID_OF_YOUR_APP_SPECIFIC_UI_ELEMENT"))  # Wait for you app-specific UI element by ID selector
        sub_measure1()
    measure()

def app_specific_action_filterGroups(webdriver, datasets):
    page = BasePage(webdriver)
    @print_timing("selenium_app_custom_action_filterGroups")
    def measure():
        #@print_timing("selenium_app_custom_action:MyUserManagerForJira_ filterGroups")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/myusermanagerforjira/filterGroupsmyusermanager")
            page.wait_until_visible((By.ID, "groupTable"))  # Wait for userTable visible
            #page.wait_until_visible((By.ID, "ID_OF_YOUR_APP_SPECIFIC_UI_ELEMENT"))  # Wait for you app-specific UI element by ID selector
        sub_measure()
    measure()


def app_specific_action_mySettings(webdriver, datasets):
    page = BasePage(webdriver)
    @print_timing("selenium_app_custom_action_mySettings")
    def measure():
        #@print_timing("selenium_app_custom_action:MyUserManagerForJira_ mySettings")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/myusermanagerforjira/configuration")
            page.wait_until_visible((By.ID, "lastLoginInDays"))  # Wait for userTable visible
            #page.wait_until_visible((By.ID, "ID_OF_YOUR_APP_SPECIFIC_UI_ELEMENT"))  # Wait for you app-specific UI element by ID selector
        sub_measure()
    measure()
