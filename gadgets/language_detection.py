from langdetect import detect

text = input("Enter text to detect language: ")

language = detect(text)

print(f"The detected language is: {language}")