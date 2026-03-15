import pytest
from ApiClient import ApiClient
import requests

BASE_URL = "https://ru.yougile.com"

users = [
    {
        "id": "809400f7-b024-4dbc-9408-fbd097690e78",
        "email": "prikhodko.ol14@gmail.com",
        "isAdmin": True,
        "realName": "Ольга"
    },
    {
        "id": "f3d388f7-4c11-4903-9d08-10e09bfa57b7",
        "email": "example.user@yandex.ru",
        "isAdmin": False,
        "realName": "example.user@yandex.ru",
    },
    {
        "id": "0f788dd8-d21f-4de9-97c7-7549e548571a",
        "email": "user22@yandex.ru",
        "isAdmin": False,
        "realName": "user22@yandex.ru",
    }
]

@pytest.fixture
def api_client():
    client = ApiClient(BASE_URL, LOGIN, PASSWORD)
    auth_data = client.auth_data()
    api_key = client.get_api_key(auth_data)
    return client, api_key

def test_create_project_positive(api_client):
    client, api_key = api_client
    users = {
        "f3d388f7-4c11-4903-9d08-10e09bfa57b7": "worker",
        "0f788dd8-d21f-4de9-97c7-7549e548571a": "observer"
    }
    response = client.create_project(api_key, "ОлолоТур", users)
    assert response.status_code == 201
    response_data = response.json()
    assert 'id' in response_data

def test_create_project_negative(api_client):
    client, api_key = api_client
    users = {"ppldifun1123": "worker"}
    response = client.create_project(api_key, "", users)

    response_json = response.json()

    expected_response = {
    "statusCode": 400,
    "message": [
    "title should not be empty",
    "title must be a string"
    ],
    "error": "Bad Request"
    }

    assert response_json == expected_response, (
    f"Expected response {expected_response}, but got {response_json}"
    )

def test_edit_project_positive(api_client):
    client, api_key = api_client
    users = {
        "0f788dd8-d21f-4de9-97c7-7549e548571a": "worker",
    }
    project_response = client.create_project(api_key, "Помянем", users)
    assert project_response.status_code == 201

    json_response = project_response.json()
    project_id = json_response.get('id')
    assert project_id is not None

    new_users = {
        "f3d388f7-4c11-4903-9d08-10e09bfa57b7": "worker", 
        "0f788dd8-d21f-4de9-97c7-7549e548571a": "worker"
    }
    response = client.edit_project(api_key, project_id, "Мы живы!", new_users, deleted=True)
    assert response.status_code == 200
    response_json = response.json()
    assert 'id' in response.json
    assert response['title'] == "Мы живы!"
    assert response.get('deleted') is True

def test_edit_negative(api_client):
    client, api_key = api_client
    project_id = "id0dfrkmsbfu"
    users = {
        "4902b994-b806-4af4-acec-018ea5ea6468" : "worker",
        "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018" : "530056b7-e628-4128-bcf0-909a63e9781c"
        }
    response = client.edit_project(api_key, project_id, "ВайТур", users, deleted=True)
    
    assert response.status_code == 400, f"Expected 400, but got {response.status_code}"
    with pytest.raises(requests.HTTPError):
        response.raise_for_status()
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        assert "Error" in str(e) or "Bad Request" in str(e)

def test_get_project_by_id_positive(api_client):
    client, api_key = api_client
    users = {
        "f3d388f7-4c11-4903-9d08-10e09bfa57b7": "worker"
    }
    project_response = client.create_project(api_key, "Test Project", users)
    assert project_response.status_code == 201 

    project_data = project_response.json()
    project_id = project_response['id']

    response = requests.get(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )
    response.raise_for_status()
        
    data = response.json()
    assert data.get("id") == project_id

def test_get_project_by_id_negative(api_client):
    client, api_key = api_client
    users = [{"id": "ppldifun`1123", "role": "worker"}]
    response = requests.get(
        f"{BASE_URL}/api-v2/projects/invalid_id",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )
    with pytest.raises(requests.HTTPError):
        response.raise_for_status()
