def validYear(prompt='Input a valid year: '):
    while True:
        try:
            year = int(input(prompt))
            if not year:
                raise ValueError
            elif year < 1915 or year > 2014:
                raise ValueError
            else:
                return year
        except (ValueError, TypeError):
            print('Please input a valid year between 1915 and 2014')


def validGender(prompt='Input gender (M or F): '):
    while True:
        try:
            gender = input(prompt).upper()
            if(gender == 'M' or gender == 'F'):
                return gender
            else:
                raise ValueError
        except (TypeError, ValueError):
            print('Invalid input, input M or F')
    