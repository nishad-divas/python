#generate a random integer between 1 and 100
import random 
jackpot=random.randint(1,100)


geuss=int(input('geuss kro'))
counter=1

while geuss!=jackpot:
  if geuss<jackpot:
   print('galat!geuss higher ')
  else:
   print('galat!geuss lower')
  geuss=int(input('geuss kro'))
  counter+=1
else:
 print('correct guess')
 print('attemps',counter)
