import requests


class AirportController:

    def __init__(self):
        self.base_url = "https://airportgap.com/api"

    def get_airports(self):
        response = requests.get(f"{self.base_url}/airports")
        return response

    def calculate_distance(self, payload):
        response = requests.post(f"{self.base_url}/airports/distance", json=payload)
        return response
