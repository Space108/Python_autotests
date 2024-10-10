import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a8ccd767681be2b77c55c99ec6a77d23'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '7117'


def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def get_trainer_name():
    response = requests.get(f'{URL}/trainers/{TRAINER_ID}', headers=HEADER)
    data = response.json()
    trainer_name = data.get('name')
    if trainer_name == 'Артист':
        print(f"Имя тренера найдено и соответствует: {trainer_name}")
        print("Отличная работа")
    else:
        print("Имя тренера не найдено или не является 'Артист'.")

get_trainer_name()


