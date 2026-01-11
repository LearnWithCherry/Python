number_list = [2,7,4,10,23,30]
found = False
target = 9

for i in range(len(number_list)):
    for j in range(i+1, len(number_list)):
        if number_list[i] + number_list[j] == target:
            print(f"{number_list[i]} Plus {number_list[j]} are equal to {target}")
            found = True
            break
        if found:
            break
if not found:
    print("Value not found.")