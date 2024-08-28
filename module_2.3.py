numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

numbers_ = 0

while len(numbers) > numbers_:
    
    if numbers[numbers_] > 0:
        
        print(numbers[numbers_])
          
    numbers_ += 1

    if numbers[numbers_] < 0:
        
        break
         