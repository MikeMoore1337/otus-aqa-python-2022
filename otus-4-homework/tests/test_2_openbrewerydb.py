import pytest
import requests
from jsonschema import validate


def test_ststus_code(url_param="https://api.openbrewerydb.org"):
    """Checking API status"""
    response = requests.get(url_param)
    assert response.status_code == 200


def test_search(url_param="https://api.openbrewerydb.org/breweries/search?query="):
    """Checking search"""
    response = requests.get(f"{url_param}monkey")
    assert response.status_code == 200


def test_schema_brewereis(url_param="https://api.openbrewerydb.org/breweries"):
    response = requests.get(url_param)
    assert response.status_code == 200
    resp = response.json()
    schema = {
        "type": "array",
        "items": {
            "type": "object"
        }
    }
    validate(resp, schema)


@pytest.mark.parametrize("city", {'los_angeles', 'new_york', 'berlin', 'london', 'moscow'})
def test_filter_breweries_by_city(city, url_param="https://api.openbrewerydb.org/breweries?by_city="):
    """Filter breweries by city"""
    link = f"{url_param}/{city}/"
    response = requests.get(link)
    assert response.status_code == 200


@pytest.mark.parametrize(
    "url_param, expected",
    [("https://api.openbrewerydb.org/breweries?by_city=los_angeles", 20),
     ("https://api.openbrewerydb.org/breweries?by_city=moscow", 4),
     ("https://api.openbrewerydb.org/breweries?by_city=london", 7)]
)
def test_assert_count(url_param, expected):
    """Checking count breweries by city"""
    response = requests.get(url_param, expected)
    json_dict = response.json()
    count_brewery = len(json_dict)
    assert count_brewery == expected
