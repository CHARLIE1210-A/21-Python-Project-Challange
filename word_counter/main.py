import re
from collections import Counter

# ================= TEXT PROCESSING =================
def clean_text(text):
    """
    Cleans the input text by removing special characters and converting to lowercse.
    - Lowercase the text
    - Remove special charcaters
    """
    
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    
    return text

def count_words(text):
    """
    Count the frequency of each word in the input text.
    - Split the text into words
    - Use Counter to count word frequencies
    """
    
    words = text.split()
    return len(words)

def count_characters(text, include_spaces=True):
    """
    Count the number of characters in the input text.
    """
    if include_spaces:
        return len(text)
    
    return len(text.replace(" ", ""))

def count_lines(text):
    """ 
    Count the number of lines in the input text.
    """
    lines = text.splitlines()
    return len(lines)

def word_frequency(text):
    """
    Calculate the freuency of each word in the input text.
    """
    words = text.split()
    return Counter(words)

def most_common_words(text, n=5):
    freq = word_frequency(text)
    return freq.most_common(n)


# ================= INPUT HANDLING =================
def read_from_file(file_path):
    """
    Read text from a file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def read_from_input():
    """
    Read text from sandard input.
    """
    print("Enter text (type 'END' on a new line to finish): ")
    lines = []
    
    while True:
        line = input()
        if line.strip() == 'END':
            break
        lines.append(line)
        
    return "\n".join(lines)

# ================= DISPLAY =================
def display_results(text):
    clean = clean_text(text)
    
    print("\n=== Text Analysis Results ===")
    print(f"\nLines Count: {count_lines(text)}")
    print(f"Words Count: {count_words(text)}")
    print(f"Characters Count (no spaces): {count_characters(text, include_spaces=False)}")
    print(f"Words Frequency: {word_frequency(clean)}")
    
    print("\nMost Common Words: ")
    for word, freq in most_common_words(clean):
        print(f"{word}: {freq}")
        
# ================= MAIN APP =================
def main():
    print("Text Analysis Tool")
    print("\nChoose input method:")
    print("1. Analyze from text input")
    print("2. Analyze from text file")
    
    choice = input("\nEnter choice (1 or 2): ")
    
    try:
        if choice == "1":
            text = read_from_input()
        elif choice == "2":
            path = input("Enter file path: ")
            text = read_from_file(path)
        else:
            print("Invalid choice. Existing.")
            return
        
        display_results(text)
    except Exception as e:
        print(f"Error reading input: {e}")
        
if __name__ == "__main__":
    main()