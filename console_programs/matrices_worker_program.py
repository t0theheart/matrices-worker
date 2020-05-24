from console_programs.abc import ConsoleMatricesProgramABC


class ConsoleMatricesWorkerProgram(ConsoleMatricesProgramABC):
    def _input_read_from(self):
        self._read_from = input('Enter a path to read from: ')

    def start(self):
        print('"Matrices worker" is started!')
        self._input_read_from()
        self._input_write_to()
        self._output_result()
        print('End')
        exit()
