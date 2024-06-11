from validate_docbr import CPF
from timeit import timeit

cpf = CPF()

print(cpf.generate(True))

cpfs = [
    cpf.generate(),
    cpf.generate(),
    cpf.generate(),
    cpf.generate(),
    cpf.generate(),
]

print(cpf.validate_list(cpfs))
