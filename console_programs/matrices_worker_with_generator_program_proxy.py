from console_programs.abc import ConsoleMatricesWorkerProgramABC
from console_programs.matrices_worker_with_generator_program import ConsoleMatricesWorkerWithGeneratorProgram


class ConsoleMatricesWorkerWithGeneratorProgramProxy(ConsoleMatricesWorkerProgramABC):
    def __init__(self, program: ConsoleMatricesWorkerWithGeneratorProgram):
        self._program = program
        self._read_from = 'proxy_generated_matrices.json'
        self._write_to = 'proxy_result.json'
        self._counter = 0

    def _up_count(self):
        self._counter += 1

    def _log(self):
        print(f'Program has been started for {self._counter} times')

    def start(self):
        self._program._worker.generate_and_write_matrices(write_to=self._read_from)
        self._program._worker.put_matrices_sum_to_file(read_from=self._read_from, write_to=self._write_to)
        self._up_count()
        self._log()
