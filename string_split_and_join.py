def split_and_join(line):
   words = line.split(' ')
   new_line = '-'.join(words)
   return new_line

if __name__ == '__main__':
   line = input()
   result = split_and_join(line)
   print(result) 