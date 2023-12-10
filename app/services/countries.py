import requests
from loguru import logger
from cachetools import TTLCache

cache = TTLCache(maxsize=1, ttl=3600)


def fetch_countries_data():
    response = requests.get("https://restcountries.com/v3/all")
    if response.status_code == 200:
        return response.json()

    else:
        return []


def get_countries():
    if "countries_data" in cache:
        countries_data = cache["countries_data"]
        logger.info('Countries From Cache')
    else:
        countries_data = fetch_countries_data()
        cache["countries_data"] = countries_data
        logger.info('Countries From Request')

    countries = []

    for country_data in countries_data:
        if country_data['name']['common'] and country_data["idd"]:
            code = country_data["idd"]["root"] + \
                country_data['idd']['suffixes'][0]
            capital = country_data.get("capital")
            # logger.info(capital)
            country = {
                "name": country_data['name']['common'],
                "zip_code": code,
                "flag": country_data['flags'][1],
                "short": country_data['altSpellings'][0],
                'region': country_data['region'],
                "capital": capital[0] if capital else '',
                "population": country_data['population'],
                "location": country_data['latlng'],
                "sub_region": country_data.get("subregion") if country_data.get("subregion") else '',
                "languages": list(country_data.get("languages").values()) if country_data.get("languages") else [],
                "currencies": list(country_data.get("currencies").values()) if  country_data.get("currencies") else {},
                "borders": country_data.get("borders") if  country_data.get("borders") else [],
                "tld": country_data.get("tld"),
                "nativeName": list(country_data.get("name").get("nativeName").values()),
                "map": country_data.get("maps"),
                "cca3": country_data.get("cca3"),
                
            }
            countries.append(country)
    sorted_countries = sorted(countries, key=lambda x: x["name"])

    return sorted_countries
