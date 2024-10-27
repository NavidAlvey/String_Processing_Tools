import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def edit_distance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    #2D array stores edit distance between prefixes
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Initialize base cases
    for i in range(len1 + 1):
        # Deleting all characters from str1
        dp[i][0] = i 
    for j in range(len2 + 1):
        # Inserting all characters into str1
        dp[0][j] = j

    # Fill in dp array
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Characters match, no operation needed
            else:
                dp[i][j] = min(dp[i - 1][j], # Deletion
                               dp[i][j - 1], # Insertion
                               dp[i - 1][j - 1]) + 1  # Substitution

    return dp[len1][len2]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python hw1_p31.py input1.txt input2.txt")
        sys.exit(1)

    # Read input file strings
    input1_path = sys.argv[1]
    input2_path = sys.argv[2]

    string1 = read_file(input1_path)
    string2 = read_file(input2_path)

    # Calculate edit distance between two strings
    result = edit_distance(string1, string2)

    # Print the result
    print(result)
