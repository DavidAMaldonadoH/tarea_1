n = int(input())
nums = {}

for i in range(n):
   x = input()
   nums[x] = 'None'

def repeat(string):
   valid = True
   k = len(string)-3
   for i in range(k):
      if string[i:i+4] == string[i]*4:
         valid = False
   return valid

def validate(dict, key):
   if key.isdigit():
      if key[0] == '4' or key[0] == '5' or key[0] == '6':
         if repeat(key):
            dict[key] = 'Valid'
         else:
            dict[key] = 'Invalid'
      else:
            dict[key] = 'Invalid'
   elif any([c == '-' for c in key]):
         cards = key.split('-')
         card_num = key.replace('-', '')
         if all([len(item) == 4 for item in cards]):
            if card_num.isdigit():
               if key[0] == '4' or key[0] == '5' or key[0] == '6':
                  if repeat(card_num):
                     dict[key] = 'Valid'
                  else:
                     dict[key] = 'Invalid'
               else:
                  dict[key] = 'Invalid'
         else:
            dict[key] = 'Invalid'
   else:
      dict[key] = 'Invalid'

for key, num in nums.items():
   if len(key) == 16:
      validate(nums, key)  
   elif len(key) == 19:
      validate(nums, key)
   else:
      nums[key] = 'Invalid'

for key, num in nums.items():
   print(num)
