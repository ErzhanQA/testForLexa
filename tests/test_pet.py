import pytest
from Reader import Reader
from groups.PetClass import Pet


class TestPet:
    """ Класс тестирования хендлеров группы Pet """
    correct_data_for_get_pet = Reader.read_csv_file("correct_data_for_get_pet.csv", delimiter=",")
    correct_data_for_get_non_existent_pet = Reader.read_csv_file("correct_data_for_get_non_existent_pet.csv",
                                                                 delimiter=",")
    incorrect_data_for_get_pet = Reader.read_csv_file("incorrect_data_for_get_pet.csv", delimiter=",")

    @pytest.mark.positive
    @pytest.mark.parametrize(correct_data_for_get_pet.head, correct_data_for_get_pet.body)
    def test_get_pet(self, pet_id):
        response = Pet().get_pet(pet_id)
        assert response.status_code == 200, "Неверный статус код"
        assert response.json()["id"] == pet_id, "Неверный идентификатор животного"

    @pytest.mark.negative
    @pytest.mark.parametrize(correct_data_for_get_non_existent_pet.head, correct_data_for_get_non_existent_pet.body)
    def test_get_pet(self, pet_id, code, message):
        response = Pet().get_pet(pet_id)
        assert response.status_code == 404, "Неверный статус код"
        assert response.json()["code"] == code, "Неверный код ошибки"
        assert response.json()["message"] == message, "Неверное сообщение об ошибке"

    @pytest.mark.negative
    @pytest.mark.parametrize(incorrect_data_for_get_pet.head, incorrect_data_for_get_pet.body)
    def test_get_pet(self, pet_id, status_code, code, message):
        response = Pet().get_pet(pet_id)
        assert response.status_code == status_code, "Неверный статус код"
        assert response.json()["code"] == code, "Неверный код ошибки"
        assert response.json()["message"] == message, "Неверное сообщение об ошибке"
