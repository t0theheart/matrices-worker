from console_programs import ConsoleMatricesWorkerProgram
from matrices_workers import MatricesWorker


def main():
    """
        Example of using

        "Matrices worker" is started!
        Enter a path to read from: matrices.json
        Enter a path to write to: result.json
        Result of matrices sum was written in "result.json"
        End
    """
    worker = MatricesWorker()
    program = ConsoleMatricesWorkerProgram(worker)
    program.start()


if __name__ == '__main__':
    main()
