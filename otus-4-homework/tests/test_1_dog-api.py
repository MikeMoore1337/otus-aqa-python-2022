import pytest
import requests


def test_status(url_param="https://dog.ceo/api/breed/terrier/american/images/random"):
    """Check the status in a message success"""
    response = requests.get(url_param)
    status = response.json()["status"]
    assert status == "success"


def test_list_count_of_breeds(url_param='https://dog.ceo/api/breeds/list/all'):
    """Counting the breeds"""
    response = requests.get(url_param)
    dict_breeds = response.json()['message']
    assert len(dict_breeds) == 96


@pytest.mark.parametrize(
    "test_breeds, expected",
    [("australian", ["shepherd"]),
     ("buhund", ["norwegian"]),
     ("coonhound", []),
     ("mastiff", ["bull", "english", "tibetan"])]
)
def test_get_breed(test_breeds, expected, url_param="https://dog.ceo/api/breeds/list/all"):
    """Checking the breed"""
    response = requests.get(url_param)
    dict_breeds = response.json()["message"]
    assert dict_breeds.get(test_breeds) == expected


def test_add_breed(url_param="https://dog.ceo/api/breeds/list/all"):
    """Checking the breed after adding"""
    response = requests.get(url_param)
    dict_breeds = response.json()["message"]
    dict_breeds["retriever"] = ["golden"]
    assert dict_breeds.get("retriever") == ["golden"]


@pytest.mark.parametrize("number", [1, 7, 25, 42, 50, pytest.param(51, marks=pytest.mark.xfail)])
def test_numbers_image(number, url_param="https://dog.ceo/api", get_image="breeds/image/random"):
    """Checking the amount of a photo"""
    dogs_image = f"{url_param}/{get_image}/{number}"
    res_dogs = requests.get(dogs_image)
    assert len(res_dogs.json().get("message")) == number
