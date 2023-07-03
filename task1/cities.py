import requests
import json
import random

class CityPicker:
    def __init__(self, file_url):
        self.file_url = file_url
        self.cities = []
        self.load_cities()

    def load_cities(self):
        response = requests.get(self.file_url)
        data = json.loads(response.text)
        for city_data in data:
            name = city_data.get('name')
            population = city_data.get('population')
            if name and population:
                self.cities.append((name, population))

    def get_random_city(self):
        total_population = sum(city[1] for city in self.cities)
        probabilities = [city[1] / total_population for city in self.cities]
        random_value = random.random()
        population_sum = 0
        for city, probability in zip(self.cities, probabilities):
            population_sum += probability
            if population_sum >= random_value:
                return city[0]

file_url = "https://raw.githubusercontent.com/KateShama/taskYandex/main/task1/input.json"
city_picker = CityPicker(file_url)
selected_city = city_picker.get_random_city()
print("Выбранный город:", selected_city)


