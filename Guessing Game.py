import random
# توليد رقم عشوائي  من 1 الي 10
secret_number = random.randint(0, 10)

#ترحيب بالمستخدم 
print (" |❤️  Welcome to the guessing game 😍 | ")
print(" 👀  I chose a number from 1 to 10. Try to guess it 😉 ")
while True:
    guess = int(input("Enter your number ➡️ "))
    
    if guess==secret_number:
        print("Good  💓  ✅"  )
        break
    elif guess < secret_number:
        print("Your guess is false ✖️ ")
        print("Try again 🔃 ")