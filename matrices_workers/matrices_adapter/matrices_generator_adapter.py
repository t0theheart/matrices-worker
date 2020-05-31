from matrices_workers.matrices_worker.matrices_worker import MatricesWorker
from matrices_workers.matrices_generator.matrices_generator import MatricesGenerator


class MatricesGeneratorAdapter(MatricesWorker, MatricesGenerator):
    """Adapter for MatricesGenerator"""
