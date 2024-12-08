import re
from common.text_utils import read_txt_file

def sum_all_valid_multiplications(content_txt):
  """
  Extracts all valid operations from the given text. 
  A valid operation is defined as one of the following patterns:
    - mul(number,number): A multiplication operation with two numbers.
    - do(): A command to resume multiplication operations.
    - don't(): A command to pause multiplication operations.

  Calculates the total sum of all valid multiplication operations found.
  Handles special commands:
    - "do()": Resumes multiplications after a "don't()" command. 
    - "don't()": Pauses multiplication until a "do()" command is encountered.
    
  Args:
    content_txt (str): The content as a single string.
    
  Returns:
    int: The total sum of all valid multiplications.
  """
  # For part 1 the regex used was r"mul\([0-9]+,[0-9]+\)"
  all_operations = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", content_txt)

  total = 0
  dont = False
  
  for operation in all_operations:
    if operation == "do()":
      dont = False
      continue

    if not dont:
      if operation == "don't()":
        dont = True
        continue

      # Extract numbers from the multiplication operation and compute the product
      if operation.startswith("mul("):
        numbers = operation[4:-1].split(",")
        total += int(numbers[0]) * int(numbers[1])
  
  return total    

def main():
  print("Mull It Over")
  file_name = input("Enter the name of the txt file (default: input.txt): ") or "input.txt"
  content_txt = read_txt_file(file_name)
  
  if content_txt:
    print(f"Total: {sum_all_valid_multiplications(content_txt)}")

if __name__ == "__main__":
  main()