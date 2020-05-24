from abc import ABC, abstractmethod
from matrices_workers import MatricesWorkerABC, MatricesGeneratorABC


class ConsoleMatricesProgramABC(ABC):
    def __init__(self, worker: MatricesWorkerABC and MatricesGeneratorABC):
        self._worker = worker
        self._read_from = None
        self._write_to = None

    @abstractmethod
    def start(self):
        """text"""

    def _input_write_to(self):
        self._write_to = input('Enter a path to write to: ')

    def _output_result(self):
        print(f'Result of matrices sum was written in "{self._write_to}"')
        self._worker.put_matrices_sum_to_file(read_from=self._read_from, write_to=self._write_to)
