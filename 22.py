def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)

# Example usage
read_file('filename.txt')

def read_first_n_lines(filename, n):
    with open(filename, 'r') as file:
        for i in range(n):
            line = file.readline()
            print(line)

# Example usage
read_first_n_lines('filename.txt', 5)

def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()
        start_line = max(0, len(lines) - n)
        for line in lines[start_line:]:
            print(line)

# Example usage
read_last_n_lines('filename.txt', 5)

def count_words(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        words = contents.split()
        return len(words)

# Example usage
num_words = count_words('filename.txt')
print("Number of words:", num_words)


import os

def read_last_n_lines(filename, n):
    with open(filename, 'rb') as file:
        file.seek(-2, os.SEEK_END)
        lines = []
        while len(lines) < n:
            try:
                while file.read(1) != b'\n':
                    file.seek(-2, os.SEEK_CUR)
            except OSError:
                file.seek(0)
                break
            lines.insert(0, file.readline().decode().strip())
    for line in lines:
        print(line)

# Example usage
read_last_n_lines('filename.txt', 5)