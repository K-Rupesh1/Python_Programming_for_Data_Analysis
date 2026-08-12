def is_password_strong(password):
    if len(password)<8:
        return False
    if not any(char.isdigit()  for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any (char in '!@#$%^&*()_+-' for char in password):
        return False
    else:
        return True
print(is_password_strong('rupesh'))
print(is_password_strong('Rupesh1!'))