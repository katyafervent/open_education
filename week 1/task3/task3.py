# sortirovka vstavkami
input = 'input.txt'
with open(input) as f:
    length = int(f.readline())
    numbers = list(map(lambda item: int(item), f.readline().split(' ')))

sorted_numbers = numbers
positions = [1]

for i in range(1, length):
    while i > 0 and numbers[i - 1] > numbers[i]:
        numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
        i -= 1
    positions.append(i + 1)

output = 'output.txt'

with open(output, 'w') as f:
    result1 = ' '.join(str(item) for item in positions)
    f.write(result1)
    f.write('\n')
    result2 = ' '.join(str(item) for item in numbers)
    f.write(result2)
