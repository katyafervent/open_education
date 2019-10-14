input = 'input.txt'
with open(input) as f:
    numbers = f.readline().split(' ')
result = sum(map(lambda item: int(item), numbers))

output = 'output.txt'
with open(output, 'w') as f:
    f.write(str(result))
