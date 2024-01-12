import pytest
import requests
from jsonschema import validate

POST_ID = 100
COMMENT_ID = 500


def test_count_id(url_param='https://jsonplaceholder.typicode.com/photos', expected=5000):
    """Checking count of photos"""
    response = requests.get(url_param)
    json_dict = response.json()
    fact_list = []
    for element in json_dict:
        fact_list.append(element['id'])
    assert len(fact_list) == expected


def test_delete_post(url_param="https://jsonplaceholder.typicode.com"):
    """Checking delete post"""
    response = requests.delete(f"{url_param}/posts/1")
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_create_post(url_param="https://jsonplaceholder.typicode.com"):
    """Checking creating a post"""
    loading = {"title": "lorem ipsum dolor sit amet", "body": "consectetur adipiscing elit", "userId": 1}
    response = requests.post(f"{url_param}/posts", json=loading)
    json_resp = response.json()
    assert json_resp["id"] == POST_ID + 1
    assert json_resp["userId"] == loading["userId"]
    assert json_resp["title"] == loading["title"]
    assert json_resp["body"] == loading["body"]


@pytest.mark.parametrize("index", range(100))
def test_json_schema(index, url_param="https://jsonplaceholder.typicode.com/posts"):
    """Checking JSON Schema"""
    response = requests.get(url_param)
    schema = {
        "type": "object",
        "properties":
            {
                "userId": {"type": "number"},
                "id": {"type": "number"},
                "title": {"type": "string"},
                "body": {"type": "string"},
            },
        "required": ["userId", "id", "title", "body"]
    }
    validate(instance=response.json()[index], schema=schema)


@pytest.mark.parametrize("comment_id", [1, COMMENT_ID])
def test_check_id(comment_id, url_param="https://jsonplaceholder.typicode.com"):
    """Checking comments by id"""
    response = requests.get(f"{url_param}/comments/{comment_id}")
    assert response.json()["id"] == comment_id
