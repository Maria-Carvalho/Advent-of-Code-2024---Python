def read_txt_file(file_path):
  """
  Reads a text file and returns its contents as a list of lines.
  If the file does not exist or an error occurs, prints an error message and returns an empty list.

  Args:
    file_path (str): The path to the text file.

  Returns:
    list[str]: A list containing the lines of the file, or an empty list if an error occurs.
  """
  try:
    with open(file_path, 'r') as file:
      return file.readlines()  # Read all lines into a list
  except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    return []
  except Exception as e:
    print(f"An error occurred: {e}")
    return []


def process_txt(content):
  """
  Processes the content of a text file and extracts two lists of integers.
  Each line is split into two parts, and the integers are appended to respective lists.

  Args:
    content (list[str]): A list of strings where each string is a line of the text file.

  Returns:
    tuple[list[int], list[int]]: Two lists of integers, extracted from the text content.
  """
  left_list = []
  right_list = []

  for line in content:
    line_split = line.split()
    left_list.append(int(line_split[0].strip()))
    right_list.append(int(line_split[1].strip()))
  return left_list, right_list


def calculate_distance(left_list, right_list):
  """
  Calculates the total distance between the values in the left list and the right list.
  Both lists are sorted, and the distance is computed as the sum of the absolute differences 
  between corresponding values in the sorted left and right lists.

  Args:
    left_list (list[int]): The first list of integers.
    right_list (list[int]): The second list of integers.

  Returns:
    int: The total distance between the sorted values of the left and right lists.
  """
  total_distance = 0

  for leftVal, right_val in zip(sorted(left_list), sorted(right_list)):
    total_distance += abs(leftVal - right_val)

  return total_distance


def calculate_similarity_score(left_list, right_list):
  """
  Calculates a similarity score by summing the product of each number in the left list and the number of times 
  it appears in the right list.

  Args:
    left_list (list[int]): The first list of integers.
    right_list (list[int]): The second list of integers.

  Returns:
    int: The calculated similarity score.
  """
  similarity_score = 0

  for left_value in left_list:
    similarity_score += right_list.count(left_value) * left_value

  return similarity_score


def main():
  # Your main program logic here
  file_name = input("Enter the name of the txt file (default: input.txt): ") or "input.txt"
  content_txt = read_txt_file(file_name)
  if content_txt:
    left_list, right_list = process_txt(content_txt)
  print(f"Distance: {calculate_distance(left_list, right_list)}")
  print(f"Similarity score: {calculate_similarity_score(left_list, right_list)}")

if __name__ == "__main__":
  main()