import random as rand

print("Hello World")

radnInt = rand.radnint(1, 10)
while(1):
  '''you might need to do casting!'''
  guess = int(input("Enter secret number: "))
  if guess < randInt:
    print('Too low')
  elif guess > randInt:
    print('Too high')
  elif guess  == randInt:
    print('Congratulation!!')
  else:
    print('Unknown input:)
