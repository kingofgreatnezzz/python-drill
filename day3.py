#NO1. slicing, indexing
s = "Python Language"
print(s[0]) #First letter
print(s[-1]) #Last letter
print(s[::-1]) # walk backward to the top
print(s[::3]) # hop over every other by step 3

#[::] inside square bracket [start : stop : step]
print(s[2:10]) # print from 2 to 10[start: stop]

#NO2.  Count vowels using SUM()
text = "mi-lla m o-Alex"
vowels = sum(1 for char in text.lower() if char in "aeiou") #.lower() so that the capital letter still matches the check 
print(vowels)


# Note STRING MANIPULATION
print(text.split("-")) # .split() turns a sentence into a list
print("--".join(text)) # glues a list of words to one big string using whatever you added in front
print(text.strip()) # 
print(text.replace('m','n')) # replaces a letter with another

#changing cases 
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

# searching & counting
print(text.count("a")) # counts a letter in a text
print(text.find("e")) # finds a letters index number
print(text.startswith("Mi")) # a boolean respons if a  text starts with a letter
print(text.endswith("py"))

print("# checking ID (True/False)")
print(text.isalnum()) # is all characters letters or numbers ?  
print(text.isdigit()) # 
print(' '.isspace()) # is it nothing but empty space?
print(text.isalpha()) # is it all alphabet?

print(f"dijiste {text}")

#NO3. palindrome check
phrase= 'A man, a plan, a canal: Panama'
print(phrase.split(" "))
print("--".join(phrase))

#NO4. word frequency
counts = {}
for word in ["hi", "hi", "bye"]:
    counts[word] = counts.get(word, 0) +1
    
# NO5 Regex
import re
# \d+ means "one digits and more"
nums = re.findall(r"\d+", "Order 43 costs 400003")
print(nums)

#NO6 string masking
secret =  "9329434"
mask = "*" * (len(secret) - 3) + secret[-3:]
print(len(secret))
print(mask)
