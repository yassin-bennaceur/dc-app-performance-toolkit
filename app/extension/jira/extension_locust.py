import re
from locustio.common_utils import init_logger, jira_measure, raise_if_login_failed, RESOURCE_HEADERS, ADMIN_HEADERS

logger = init_logger(app_type='jira')

@jira_measure("locust_custom_action_endpoint_getConfig")
def endpoint_getConfig(locust):
    #raise_if_login_failed(locust)
    #r = locust.get('/app/get_endpoint', catch_response=True)  # call app-specific GET endpoint
    #r = locust.get('/rest/myUserManagerResource/1.0/MyUserManagementConfig/getConfig', headers=RESOURCE_HEADERS,auth=('admin', 'admin'), catch_response=True)  # call app-specific GET endpoint
    r = locust.get('/rest/myUserManagerResource/1.0/MyUserManagementConfig/getConfig', headers=RESOURCE_HEADERS, catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content
    if not ('lastLoginInDays' in content):
        logger.error(f'lastLoginInDays not found in Content: {content}')
    assert 'lastLoginInDays' in content, 'MyUserManagerForJira_getConfig is finished sucessfully'

@jira_measure("locust_custom_action_endpoint_getUsers")
def endpoint_getUsers(locust):
    #raise_if_login_failed(locust)
    r = locust.get('/rest/myUserManagerResource/1.0/MyUserManagement/getUsers', 
                    params={'lastLoginInDays': '90',
                            'startAt':'0',
                            'maxResult':'100',
                            'searchInUserInfo':'',
                            'searchNotInUserInfo':'',
                            'searchInGroups':'',
                            'searchNotInGroups':'',
                            'searchInDirectories':'',
                            'searchInStatus':''},
                    #headers=RESOURCE_HEADERS, auth=('admin', 'admin'), catch_response=True)  # call app-specific GET endpoint
                    headers=RESOURCE_HEADERS, catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content
    #logger.locust_info(f'======> {content}')
    if not ('ListUserDBToShow' in content):
        logger.error(f'ListUserDBToShow not found in Content: {content}')
    assert 'ListUserDBToShow' in content, 'MyUserManagerForJira_getUsers is finished sucessfully'


@jira_measure("locust_custom_action_endpoint_getMyGroups")
def endpoint_getMyGroups(locust):
    #raise_if_login_failed(locust)
    r = locust.get('/rest/myUserManagerResource/1.0/MyGroupManagement/getMyGroups', 
                    params={'startAt':'0',
                            'maxResult':'100',
                            'groupNameContains':'',
                            'groupNameStartsWith':'',
                            'groupNameEndsWith':'',
                            'groupNameDoesNotContain':'',
                            'groupNameDoesNotStartWith':'',
                            'groupNameDoesNotEndWith':'',
                            'groupContainsNoActiveUsers':'false',
                            'groupContainsDeactivatedUsers':'false'},
                    #headers=RESOURCE_HEADERS, auth=('admin', 'admin'), catch_response=True)  # call app-specific GET endpoint
                    headers=RESOURCE_HEADERS, catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content
    #logger.locust_info(f'======> {content}')
    if not ('ListGroupToShow' in content):
        logger.error(f'ListGroupToShow not found in Content: {content}')
    assert 'ListGroupToShow' in content, 'MyUserManagerForJira_getMyGroups is finished sucessfully'

def app_specific_action(locust):
    endpoint_getConfig(locust)  
    endpoint_getUsers(locust)
    endpoint_getMyGroups(locust)
    '''
    token_pattern_example = '"token":"(.+?)"'
    id_pattern_example = '"id":"(.+?)"'
    token = re.findall(token_pattern_example, content)  # get TOKEN from response using regexp
    id = re.findall(id_pattern_example, content)    # get ID from response using regexp

    logger.locust_info(f'token: {token}, id: {id}')  # log info for debug when verbose is true in jira.yml file
    if 'assertion string' not in content:
        logger.error(f"'assertion string' was not found in {content}")
    assert 'assertion string' in content  # assert specific string in response content

    body = {"id": id, "token": token}  # include parsed variables to POST request body
    headers = {'content-type': 'application/json'}
    r = locust.post('/app/post_endpoint', body, headers, catch_response=True)  # call app-specific POST endpoint
    content = r.content.decode('utf-8')
    if 'assertion string after successful POST request' not in content:
        logger.error(f"'assertion string after successful POST request' was not found in {content}")
    assert 'assertion string after successful POST request' in content  # assertion after POST request
    '''
