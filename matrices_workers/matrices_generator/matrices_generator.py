from matrices_workers.matrices_generator.abc import MatricesGeneratorABC
import random
import json


class MatricesGenerator(MatricesGeneratorABC):
    def __init__(self, min_value: int, max_value: int, height: int, width: int):
        self._min_value = min_value
        self._max_value = max_value
        self._height = height
        self._width = width

    def _generate_matrix(self) -> list:
        return [
            [
                random.randint(self._min_value, self._max_value) for _ in range(self._width)
            ] for _ in range(self._height)
        ]

    def _generate_matrices(self) -> dict:
        return {
            "matrix_1": self._generate_matrix(),
            "matrix_2": self._generate_matrix(),
        }

    def generate_and_write_matrices(self, write_to: str):
        matrices = self._generate_matrices()
        with open(write_to, 'w') as f:
            json.dump(matrices, fp=f)
