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


def report_is_safe(report):
  """
  Determines whether a report is considered safe based on specific conditions:
    1. Levels must either be all increasing or all decreasing.
    2. Any two adjacent levels must differ by at least 1 and at most 3.

  Args:
    report (list[int]): A list of integer levels from the report.
  Returns:
    bool: True if the report is safe, False otherwise.
  """
  prevReportOrientation = 1 if report[0] < report[1] else 0

  for i in range(1, len(report) - 1):
    currentReportOrientation = 1 if report[i] < report[i + 1] else 0
    
    if not (0 < abs(report[i] - report[i + 1]) < 4) or not (0 < abs(report[i] - report[i - 1]) < 4):
      break

    if currentReportOrientation != prevReportOrientation:
      break

    prevReportOrientation = currentReportOrientation
  else:
    return True

  return False


def count_safe_reports(reports):
  """
  Counts the number of safe reports from a list of reports. Each report contains levels as space-separated strings.

  Args:
    reports (list[str]): A list of strings, where each string represents a report with space-separated levels.

  Returns:
    int: The count of safe reports.
  """
  count_safe = 0
  for report in reports:
    reportByLevels = report.split()
    reportByLevels = [(lambda x: int(x.strip()))(lvl) for lvl in reportByLevels]
    if report_is_safe(reportByLevels):
      count_safe += 1

  return count_safe

def main():
  print("Red-Nosed Reports")
  file_name = input("Enter the name of the txt file (default: input.txt): ") or "input.txt"
  content_txt = read_txt_file(file_name)
  
  if content_txt:
    print(f"Reports safe: {count_safe_reports(content_txt)}")
    print(f"Reports safe with dampener:  ") #TODO
  

if __name__ == "__main__":
  main()