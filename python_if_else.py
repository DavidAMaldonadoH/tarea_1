if __name__ == '__main__':

     n = int(input().strip())
     if n%2==1:
          print('Weird')
     elif n>20:
          if n%2==0:
               print('Not Weird')
          else:
               print('Weird')
     elif (n in range(6, 21)):
          if n%2==0:
               print('Weird')
          else:
               print('Not Weird')
     elif (n in range(2, 6)):
          if n%2==0:
               print('Not Weird')
          else:
               print('Weird')
     else:
        print('Weird')

