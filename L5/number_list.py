number_list = [11, 13, 12, 10, 5, 8, 15, 18]

count = 0
for num in number_list:
    print(num, count)
    if num < 10:
        count = count + 1
    
print(count)