# Word Counter - 21 Days Python Challenge (Project 5)

## Overview
This project is a simple **Text Analysis Tool** developed as part of the 21 Days Python Challenge. It allows users to analyze text input or text files to get insights such as word count, character count, line count, word frequency, and the most common words.

## Features
- **Clean Text:** Removes special characters and converts text to lowercase for accurate analysis.
- **Word Count:** Counts the total number of words in the text.
- **Character Count:** Counts characters with or without spaces.
- **Line Count:** Counts the number of lines in the text.
- **Word Frequency:** Shows how often each word appears.
- **Most Common Words:** Displays the top N most frequent words.
- **Input Options:**
  - Enter text manually
  - Read text from a file

## How to Use
1. **Run the Program:**
   ```bash
   python main.py
   ```
2. **Choose Input Method:**
   - Enter `1` to input text manually (type 'END' on a new line to finish input).
   - Enter `2` to analyze text from a file (provide the file path when prompted).
3. **View Results:**
   - The program will display line count, word count, character count (without spaces), word frequency, and the most common words.

## Example Output
```
Text Analysis Tool

Choose input method:
1. Analyze from text input
2. Analyze from text file

Enter choice (1 or 2): 1
Enter text (type 'END' on a new line to finish):
Hello world!
This is a test.
END

=== Text Analysis Results ===

Lines Count: 2
Words Count: 6
Characters Count (no spaces): 26
Words Frequency: Counter({'hello': 1, 'world': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1})

Most Common Words:
hello: 1
world: 1
this: 1
is: 1
a: 1
test: 1
```

## Requirements
- Python 3.x
- No external dependencies (uses only Python standard library)

## File Structure
- `main.py` - Main application file containing all logic

## License
This project is for educational purposes as part of the 21 Days Python Challenge.
