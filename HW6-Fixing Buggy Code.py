# Jedsada Thavornfung (JT43227)
# Homework 6: Buggy Code

def get_average(list_of_num):
  total = 0
  for i in list_of_num:
    total = total + i
  avg = total
  
  # Zero Division Error
  try:
    avg = avg/len(list_of_num)  # Can't divided by 0
  except ZeroDivisionError as err:
    print('Error message: ',err)
  avg = round(avg)
  return avg
 
def main():
  numbers = ['one','two','three'] 
  # NameError
  try: 
    print(get_average(number))  # No 'number' variable
  except NameError as err:
    print('Error message: ',err)
  greeting = 'Hello World'
  
  # IndexError
  try:
    for i in range(len(greeting)+1):
      print(greeting[i])       # Not enough value for index
  except IndexError as err:
    print('Error message: ',err)
    
  numbers = []
  print(get_average(numbers))
  # IndexError
  try:
    print(numbers[10])         # Not enough value for index
  except IndexError as err: 
    print('Error message: ',err)
  
  # ValueError
  try:
    color = int(input('Enter your favorite color: '))  # Need int not str
  except ValueError as err:
    print('Error message: ',err)
  
if __name__=="__main__":
  main()