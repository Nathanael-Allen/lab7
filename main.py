from Name import Name
from Database import Database
from valid import validYear, validGender

def main():
    year = validYear('Input a year between 1914 and 2014: ')
    gender = validGender('Input gender (M/F): ')
    data = Name.showNames(year, gender)
    print('YEAR | NAME | GENDER | COUNT')
    print('-' * 30)

    for name in data:
        print(f'{name.getYear()} | {name.getName()} | {name.getGender()}      | {name.getCount()}')
        print('-' * 30)


if __name__ == '__main__':
    main()