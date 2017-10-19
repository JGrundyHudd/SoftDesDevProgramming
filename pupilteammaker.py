number_of_pupils = int(input('Enter a number of pupils: '))
pupils_per_team = 5
print('From', number_of_pupils, 'pupils there can be', number_of_pupils // pupils_per_team, 'teams of 5')
print('and there will be', number_of_pupils % pupils_per_team, 'pupils left out')