from urllib.parse import urljoin

import requests
import jsonpath


def get_access_token():
    headers_payload = {"content-type": "application/x-www-form-urlencoded",
                       "Authorization": "Basic Y2xpZW50YXBwOjEyMzQ1Ng=="}
    payload = {'username': 'liveaug29@indition.net',
               'password': 'Password!1',
               "grant_type": "password",
               "scope": "write",
               "app": "crmsales"}
    r = requests.post(("https://api.inditioncrm.com/CrmSalesTeam-1.28/oauth/token"),
                      headers=headers_payload,
                      params=payload,
                      verify=False)
    l = jsonpath.jsonpath(r.json(), "$.access_token")
    return l[0]


def test01_get_number_of_companies():
    header = {"Authorization":f"Bearer {get_access_token()}"}
    print(header)
    response = requests.get(("https://api.inditioncrm.com/CrmSalesTeam-1.28/picklist/countries"),
                            headers=header,
                            verify=False
                            )
    print("Total Countries found: ",len(jsonpath.jsonpath(response.json(),"$.[*].id")))
