#https://www.hackerrank.com/challenges/capitalize/problem
def solve(s):
   words = list(s.split(' '))
   capitalized = list()

   for word in words:
      if len(word) != 0:
         word_c = word.capitalize()
         capitalized.append(word_c + ' ')
      else:
         capitalized.append(' ')
   
   final_s = ''.join(capitalized)
   return final_s

nombre = 'hello   world  lol'

print(solve(nombre))