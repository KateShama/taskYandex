import json
import random

class CityPicker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cities = []
        self.load_cities()

    def load_cities(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            for city_data in data:
                name = city_data.get('name')
                population = city_data.get('population')
                if name and population:
                    self.cities.append((name, population))

    def get_random_city(self):
        total_population = sum(city[1] for city in self.cities)
        random_value = random.random() * total_population
        population_sum = 0
        for city in self.cities:
            population_sum += city[1]
            if population_sum >= random_value:
                return city[0]

