import jsonpath
import pytest
import requests


@pytest.fixture
def get_auth_header():
    headers_payload = {"content-type": "application/x-www-form-urlencoded",
                       "Authorization": "Basic Y2xpZW50YXBwOjEyMzQ1Ng=="}
    payload = {'username': 'liveaug29@indition.net',
               'password': 'Password!1',
               "grant_type": "password",
               "scope": "write",
               "app": "crmsales"}
    r = requests.post("https://api.inditioncrm.com/CrmSalesTeam-1.28/oauth/token",
                      headers=headers_payload,
                      params=payload,
                      verify=False)
    # l = jsonpath_ng.parse(r.json(),"$.access_token")
    l = jsonpath.jsonpath(r.json(), "$.access_token")
    # return l[0]
    yield {"Authorization": f"Bearer {l[0]}"}


def test_token(get_auth_header):
    print(get_auth_header)


def test01_get_number_of_companies(get_auth_header):
    response = requests.get("https://api.inditioncrm.com/CrmSalesTeam-1.28/picklist/countries",
                            headers=get_auth_header,
                            verify=False
                            )
    print("Total Countries found: ", len(jsonpath.jsonpath(response.json(), "$.[*].id")))


def test_01():
    response = requests.get('https://api.github.com')
    print("Status Code: ",response.status_code)


def test_02():
    # Search GitHub's repositories for requests
    response = requests.get(
        'https://api.github.com/search/repositories',
        params={'q': 'requests+language:python'},
    )

    # Inspect some attributes of the `requests` repository
    json_response = response.json()
    repository = json_response['items'][0]
    print(f'Repository name: {repository["name"]}')  # Python 3.6+
    print(f'Repository description: {repository["description"]}')  # Python 3.6+


def test_03():
    r = requests.head('https://httpbin.org/get')
    print(r)


def test_04():
    r = requests.options('https://httpbin.org/get')
    print(r.text)