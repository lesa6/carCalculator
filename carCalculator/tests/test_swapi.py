import requests
import pytest

URL = 'https://wexler.io'

# @pytest.fixture
# def token(password):
#     url = f'{URL}/user/login/'
#     res = requests.post(url, data={
#         'username': 'egor.wexler@voitixler.com',
#         'password': password
#     })
#     data = res.json()
#     return data['access']

# def test_get_car_engines(token):
#     url = f'{URL}/garage/car_engines/'
#     res = requests.get(url, header={'Authotization': f'Bearer {token}'})
#     assert res.status_code == 200
#     data = res.json()

#     assert isinstance(data , dict)


def test_people_api():
    url = 'https://rickandmortyapi.com/api/character'
    res = requests.get(url)
    assert res.status_code == 200

    data = res.json()
    person_found = False
    for person in data['results']:
        if person['name'] == 'Rick Sanchez':
            assert person['gender'] == 'Male'
            person_found = True

    assert person_found


