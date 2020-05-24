from console_programs.abc import ConsoleMatricesProgramABC


class ConsoleMatricesWorkerWithGeneratorProgram(ConsoleMatricesProgramABC):
    def _generate_matrices(self):
        matrices_path = input('Enter a path to generate matrices: ')
        self._worker.generate_and_write_matrices(write_to=matrices_path)
        self._read_from = matrices_path

    def start(self):
        print('"Matrices worker with generator" is started!')
        self._generate_matrices()
        self._input_write_to()
        self._output_result()
        print('End')
        exit()
