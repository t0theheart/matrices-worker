from matrices_workers import MatricesWorker, MatricesGenerator, MatricesGeneratorAdapter


class Client:
    def __init__(self, worker: MatricesWorker):
        self._worker = worker

    def do_something(self, read_from: str, write_to: str):
        self._worker.put_matrices_sum_to_file(read_from, write_to)


matrices_worker_1 = MatricesWorker()
matrices_worker_2 = MatricesGenerator(min_value=-10, max_value=10, height=3, width=3)

# Client's object can work with MatricesWorker's object!
client_1 = Client(matrices_worker_1)
client_1.do_something(read_from='matrices.json', write_to='result.json')

# Expected type 'MatricesWorker', got 'MatricesGenerator' instead.... Oops!
# Client can't work with MatricesGenerator's object, the object doesn't have 'put_matrices_sum_to_file' method
try:
    client_2 = Client(matrices_worker_2)
    client_2.do_something(read_from='matrices.json', write_to='result.json')
except AttributeError:
    pass


matrices_worker_3 = MatricesGeneratorAdapter(min_value=-20, max_value=20, height=4, width=4)

# MatricesGenerator's object has its own method 'generate_and_write_matrices'
matrices_worker_3.generate_and_write_matrices(write_to='new_matrices.json')

# And our client can work with it! MatricesGeneratorAdapter's object has 'put_matrices_sum_to_file' method!
client_3 = Client(matrices_worker_3)
client_3.do_something(read_from='new_matrices.json', write_to='new_result.json')
