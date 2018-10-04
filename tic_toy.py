from random import randint
def win(b):
    if (b[7] == b[8] == b[9] == x) or \
            (b[4] == b[5] == b[6] == 'x') or \
            (b[1] == b[2] == b[3] == 'x') or \
            (b[7] == b[4] == b[1] == 'x') or \
            (b[9] == b[6] == b[3] == 'x') or \
            (b[1] == b[5] == b[9] == 'x') or \
            (b[3] == b[5] == b[7] == 'x'):
        print('the'+p1+' win the game')
        exit()
    elif (b[7] == b[8] == b[9] == 'o') or \
            (b[4] == b[5] == b[6] == 'o') or \
            (b[1] == b[2] == b[3] == 'o') or \
            (b[1] == b[4] == b[7] == 'o') or \
            (b[9] == b[6] == b[3] == 'o') or \
            (b[1] == b[5] == b[9] == 'o') or \
            (b[3] == b[5] == b[7] == 'o'):
        print('the '+p2+' win the game')
        exit()






def board(b):
    print(""+b[1]+"   |   "+b[2]+"   |   "+b[3]+"")

    print("" + b[4] + "   |   " + b[5] + "   |   " + b[6] + "")

    print("" + b[7] + "   |   " + b[8] + "   |   " + b[9] + "")



#main program from here
p1=str(input('enter the name of the person1:\n'))
p2=str(input('enter the name of the person2:\n'))
c=randint(1,2)
print(c)
b=['']*10
t=[1,2,3,4,5,6,7,8,9,'']
board(b)
for i in range(9):
   if c == 1:
      print(t)
      print(p1)
      x=int(input('were u want to insert"choice from above list":\n'))
      if x not in t:
          print("{} already filled".format(x))
          continue
      t.remove(x)
      b[x]= 'x'
      board(b)
      win(b)
      c+=1
      continue
   elif c==2:
       print(t)
       print(p2)
       x=int(input('were u want to insert"choice from above list":\n'))
       if x not in t:
          print("{} already filled".format(x))
          continue
       t.remove(x)
       b[x]= 'o'
       board(b)
       win(b)
       c-=1
       continue



print('its draw  bro')





