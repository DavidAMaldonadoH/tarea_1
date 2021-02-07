#https://www.hackerrank.com/challenges/string-validators/problem
if __name__ == '__main__':

   s = input()

   char = False
   letters = False
   nums = False
   lower = False
   upper = False

   if any([c.isalnum() for c in s]):
      char = True
   
   if any([c.islapha() for c in s]):
      letters = True

   if any([c.isdigit() for c in s]):
      nums = True

   if any([c.islower() for c in s]):
      lower = True
   
   if any([c.isupper() for c in s]):
      upper = True

   print(char)
   print(letters)
   print(nums)
   print(lower)
   print(upper)
   