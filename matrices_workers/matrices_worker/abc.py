from abc import ABC, abstractmethod


class MatricesWorkerABC(ABC):
    @abstractmethod
    def put_matrices_sum_to_file(self, read_from: str, write_to: str): pass
