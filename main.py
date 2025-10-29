from random import randint
def funct():
  random_num = randint(1,100)
  user_number = -1
  guess = 0
  while(user_number != random_num) :
      guess +=1
      user_number = int(input("Guess the random number selected by the computer : "))
      if(user_number < random_num ) :
        print ("shiiit! you selected a lower number. Now go for a higher number : ")
      elif(user_number > random_num):
        print("oh nooooo! You selected a higher number. Now go for a lower number : ")
  print(f'''eemmmmm you have guessed the right number {random_num} in {guess} attempts ''')

while True:
  funct()
  user = input("want to try again (yes/no) : ").lower()
  if (user != "yes"):
    print (" No problem!! See you soon 😊😊")
    break
