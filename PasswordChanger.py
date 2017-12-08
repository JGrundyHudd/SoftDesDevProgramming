disallowed_passwords = ['Password', 'password', 'sesame', 'Sesame', 'Letmein', 'LetMeIn', 'Qwerty', 'Cheese']
password_entry_one = input('Please enter your new password. It should be between 6 and 12 characters long:')
if 5 < len(password_entry_one) < 13 and password_entry_one not in disallowed_passwords:
    password_entry_two = input('Please enter your new password again:')
    if password_entry_one == password_entry_two:
        print('Password Changed')
    else:
        print('The two passwords you entered did not match, password change failed')
elif 5 < len(password_entry_one) < 13:
    print('The password you entered is not allowed, you must choose a more distinct password')
else:
    print('The password you entered is not between 6 and 12 characters, password change failed')
