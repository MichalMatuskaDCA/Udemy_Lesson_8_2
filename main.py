#Write your code below this line 👇
def prime_checker(number):
  p = False
  for num in range(2, number):
    if number % num == 0:
      print(f'{number} is not a prime number.')
      p = True
      break
  if p == False:
    print(f'{number} is a prime number.')
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



