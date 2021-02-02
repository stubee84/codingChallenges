def formingMagicSquare(s):
    d = dict()
    coords = dict()

    d['row1'] = sum(s[0])
    coords[(0,0)] = ['row1']
    coords[(0,1)] = ['row1']
    coords[(0,2)] = ['row1']
    d['row2'] = sum(s[1])
    coords[(1,0)] = ['row2']
    coords[(1,1)] = ['row2']
    coords[(1,2)] = ['row2']
    d['row3'] = sum(s[2])
    coords[(2,0)] = ['row3']
    coords[(2,1)] = ['row3']
    coords[(2,2)] = ['row3']

    d['col1'] = s[0][0] + s[1][0] + s[2][0]
    coords[(0,0)].append('col1')
    coords[(1,0)].append('col1')
    coords[(2,0)].append('col1')
    d['col2'] = s[0][1] + s[1][1] + s[2][1]
    coords[(0,1)].append('col2')
    coords[(1,1)].append('col2')
    coords[(2,1)].append('col2')
    d['col3'] = s[0][2] + s[1][2] + s[2][2]
    coords[(0,2)].append('col3')
    coords[(1,2)].append('col3')
    coords[(2,2)].append('col3')

    d['diag1'] = s[0][0] + s[1][1] + s[2][2]
    coords[(0,0)].append('diag1')
    coords[(1,1)].append('diag1')
    coords[(2,2)].append('diag1')
    d['diag2'] = s[0][2] + s[1][1] + s[2][0]
    coords[(0,2)].append('diag2')
    coords[(1,1)].append('diag2')
    coords[(2,0)].append('diag2')

    max_value = max([d['row1'], d['row2'], d['row3'], d['col1'], d['col2'], d['col3'], d['diag1'], d['diag2']])

    equal_max = list()
    below_max = list()
    for k,v in d.items():
        if v < max_value:
            below_max.append(k)
        else:
            equal_max.append(k)

    print(below_max)
    print(equal_max)

if __name__ == "__main__":
    square = [
        [4,9,2],
        [3,5,7],
        [8,1,6]]

    formingMagicSquare(s=square)