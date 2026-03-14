import requests


class ApiClient:

    def __init__(self, base_url, login, password):
        self.base_url = base_url
        self.login = login
        self.password = password


    def auth_data(self):
        resp = requests.post(f"{self.base_url}/api-v2/auth/companies", json={
        "login": self.login,
        "password": self.password
    })
        resp.raise_for_status()
        company_id = resp.json()['content'][0]['id']
        return {
        "login": self.login,
        "password": self.password,
        "companyId": company_id
    }

    def get_api_key(self, auth_data):
        url = f"{self.base_url}/api-v2/auth/keys/get"
        resp = requests.post(url, json=auth_data)
        resp.raise_for_status()
        return resp.json()["key"]

    def create_user(self, api_key, email):
        url = f"{self.base_url}/api-v2/users"
        headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
        resp = requests.post(url, headers=headers, json={
        "email": email,
        "isAdmin": False
    })
        resp.raise_for_status()
        return resp.json()["id"]

    def get_project(self, api_key, title, users):
        url = f"{self.base_url}/api-v2/projects"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        resp = requests.post(url, headers=headers, json={
            "title": title,
            "users": users
        })
        resp.raise_for_status()
        return resp.json()["id"]
    def edit_project(self, api_key, project_id, new_name, users, deleted=False):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            "deleted": deleted,
            "title": new_name,
            "users": users
        }
        resp = requests.put(url, headers=headers, json=data)
        resp.raise_for_status()
        return resp.json()
