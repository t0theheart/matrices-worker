from console_programs.abc import ConsoleMatricesWorkerProgramABC
from matrices_workers import MatricesWorkerABC


class ConsoleMatricesWorkerProgram(ConsoleMatricesWorkerProgramABC):
    def __init__(self, worker: MatricesWorkerABC):
        self._worker = worker
        self._read_from = None
        self._write_to = None

    def _input_read_from(self):
        self._read_from = input('Enter a path to read from: ')

    def _input_write_to(self):
        self._write_to = input('Enter a path to write to: ')

    def _output_result(self):
        print(f'Result of matrices sum was written in "{self._write_to}"')
        self._worker.put_matrices_sum_to_file(read_from=self._read_from, write_to=self._write_to)

    def start(self):
        print('"Matrices worker" is started!')
        self._input_read_from()
        self._input_write_to()
        self._output_result()
        print('End')
        exit()
