#do replace all on words in input file: 5838218 798
import re

with open("input.txt") as f:
  input = f.readlines()

input_dict = {}
i = 0
for line in input:
  #replace the regex with "(\d)" for part 1
  digits = re.findall("(one|two|three|four|five|six|seven|eight|nine|\d)", line)
  input_dict[i] = (digits[0], digits[len(digits)-1])
  i+=1

def map_word(val):
  if val == 'one':
    return '1'
  elif val == 'two':
    return '2'
  elif val == 'three':
    return '3'
  elif val == 'four':
    return '4'
  elif val == 'five':
    return '5'
  elif val == 'six':
    return '6'
  elif val == 'seven':
    return '7'
  elif val == 'eight':
    return '8'
  elif val == 'nine':
    return '9'
  else:
    return val

sum = 0
for k,v in input_dict.items():
  n = int(map_word(v[0]) + map_word(v[1]))
  sum+=n

print(sum)
