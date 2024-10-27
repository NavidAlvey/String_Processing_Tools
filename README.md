# String Processing Tools

## Description

### Pattern Extraction with `extract_three_digit_patterns.py`

- Reads text data from a specified file to identify and extract sequences of three digits following a unique pattern.
- Uses regular expressions to search for patterns formatted as `[letter][digit][letter][digit]_[three digits]`.
- Outputs all matching three-digit sequences found within the text file.

### Edit Distance Calculation with `string_edit_distance.py`

- Calculates the edit distance (Levenshtein distance) between strings in two separate text files.
- Initializes a 2D matrix to store minimum operations between prefixes of each string, allowing insertion, deletion, and substitution operations.
- Outputs the final edit distance, representing the minimum number of edits required to transform one string into the other.

## Project Structure

- **`extract_three_digit_patterns.py`**: Script for identifying and extracting specific three-digit patterns within a text file.
- **`string_edit_distance.py`**: Script to compute the edit distance between two input strings, useful for measuring string similarity.
- **`input.txt` and `input2.txt`**: Sample text files used for testing and demonstration of the scripts.

## Requirements

The scripts require Python 3.x and the following Python packages:

- `re` (built-in)
- `sys` (built-in)

No additional installations are necessary.

## Usage

### Pattern Extraction

Run `extract_three_digit_patterns.py` to extract specific three-digit patterns from a file:

```bash
python extract_three_digit_patterns.py input.txt
