import re

cubes = {"red": 12, "green": 13, "blue": 14}

with open("day2input.txt") as f:
  input = f.readlines()

index = 1
input_dict = {}
for row in input:
  input_dict[index] = row[row.find(": ")+2:].strip().split(";")
  index+=1

def get_game_counts(list_of_peek_strings):
  output = []
  for peek_string in list_of_peek_strings:
    peek = {"red": 0, "green": 0, "blue": 0}
    if "red" in peek_string:
      count_red = re.search('(\d?\d)(?= red)', peek_string)
      peek['red'] = int(count_red.group(0))
    if "green" in peek_string:
      count_green = re.search('(\d?\d)(?= green)', peek_string)
      peek['green'] = int(count_green.group(0))
    if "blue" in peek_string:
      count_blue = re.search('(\d?\d)(?= blue)', peek_string)
      peek['blue'] = int(count_blue.group(0))
    output.append(peek)
  return output

for k,v in input_dict.items():
  input_dict[k] = get_game_counts(v)

part_1_sum = 0

for game_id,game_peek_list in input_dict.items():
  inner_count = 0
  for peek in game_peek_list:
    if peek['red'] > cubes['red'] or peek['green'] > cubes['green'] or peek['blue'] > cubes['blue']:
      break
    else:
      inner_count+=1
  if inner_count == len(game_peek_list):
    part_1_sum+=game_id
    
print(part_1_sum)

def get_power(game_peek_list):
  min_set = {"red": 0, "green": 0, "blue": 0}
  for peek in game_peek_list:
    if peek['red'] > min_set['red']:
      min_set['red'] = peek['red']
    if peek['green'] > min_set['green']:
      min_set['green'] = peek['green']
    if peek['blue'] > min_set['blue']:
      min_set['blue'] = peek['blue']
  power = min_set['red'] * min_set['green'] * min_set['blue']
  return power

part_2_sum = 0

for game_id,game_peek_list in input_dict.items():
  part_2_sum+=get_power(game_peek_list)

print(part_2_sum)
