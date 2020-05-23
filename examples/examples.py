from matrices_workers.matrices_worker.matrices_worker import MatricesWorker
from matrices_workers.matrices_generator.matrices_generator import MatricesGenerator
from matrices_workers.matrices_adapters.matrices_generator_adapter import MatricesGeneratorAdapter


class Client:
    @staticmethod
    def do_something(worker: MatricesWorker):
        worker.put_matrices_sum_to_file(read_from='matrices.json', write_to='result.json')


matrices_worker_1 = MatricesWorker()
matrices_worker_2 = MatricesGenerator(min_value=-10, max_value=10)

# Client can work with MatricesWorker's object!
Client.do_something(matrices_worker_1)

# Expected type 'MatricesWorker', got 'MatricesGenerator' instead.... Oops!
# Client can't work with MatricesGenerator's object, the object doesn't have 'put_matrices_sum_to_file' method
try:
    Client.do_something(matrices_worker_2)
except AttributeError:
    pass


matrices_worker_3 = MatricesGeneratorAdapter(min_value=-10, max_value=10)

# Client can work! MatricesGeneratorAdapter's object has 'put_matrices_sum_to_file' method
Client.do_something(matrices_worker_3)

# and others MatricesGenerator methods!
matrices_worker_3.generate_and_write_matrices(height=3, width=3, write_to='new_matrices.json')
