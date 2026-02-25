# Simple Email Validator Program

def is_valid_email(email):

    # check if '@' exists and only one '@'
    if email.count("@") != 1:
        return False

    # split local part and domain part
    parts = email.split("@")
    local_part = parts[0]
    domain_part = parts[1]

    # local and domain should not be empty
    if local_part == "" or domain_part == "":
        return False

    # domain must contain at least one dot
    if "." not in domain_part:
        return False

    # dot should not be first or last in domain
    if domain_part.startswith(".") or domain_part.endswith("."):
        return False

    return True


# Taking input from user
user_email = input("Enter an email address: ")

if is_valid_email(user_email):
    print("Valid email address.")
else:
    print("Invalid email address.")