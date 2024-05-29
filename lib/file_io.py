def write_file(file_path, content):
    with open(f'{file_path}.txt', 'w') as f:
        f.write(content)

def append_file(file_path, content):
    with open(f'{file_path}.txt', 'a') as f: 
        f.write(content)

def read_file(file_path):
    with open(f'{file_path}.txt', 'r') as f:
        return f.read()
