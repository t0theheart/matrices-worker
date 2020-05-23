from abc import ABC, abstractmethod


class MatricesGeneratorABC(ABC):
    @abstractmethod
    def generate_and_write_matrices(self, height: int, width: int, write_to: str):
        """text"""
