import re
import sys

def extract_last_three_digits(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
        pattern = r'[a-zA-Z]\d[a-zA-Z]\d_(\d{3})'
        last_three_digits = re.findall(pattern, data)
        print(last_three_digits)

    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hw1_p12.py input.txt")
    else:
        input_file = sys.argv[1]
        extract_last_three_digits(input_file)
