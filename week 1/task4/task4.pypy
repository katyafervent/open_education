input = 'input.txt'
with open(input) as f:
    total = int(f.readline())
    income = [[income, i + 1] for i, income in enumerate(map(lambda item: float(item), f.readline().split(' ')))]

sorted_income = income
for i in range(1, total):
    while i > 0 and income[i - 1][0] > income[i][0]:
        income[i - 1], income[i] = income[i], income[i - 1]
        i -= 1
output = 'output.txt'
with open(output, 'w') as f:
    f.write(str(income[0][1]) + ' ' + str(income[total//2][1]) + ' ' + str(income[-1][1]))
