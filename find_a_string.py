#https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    count_substring = 0
    for i in range(len(string)):
        if(string[i:i+len(sub_string)] == sub_string):
            count_substring+=1
        
    return count_substring