import re

# Part 1

def mul(a,b):
    return a*b

with open("input.txt", "r") as input_file:
    program = input_file.read()

padrao = re.compile(r'mul\(\d+,\d+\)')
ocorrencias = padrao.findall(program)

total = 0
for i in ocorrencias:
    total += eval(i)

print(total)