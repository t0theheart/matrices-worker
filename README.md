# matrices-worker

## [OTUS](https://otus.ru) homework

### Goals
Implement some OOP patterns:
1. "Adapter"
2. "Proxy"

### Description
There are two modules:
1. **matrices_workers**
2. **console_programs**

There are classes for doing some operations with matrices in **matrices_workers**.
The operations like read and write from file, add and generate matrices.

**console_programs** objects provide a console interface to interact with **matrices_workers** objects.

### Adapter
Client **ConsoleMatricesWorkerProgram** works with **MatricesWorker** object.
```python
worker = MatricesWorker()
program = ConsoleMatricesWorkerProgram(worker)
program.start()
```
But our client can't work with **MatricesGenerator** object.
```python
worker = MatricesGenerator(min_value=-10, max_value=10, height=3, width=3)
program = ConsoleMatricesWorkerProgram(worker)
program.start()
# AttributeError: 'MatricesGenerator' object has no attribute 'put_matrices_sum_to_file'
```
So adapter class **MatricesGeneratorAdapter** is need here!
```python
worker = MatricesGeneratorAdapter(min_value=-10, max_value=10, height=3, width=3)
program = ConsoleMatricesWorkerProgram(worker)
program.start()
```
Look more detail explanation of adapter in examples.


### Proxy
If we want to add new logic to class without refactoring and changing interface we could use proxy.
```python
worker = MatricesGeneratorAdapter(min_value=-20, max_value=20, height=4, width=4)
program = ConsoleMatricesWorkerWithGeneratorProgram(worker)
program_proxy = ConsoleMatricesWorkerWithGeneratorProgramProxy(program)
```
This proxy class logs every **start** method calling 
```python
program_proxy.start()  # Program has been started for 1 times
program_proxy.start()  # Program has been started for 2 times
program_proxy.start()  # Program has been started for 3 times
```
And fills **read from** and **write to** attributes instead of user inputs in class constructor.
```python
def __init__(self, program: ConsoleMatricesWorkerWithGeneratorProgram):
    self._program = program
    self._read_from = 'proxy_generated_matrices.json'
    self._write_to = 'proxy_result.json'
    self._counter = 0
```

### Difference
- Adapter adds new logic and gives another interface.
- Proxy adds new logic and gives the same interface.


#### There are three programs:
1. program_1.py reads matrices from file and writes sum to another file
2. program_2.py generates matrices to file and writes sum to another file.
3. program_3.py does as the program_2 but without console interface.

To run program:
```bash
$ python program_1.py
```

To run tests:
```bash
$ python -m unittest tests
```