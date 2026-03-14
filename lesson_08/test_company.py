import pytest
from ApiClient import ApiClient

BASE_URL = "https://ru.yougile.com"
LOGIN = "prikhodko.ol14@gmail.com"
PASSWORD = "qwedsass13"

@pytest.fixture
def api_client():
    client = ApiClient(BASE_URL, LOGIN, PASSWORD)
    auth_data = client.auth_data()
    api_key = client.get_api_key(auth_data)
    return client

def test_create_project_positive(api_client):
    auth_data = api_client.auth_data()
    api_key = api_client.get_api_key(auth_data)
    users = {
        "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
        "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
    }
    project_response = api_client.get_project(api_key, "ОлолоТур", users)
    assert 'id' in project_response
    assert project_response.get('title') == "ОлолоТур"


def test_create_project_negative(api_client):
    client = api_client
    auth_data = client.auth_data()
    api_key = client.get_api_key(auth_data)
    users = {
        "fbsoe123": "worker",
        "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
    }
    response_json = client.get_project(api_key, "Пыщ", users)

def test_edit_project_positive(api_client):
    client, api_key = api_client
    users = {
        "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
        "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
    }
    project_response = client.get_project(api_key, "Помянем", users)
    project_id = project_response.get('id')

    new_users = {
        "4902b994-b806-4af4-acec-018ea5ea6468": "manager", 
        "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "worker"
    }
    response = client.edit_project(api_key, project_id, "Обновленный проект", new_users, deleted=True)

    assert response.get('id') == project_id
    assert response.get('title') == "Обновленный проект"
    assert response.get('deleted') is True


def test_edit_negativce(api_client):
    auth_data = api_client.auth_data()
    api_key = api_client.get_api_key(auth_data)
    project_id = "id0dfrkmsbfu"
    users = [{"id": "4902b994-b806-4af4-acec-018ea5ea6468", "role": "worker"},
             {"id": "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018", "role": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"}]
    response = api_client.edit_project(api_key, project_id, "ВайТур", users, deleted=True)
    try:
        response.raise_for_status()
    except requests.HTTPError:
        assert response.status_code == 404

def test_get_project_by_id_positive(api_client):
    client = api_client
    auth_data = client.auth_data()
    api_key = client.get_api_key(auth_data)
    # Создаём проект, получаем id
    users = {
        "4902b994-b806-4af4-acec-018ea5ea6468": "worker"
    }
    project_response = client.get_project(api_key, "Test Project", users)
    project_id = project_response['id']
    # Теперь делаем GET по id
    response = requests.get(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data.get("id") == project_id

def test_get_project_by_id_negative(api_client):
    client = api_client
    auth_data = client.auth_data()
    api_key = client.get_api_key(auth_data)
    # Создаём проект, получаем id
    users = {
        "ppldifun`1123": "worker"
    }
    project_response = client.get_project(api_key, "Test Project", users)
    project_id = project_response['id']
    # Теперь делаем GET по id
    response = requests.get(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 404
    data = response.json()
    assert data.get("id") == project_id
