from Src.Logics.start_factory import start_factory
from Src.Logics.deserialization_json import deserialization_json

import unittest
import json

class deserialization_json_test(unittest.TestCase):
    #
    # Проверить механизм десериализации данных в формате Json в текущие модели данных
    #
    def test_deserialize(self):
        # Подготовка 
        with open("nomenclature.json", "r") as f:
            json_data = json.load(f)
        
        # Действие
        deserializer = deserialization_json()
        result = deserializer.from_json(json_data)
        
        # Проверка
        assert result is not None

if __name__ == '__main__':
    unittest.main()
