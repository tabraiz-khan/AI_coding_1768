# generate some keywords for suspicious spam emails
import random
def generate_spam_keywords(num_keywords=16):
    spam_keywords = [
        "free", "winner", "cash", "prize", "urgent", "offer",
        "click", "buy now", "limited time", "guaranteed",
        "act now", "exclusive", "risk-free", "bonus", "cheap","Congrat"
    ]
    return spam_keywords

# classify an text as suspicious spam email or not
def is_spam_email(email_content, spam_keywords):
    email_content_lower = email_content.lower()
    for keyword in spam_keywords:
        keyword=keyword.lower()
        if keyword in email_content_lower:
            return True
    return False
# Example usage
spam_keywords = generate_spam_keywords()    
print("Generated Spam Keywords:", spam_keywords)
email_content = "congratulations! You have been shortlisted for interview, it is scheduled on first of january."
if is_spam_email(email_content, spam_keywords): 
    print("This email is classified as spam.")
else:
    print("This email is not classified as spam.")

''' 1. take marks as integer between 0 to 100
    2. if marks>40 then print pass
    3. if marks<40 then print fail'''
def check_pass_fail(marks):
    if 0 <= marks <= 100:
        if marks >= 40:
            return "Pass"
        else:
            return "Fail"
    else:
        return "Invalid marks. Please enter a number between 0 and 100."
#take age 
# if age>=18 then print eligible for voting
# if age<18 then print not eligible for voting
def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible for voting"
    else:
        return "Not eligible for voting"

# Generate a list of student names with some palindromic names
student_names = ["Anna", "Bob", "Cathy", "David", "Eve", "Hannah", "Ian", "Otto", "Paul"]
# if the name is palindrome then print it
def find_palindromic_names(names):
    palindromic_names = []
    for name in names:
        if name.lower() == name[::-1].lower():
            palindromic_names.append(name)
    return palindromic_names
palindromic_names = find_palindromic_names(student_names)
print("Palindromic Names:", palindromic_names)

#generate a list of words
words = ["level", "world", "radar", "python", "madam", "java", "civic", "code"]
# for each word , calculate its length 
def calculate_word_lengths(word_list):
    word_lengths = {}
    for word in word_list:
        word_lengths[word] = len(word)
    return word_lengths
# if length is less than 5 the word is short else long
word_lengths = calculate_word_lengths(words)
for word, length in word_lengths.items():
    if length < 5:
        print(f"{word} is a short word.")
    else:
        print(f"{word} is a long word.")




