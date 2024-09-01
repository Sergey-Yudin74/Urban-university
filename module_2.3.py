numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

numbers_ = 0

while numbers_ < len(numbers):
    
    if numbers[numbers_] <  0:
        break
    else:
       if numbers[numbers_] >  0:
        print(numbers[numbers_])
    numbers_ += 1
    continue
