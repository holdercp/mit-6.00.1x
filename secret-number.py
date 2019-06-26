start = 0
end = 100

print('Please think of a number between 0 and 100')

while True:
  guess = int((start + end) / 2)

  print('Is your secret number ' + str(guess) + '?')

  userInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
  
  if userInput == 'l':
    start = guess
  elif userInput == 'h':
    end = guess
  elif userInput == 'c':
    break
  else:
    print('Sorry, I did not understand your input.')

print('Game over. Your secret number was: ' + str(guess))