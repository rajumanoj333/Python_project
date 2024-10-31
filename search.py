import re

class Search:
    """
    Handles file reading, cleaning, and searching for a word or pattern.
    """
    def __init__(self, filename):
        self.lines = []
        try:
           with open(filename, 'r') as file:
               self.lines = list(file)
        except FileNotFoundError as fnf:
            print("Error: File Does Not Exist")
        except Exception as e:
            print(f'Error: {e}')

    def clean(self):
        """
        Clean lines by removing punctuation and newline characters.
        """
        self.lines = [re.sub(r'[^\w\s]+|\n', '', line)for line in self.lines]

    def get_lines(self, word_or_pattern):
        """
        Search for the word or pattern in cleaned lines and return matching lines.
        """
        result = [word_or_pattern]
        self.clean()

        for i, line in enumerate(self.lines):
            if word_or_pattern in line:
                result.append((i + 1, line.strip()))
        return result
