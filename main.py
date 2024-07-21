from Name import Name
from Database import Database
from valid import validYear, validGender

def main():
    print("""
______________________________________________________________________________________
Welcome, this program accesses a database of the most popular names by year and gender.
To show the top 20 most common names per year, input a year and a gender...
______________________________________________________________________________________
""")
    year = validYear('Input a year between 1914 and 2014: ')
    gender = validGender('Input gender (M/F): ')
    data = Name.showNames(year, gender)
    print(f'\nHere is the most popular {gender} names from {year}:')
    print(f'YEAR{" " * 4}NAME{" " * 30}GENDER{" " * 8}COUNT')
    print('_' * 62)

    for name in data:
        print(f'{name.getYear()}{" " * 4}{name.getName()}{" " * (36 - len(name.getName()))}{name.getGender()}{" " * 11}{name.getCount()}')


if __name__ == '__main__':
    main()