from urllib.parse import urljoin

import requests
import jsonpath

BASE_URL = "https://api-dev.inditioncrm.com:8443/CrmSalesTeam-1.29"

def test01_get_list_of_companies():
    headers_payload = {"content-type": "application/x-www-form-urlencoded", "Authorization": "Basic Y2xpZW50YXBwOjEyMzQ1Ng=="}
    payload = {'username': 'liveaug30@indition.net',
               'password': 'Password!1',
               "grant_type": "password",
               "scope": "write",
               "app": "crmsales"}
    print(urljoin(BASE_URL, "/oauth/token"))
    r = requests.post(urljoin(BASE_URL, "/oauth/token"),
                      headers=headers_payload,
                      params=payload)


    print("the response in json format: \n", r.json())
    print("Fetching Access Token: ")
    print(jsonpath.jsonpath(r.json(), "$.access_token"))

    # response = requests.get("https://api-dev.inditioncrm.com:8443/CrmSalesTeam-1.29/oauth/token",
    #                         headers={"content-type":"application/x-www-form-urlencoded",
    #                                  "Authorization":"Basic Y2xpZW50YXBwOjEyMzQ1Ng==",
    #
    #                                  })
    # print(response.text)


    # Assert.assertEquals(response.getStatusCode(), 200);
    # String
    # totalRecords = JsonPath.read(response.asString(), "$.totalRecords").toString();
    # response = Utility.GET_Response("/company/getcompanies/v2?pageSize=" + totalRecords);
    # companyIDs = JsonPath.read(response.asString(), "$.data[*].id");
    # System.out.println("---------------------------------------------------------------------");

