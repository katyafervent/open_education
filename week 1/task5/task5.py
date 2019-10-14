input = 'input.txt'
with open(input) as f:
    length = int(f.readline())
    numbers = list(map(lambda item: int(item), f.readline().split(' ')))

sorted_numbers = numbers
output = 'output.txt'
f = open(output, 'w')
# for i in range(1, length):
#     initial_i = i
#     while i > 0 and numbers[i - 1] > numbers[i]:
#         numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
#         i -= 1
#     # i = j
#     if i+1 != initial_i+1:
#         f.write('Swap elements at indices {} and {}.\n'.format(i+1, initial_i+1))

def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    j = 0
    while swapped:

        swapped = False
        for i in range(len(nums) - 1):
            initial_i = i

            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
            if swapped:
                f.write('Swap elements at indices {} and {}.\n'.format(j+1, initial_i + 1))

bubble_sort(numbers)
f.write('No more swaps needed.\n')

result2 = ' '.join(str(item) for item in numbers)
f.write(result2)
f.close()
