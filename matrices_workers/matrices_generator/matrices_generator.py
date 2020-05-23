from matrices_workers.matrices_generator.abc import MatricesGeneratorABC
import random
import json


class MatricesGenerator(MatricesGeneratorABC):
    def __init__(self, min_value: int, max_value: int):
        self._min_value = min_value
        self._max_value = max_value

    def _generate_matrix(self, height: int, width: int) -> list:
        return [
            [
                random.randint(self._min_value, self._max_value) for _ in range(width)
            ] for _ in range(height)
        ]

    def _generate_matrices(self, height: int, width: int) -> dict:
        return {
            "matrix_1": self._generate_matrix(height, width),
            "matrix_2": self._generate_matrix(height, width),
        }

    def generate_and_write_matrices(self, height: int, width: int, write_to: str):
        matrices = self._generate_matrices(height, width)
        with open(write_to, 'w') as f:
            json.dump(matrices, fp=f)
