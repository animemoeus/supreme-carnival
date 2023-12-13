import requests


class RajaOngkir:
    def __init__(self):
        self.base_url = "https://api.rajaongkir.com/starter"
        self.api_key = (
            "80277394acf599ed1cc96058b79d57cf"  # Move this to .env for production
        )

    def get_all_city(self):
        url = f"{self.base_url}/city"
        headers = {"key": self.api_key}

        response = requests.request("GET", url, headers=headers)
        cities = response.json().get("rajaongkir").get("results")
        return cities

    def check_city(self, city: str) -> bool:
        if not city:
            return False

        cities = [city.get("city_name").lower() for city in self.get_all_city()]

        if city.lower() in cities:
            return True

        return False
