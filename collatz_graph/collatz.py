def collatz(number):
    if number % 2 == 0:
        return number/2
    if number % 2 != 0:
        return (number*3)+1


while True:
    try:
        user_number = int(input('Please enter a number: '))
        break
    except:
        print('It was supposed to be a number!')

graph_value = user_number
collatz_number_list = []

while user_number != 1:
    user_number = collatz(user_number)
    collatz_number_list.append(int(user_number))

print(collatz_number_list)
