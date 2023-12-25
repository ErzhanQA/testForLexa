import requests
from requests import Response
from jsonschema import validate
from groups.schemas.get_pet_schems import get_pet_schemas


class Pet:
    """ Класс работы с животными """
    url = "https://petstore.swagger.io/v2/pet"

    def get_pet(self, pet_id: int) -> Response:
        """ Метод получения информации о животном """
        response = requests.get(url=f"{self.url}/{pet_id}")
        try:
            validate(response.json(), get_pet_schemas[response.status_code])
        except Exception:
            raise TypeError("Ответ не прошел валидацию")
        return response
