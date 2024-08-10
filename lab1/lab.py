bill_amount = 47.28

total_amount = bill_amount + (bill_amount * 0.15)

each = total_amount / 2

print(f"Each person needs to pay: ${each:.2f}")

# Q2

numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))


result = numerator / denominator
print(f"The result of {numerator} divided by {denominator} is: {result}")


#Q3
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = " }{"
word6 = "so"
word7 = "far?"
sentence = f"{word1} {word2} {word3} {word4}{word5} {word6} {word7}"
print(sentence)

#Q4

word7 = word7.replace('?', '!')
sentence = f"{word1} {word2} {word3} {word4}{word5} {word6} {word7}"
print(sentence)




#Q5

user_input = input("Please enter a statement: ")


length_of_statement = len(user_input)


print(length_of_statement)


#Q6


x = int(input("Enter 1 to multiply, 2 to sum, 3 for division: "))

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if x == 1:
    result = number1 * number2
    print(f"The result = {result}")

elif x == 2:
    result = number1 + number2
    print(f"The result = {result}")

elif x == 3:
    if number2 != 0:
        result = number1 / number2
        print(f"The result = {result}")
    else:
        print("Cannot divide by zero")

else:
    print(f"The value of {x} is not valid")

 
   



 



