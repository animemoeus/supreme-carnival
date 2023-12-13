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

    def search_city(self, search):
        for data in self.get_all_city():
            if (
                search.lower() in data.get("province").lower()
                or search.lower() in data.get("city_name").lower()
            ):
                return data

        return None

    def validate_city_id(self, id: int) -> None | dict:
        for data in self.get_all_city():
            if data.get("city_id") == str(id):
                return data

        return None
