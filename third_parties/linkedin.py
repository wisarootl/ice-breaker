import os

import requests


def scrape_linkedin_profile(linked_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from LinkedIn profile
    """
    api_endpoint = "http://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f"Bearer {os.environ.get('PROXYCURL_API_KEY')}"}

    response = requests.get(
        api_endpoint, params={"url": linked_profile_url}, headers=header_dic
    )

    if response.status_code != "200":
        response = requests.get(
            "https://gist.githubusercontent.com/emarco177/"
            "0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad"
            "52ba2a968bad9eb45128665/eden-marco.json"
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", None) and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
