# Jedsada Thavornfung (JT43227)
# HW 5 - Recipes

# List
chicken_soup = ['chicken', 'chicken broth', 'carrots', 'celery', 'noodles']
lasagna = ['lasagna noodles', 'pasta sauce', 'ricotta']
grilled_cheese = ['bread', 'butter', 'cheese']
garden_salad = ['lettuce', 'tomatoes', 'carrots', 'olives']
my_special = ['shrimp','pork','rice','oyster source','lemons']

# Function 1: List 1
def choice_first(choice_1):    
    if(choice_1.lower() == 'chicken soup'):                  # 1.Chicken Soup
        print(choice_1, end = ': ')
        choice_1 = chicken_soup
        print(*choice_1, sep = ', ')
    elif(choice_1.lower() == 'lasagna'):                     # 1. Lasagna
        print(choice_1, end = ': ')
        choice_1 = lasagna
        print(*choice_1, sep = ', ')
    elif(choice_1.lower() == 'grilled cheese'):              # 1. Grilled Cheese
        print(choice_1, end = ': ')
        choice_1 = grilled_cheese
        print(*choice_1, sep = ', ')
    elif(choice_1.lower() == 'garden salad'):                # 1. Garden Salad
        print(choice_1, end = ': ')
        choice_1 = garden_salad
        print(*choice_1, sep = ', ')
    elif(choice_1.lower() == 'jedsada\'s special'):          # 1. Jedsada's Special
        print(choice_1, end = ': ')
        choice_1 = my_special
        print(*choice_1, sep = ', ')
    else:
        print('Wrong Input. Please check your spelling!')

# Function 2: List 2
def choice_second(choice_2):
    if(choice_2.lower() == 'chicken soup'):                  # 2.Chicken Soup
        print(choice_2, end = ': ')
        choice_2 = chicken_soup
        print(*choice_2, sep = ', ')
    elif(choice_2.lower() == 'lasagna'):                     # 2.Lasagna
        print(choice_2, end = ': ')
        choice_2 = lasagna
        print(*choice_2, sep = ', ')
    elif(choice_2.lower() == 'grilled cheese'):              # 2.Grilled Cheese
        print(choice_2, end = ': ')
        choice_2 = grilled_cheese
        print(*choice_2, sep = ', ')
    elif(choice_2.lower() == 'garden salad'):                # 2.Garden Salad
        print(choice_2, end = ': ')
        choice_2 = garden_salad
        print(*choice_2, sep = ', ')
    elif(choice_2.lower() == 'jedsada\'s special'):          # 2.Jedsada's Special
        print(choice_2, end = ': ')
        choice_2 = my_special
        print(*choice_2, sep = ', ')
    else:
        print('Wrong Input. Please check your spelling!')

# Actual Input
choice_1 = str(input('What would you like to make? (Choose: Chicken Soup, Lasagna, Grilled Cheese, Garden Salad, Jedsada\'s Special): '))

if(choice_1.lower() == 'chicken soup'):                   # 1. Chicken Soup
    choice_first(choice_1)                                # Choice 1
    choice_2 = str(input('What else would you like to make? (Choose: Chicken Soup, Lasagna, Grilled Cheese, Garden Salad, Jedsada\'s Special): '))
    choice_second(choice_2)                               # Choice 2
    emp_list = []
    addition_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished): ')
    while (addition_list.lower() != 'done'):
        emp_list.append(addition_list)
        addition_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished): ')
    if(choice_2.lower() == 'chicken soup'):               # 2. Chicken Soup
        print('Grocery List:', end = ' ')
        print(*chicken_soup, *chicken_soup, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'lasagna'):                  # 2. Lasagna
        print('Grocery List:', end = ' ') 
        print(*chicken_soup, *lasagna, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'grilled cheese'):           # 2. Grilled Cheese
        print('Grocery List:', end = ' ')
        print(*chicken_soup, *grilled_cheese, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'garden salad'):             # 2. Garden Salad
        print('Grocery List:', end = ' ')
        print(*chicken_soup, *garden_salad, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'jedsada\'s special'):       # 2. Jedsada's Special
        print('Grocery List:', end = ' ')
        print(*chicken_soup, *my_special, *emp_list, sep = ', ')
    else:
        print('Wrong Input. Please check your spelling!')
elif(choice_1.lower() == 'lasagna'):                      # 1. Lasagna
    choice_first(choice_1)                                # Choice 1
    choice_2 = str(input('What else would you like to make? (Choose: Chicken Soup, Lasagna, Grilled Cheese, Garden Salad, Jedsada\'s Special): '))
    choice_second(choice_2)                               # Choice 2
    emp_list = []
    addition_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished): ')
    while (addition_list.lower() != 'done'):
        emp_list.append(addition_list)
        addition_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished): ')
    if(choice_2.lower() == 'chicken soup'):               # 2. Chicken Soup
        print('Grocery List:', end = ' ')
        print(*lasagna, *chicken_soup, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'lasagna'):                  # 2. Lasagna
        print('Grocery List:', end = ' ') 
        print(*lasagna, *lasagna, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'grilled cheese'):           # 2. Grilled Cheese
        print('Grocery List:', end = ' ')
        print(*lasagna, *grilled_cheese, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'garden salad'):             # 2. Garden Salad
        print('Grocery List:', end = ' ')
        print(*lasagna, *garden_salad, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'jedsada\'s special'):       # 2. Jedsada's Special
        print('Grocery List:', end = ' ')
        print(*lasagna, *my_special, *emp_list, sep = ', ')
    else:
        print('Wrong Input. Please check your spelling!')
elif(choice_1.lower() == 'grilled cheese'):               # 1. Grilled Cheese
    choice_first(choice_1)                                # Choice 1
    choice_2 = str(input('What else would you like to make? (Choose: Chicken Soup, Lasagna, Grilled Cheese, Garden Salad, Jedsada\'s Special): '))
    choice_second(choice_2)                               # Choice 2
    emp_list = []
    addition_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished): ')
    while (addition_list.lower() != 'done'):
        emp_list.append(addition_list)
        addition_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished): ')
    if(choice_2.lower() == 'chicken soup'):               # 2. Chicken Soup
        print('Grocery List:', end = ' ')
        print(*grilled_cheese, *chicken_soup, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'lasagna'):                  # 2. Lasagna
        print('Grocery List:', end = ' ') 
        print(*grilled_cheese, *lasagna, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'grilled cheese'):           # 2. Grilled Cheese
        print('Grocery List:', end = ' ')
        print(*grilled_cheese, *grilled_cheese, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'garden salad'):             # 2. Garden Salad
        print('Grocery List:', end = ' ')
        print(*grilled_cheese, *garden_salad, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'jedsada\'s special'):       # 2. Jedsada's Special
        print('Grocery List:', end = ' ')
        print(*grilled_cheese, *my_special, *emp_list, sep = ', ')
    else:
        print('Wrong Input. Please check your spelling!')
elif(choice_1.lower() == 'garden salad'):                 # 1. Garden Salad
    choice_first(choice_1)                                # Choice 1
    choice_2 = str(input('What else would you like to make? (Choose: Chicken Soup, Lasagna, Grilled Cheese, Garden Salad, Jedsada\'s Special): '))
    choice_second(choice_2)                               # Choice 2
    emp_list = []
    addition_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished): ')
    while (addition_list.lower() != 'done'):
        emp_list.append(addition_list)
        addition_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished): ')
    if(choice_2.lower() == 'chicken soup'):               # 2. Chicken Soup
        print('Grocery List:', end = ' ')
        print(*garden_salad, *chicken_soup, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'lasagna'):                  # 2. Lasagna
        print('Grocery List:', end = ' ') 
        print(*garden_salad, *lasagna, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'grilled cheese'):           # 2. Grilled Cheese
        print('Grocery List:', end = ' ')
        print(*garden_salad, *grilled_cheese, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'garden salad'):             # 2. Garden Salad
        print('Grocery List:', end = ' ')
        print(*garden_salad, *garden_salad, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'jedsada\'s special'):       # 2. Jedsada's Special
        print('Grocery List:', end = ' ')
        print(*garden_salad, *my_special, *emp_list, sep = ', ')
    else:
        print('Wrong Input. Please check your spelling!')
elif(choice_1.lower() == 'jedsada\'s special'):           # 1. Jedsada's Special
    choice_first(choice_1)                                # Choice 1
    choice_2 = str(input('What else would you like to make? (Choose: Chicken Soup, Lasagna, Grilled Cheese, Garden Salad, Jedsada\'s Special): '))
    choice_second(choice_2)                               # Choice 2
    emp_list = []
    addition_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished): ')
    while (addition_list.lower() != 'done'):
        emp_list.append(addition_list)
        addition_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished): ')
    if(choice_2.lower() == 'chicken soup'):               # 2. Chicken Soup
        print('Grocery List:', end = ' ')
        print(*my_special, *chicken_soup, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'lasagna'):                  # 2. Lasagna
        print('Grocery List:', end = ' ') 
        print(*my_special, *lasagna, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'grilled cheese'):           # 2. Grilled Cheese
        print('Grocery List:', end = ' ')
        print(*my_special, *grilled_cheese, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'garden salad'):             # 2. Garden Salad
        print('Grocery List:', end = ' ')
        print(*my_special, *garden_salad, *emp_list, sep = ', ')
    elif(choice_2.lower() == 'jedsada\'s special'):       # 2. Jedsada's Special
        print('Grocery List:', end = ' ')
        print(*my_special, *my_special, *emp_list, sep = ', ')
    else:
        print('Wrong Input. Please check your spelling!')
else:
    print('Wrong Input. Please check your spelling!')

