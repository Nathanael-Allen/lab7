from Name import Name
from Database import Database

def main():
    data = Database.readNames(1960, 'M')
    print(data)
    # names = Name.showNames()
    print('YEAR | NAME | GENDER | COUNT')
    print('-' * 30)

    for name in data:
        print(f'{name.getYear()} | {name.getName()} | {name.getGender()}      | {name.getCount()}')
        print('-' * 30)


if __name__ == '__main__':
    main()