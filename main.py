from Name import Name

def main():
    names = Name.showNames()
    print('YEAR | NAME | GENDER | COUNT')
    print('-' * 30)

    for name in names:
        print(f'{name.getYear()} | {name.getName()} | {name.getGender()}      | {name.getCount()}')
        print('-' * 30)


if __name__ == '__main__':
    main()