from console_programs import ConsoleMatricesWorkerWithGeneratorProgram
from matrices_workers import MatricesGeneratorAdapter


def main():
    """
        Example of using

        "Matrices worker with generator" is started!
        Enter a path to generate matrices: generated_matrices.json
        Enter a path to write to: result.json
        Result of matrices sum was written in "result.json"
        End
    """
    worker = MatricesGeneratorAdapter(min_value=-20, max_value=20, height=4, width=4)
    program = ConsoleMatricesWorkerWithGeneratorProgram(worker)
    program.start()


if __name__ == '__main__':
    main()
