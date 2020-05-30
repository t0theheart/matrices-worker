from console_programs import ConsoleMatricesWorkerWithGeneratorProgram, ConsoleMatricesWorkerWithGeneratorProgramProxy
from matrices_workers import MatricesGeneratorAdapter


def main():
    worker = MatricesGeneratorAdapter(min_value=-20, max_value=20, height=4, width=4)
    program = ConsoleMatricesWorkerWithGeneratorProgram(worker)
    program_proxy = ConsoleMatricesWorkerWithGeneratorProgramProxy(program)
    program_proxy.start()  # Program has been started for 1 times
    program_proxy.start()  # Program has been started for 2 times
    program_proxy.start()  # Program has been started for 3 times


if __name__ == '__main__':
    main()
