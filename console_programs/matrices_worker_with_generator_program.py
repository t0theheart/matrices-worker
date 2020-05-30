from console_programs.abc import ConsoleMatricesWorkerProgramABC
from matrices_workers import MatricesWorkerABC, MatricesGeneratorABC


class ConsoleMatricesWorkerWithGeneratorProgram(ConsoleMatricesWorkerProgramABC):
    def __init__(self, worker: MatricesWorkerABC and MatricesGeneratorABC):
        self._worker = worker
        self._read_from = None
        self._write_to = None

    def _generate_matrices(self):
        matrices_path = input('Enter a path to generate matrices: ')
        self._worker.generate_and_write_matrices(write_to=matrices_path)
        self._read_from = matrices_path

    def _input_write_to(self):
        self._write_to = input('Enter a path to write to: ')

    def _output_result(self):
        print(f'Result of matrices sum was written in "{self._write_to}"')
        self._worker.put_matrices_sum_to_file(read_from=self._read_from, write_to=self._write_to)

    def start(self):
        print('"Matrices worker with generator" is started!')
        self._generate_matrices()
        self._input_write_to()
        self._output_result()
        print('End')
        exit()
