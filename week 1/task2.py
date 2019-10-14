input = 'input.txt'
with open(input) as f:
    numbers = f.readline().split(' ')
n1, n2 = map(lambda item: int(item), numbers)
result = n1 + n2*n2
output = 'output.txt'
with open(output, 'w') as f:
    f.write(str(result))
