def count_characters(filename, content):
    vowels = "AEIOUaeiou"
    vowel_count = consonant_count = uppercase_count = lowercase_count = 0
    
    try:
        with open(filename, "w") as file:
            file.write(content)
            
        with open(filename, "r") as file:
            text = file.read()
            for char in text:
                if char.isalpha():
                    if char in vowels:
                        vowel_count += 1
                    else:
                        consonant_count += 1
                    if char.isupper():
                        uppercase_count += 1
                    else:
                        lowercase_count += 1
        print("Vowels:", vowel_count)
        print("Consonants:", consonant_count)
        print("Uppercase:", uppercase_count)
        print("Lowercase:", lowercase_count)
    except FileNotFoundError:
        print("File not found.")

filename = input("Enter file name: ")
content = input("Enter the content to write in the file: ")
count_characters(filename, content)