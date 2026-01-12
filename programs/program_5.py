def count_file_details(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
            
        with open(filename, "r") as file:
            text = file.read()
            lines = text.count("\n") + 1 if text else 0
            words = len(text.split())
            characters = len(text)
            
            print("Number of lines:", lines)
            print("Number of words:", words)
            print("Number of characters:", characters)
    except FileNotFoundError:
        print("File not found.")

filename = input("Enter file name: ")
content = """learning Python is fun
File handling is useful
Let's practice more. This is my program."""
count_file_details(filename, content)