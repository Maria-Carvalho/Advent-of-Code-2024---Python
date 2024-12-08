def read_txt_file(file_path, as_lines=False):
    """
    Reads a text file and returns its contents either as a list of lines or a single string.
    If the file does not exist or an error occurs, prints an error message and returns an empty list or string.

    Args:
        file_path (str): The path to the text file.
        as_lines (bool): If True, returns the file content as a list of lines.
                        If False, returns the file content as a single string.

    Returns:
        list[str] or str: The lines of the file or the full content as a string depending on `as_lines`.
                          Returns an empty list or string if an error occurs.
    """
    try:
        with open(file_path, 'r') as file:
            if as_lines:
                return file.readlines()  # Read all lines into a list
            return file.read()  # Read the entire file content as a single string
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return [] if as_lines else ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return [] if as_lines else ""