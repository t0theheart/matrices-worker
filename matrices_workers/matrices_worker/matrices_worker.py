from matrices_workers.matrices_worker.abc import MatricesWorkerABC
import json


class MatricesWorker(MatricesWorkerABC):
    @staticmethod
    def _read_matrices(path: str) -> tuple:
        with open(path, 'r') as f:
            matrices = json.load(f)
        return matrices['matrix_1'], matrices['matrix_2']

    @staticmethod
    def _sum_matrices(matrix_1: list, matrix_2: list) -> list:
        return [
           [
               matrix_1[line][elem] + matrix_2[line][elem] for elem in range(len(matrix_1[0]))
           ] for line in range(len(matrix_1))
        ]

    @staticmethod
    def _write_matrix(path: str, matrix: list):
        with open(path, 'w') as f:
            json.dump({'result': matrix}, fp=f)

    def put_matrices_sum_to_file(self, read_from: str, write_to: str):
        matrix_1, matrix_2 = self._read_matrices(read_from)
        result = self._sum_matrices(matrix_1, matrix_2)
        self._write_matrix(write_to, result)
