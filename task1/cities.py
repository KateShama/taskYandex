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
        probabilities = [city[1] / total_population for city in self.cities]
        random_value = random.random()
        population_sum = 0
        for city, probability in zip(self.cities, probabilities):
            population_sum += probability
            if population_sum >= random_value:
                return city[0]



