number_of_pupils = int(input('Enter a number of pupils: '))
pupils_per_team = 5
if number_of_pupils > 0:
    print('From', number_of_pupils, 'pupils there can be', number_of_pupils // pupils_per_team, 'teams of 5')
    print('and there will be', number_of_pupils % pupils_per_team, 'pupils left out')
elif number_of_pupils == 0:
    print('Input value not valid: No teams can be created with 0 students')
else:
    print('Input value not valid: a negative number of pupils is not possible')
