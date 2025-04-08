import sys
import math


while True:
      sentence = str(sys.stdin.readline().strip())
      count = 0

      if sentence != '#':
            for item in sentence:
                  if item in ['a','e','i','o','u','A','E','I','O','U']:
                        count +=1

            print(count)


      
      else:
            break



