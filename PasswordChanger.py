disallowed_passwords = ['Password', 'password', 'sesame', 'Sesame', 'Letmein', 'LetMeIn', 'Qwerty', 'Cheese']
password_entry_one = input('Please enter your new password. It should be between 6 and 12 characters long:')
if 5<len(password_entry_one)>13 and password_entry_one not in disallowed_passwords:
    password_entry_two = input('Please enter your new password again:')

