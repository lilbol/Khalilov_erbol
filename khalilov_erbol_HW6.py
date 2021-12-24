numbers = [2, 7, 11, 15]
desired_sum = int(input("желаемая сумма:"))
for i in range(len(numbers)-1):
    if (numbers[i]+(numbers[i+1])) == desired_sum:
        print([i, i+1])
