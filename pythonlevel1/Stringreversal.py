def reverse_string(user_input):
    user_input = user_input.strip()
    
    if user_input == "":
        return "No input given"
    
    reversed_text = user_input[::-1]
    return reversed_text

word = input("Enter text to reverse: ")
print("Output:", reverse_string(word))
