def task01(st):
    res = []
    for i, char in enumerate(st):
        res.append(char.upper() + char.lower() * i)
    return '-'.join(res)


if __name__ == "__main__":
    print('\n')
    print(task01('abcd'))
    print(task01('RqaEzty'))
    print(task01('cwAt'))
    print(task01('ZpglnRxqenU'))
    print(task01('EquhxOswchE'))
