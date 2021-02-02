from typing import List, Dict, Tuple

def pig_latin(message: str):
    msg = ''
    values = message.split(' ')
    for value in values:
        if '-' in value:
            vals = value.split('-')
            val = vals[1].split('ay')[0]+vals[0]
        elif 'yay' in value and '-' not in value:
            val = value.split('yay')[0]
        msg += val + ' '
    print(msg.rstrip(' '))


def pickingNumbers(a):
    count = 0
    sets = list()
    
    def checkNumber(i, nums):
        for num in nums:
            if abs(num-i) > 1:
                return False

        return True

    while count < len(a):
        l = list()
        num = a.pop(0)
        l.append(num)
        for i in a:
            if abs(num-i) <= 1:
                if checkNumber(i, l):
                    l.append(i)
        
        a.append(num)
        sets.append(l)
        count += 1

    return max([len(s) for s in sets])

def acmTeam(topic):
    count = 0
    topic_length = len(topic)
    max_value = 0
    team_count=0
    while count < topic_length:
        t = topic.pop(0)

        if len(topic) == 0:
            break
        for item in topic:
            value = 0
            for i in range(t):
                if (int(t[i]) | int(item[i])) > 0:
                    value += 1
            if max_value < value:
                max_value = value
                team_count = 1
            elif max_value == value:
                team_count += 1
                
        count += 1
    
    return max_value, team_count

def formingMagicSquare(s: List[List[int]]):
    coords: Dict[Tuple[Tuple[int]]] = {
        0: ((0,0),(0,1),(0,2)),
        1: ((1,0),(1,1),(1,2)),
        2: ((2,0),(2,1),(2,2)),
        3: ((0,0),(1,0),(2,0)),
        4: ((0,1),(1,1),(2,1)),
        5: ((0,2),(1,2),(2,2)),
        6: ((0,0),(1,1),(2,2)),
        7: ((0,2),(1,1),(2,0))
    }

    effect_multipler: Dict[Tuple[Tuple[int]]] = {
        2: ((0,1),(1,0),(1,2),(2,1)),
        3: ((0,0),(0,2),(2,0),(2,2)),
        4: ((1,1))
    }

    def get_coord_totals(coordinates: dict, value: int=0, coord: Tuple[int] = None) -> list:
        totals = list()
        for v in coordinates.values():
            total = 0
            for i in range(len(v)):
                prev = 0
                for j, val in enumerate(v[i]):
                    if j == 0:
                        prev = val
                        continue
                    total += s[prev][val]

            totals.append(total)
            total = 0
        return totals
        

    coord_totals: list = get_coord_totals(coordinates=coords)
    sum_total: int = sum(coord_totals)
    diff: int = len(coords)-(sum_total%len(coords))

    next_magic = int((sum_total+diff)/8)
    diffs: list = [next_magic-coord for coord in coord_totals]
    
    while True:
        for i, d in enumerate(diffs):
            get_coord_totals(coordinates=coords, value=d, coord=coords[i][0])
    
    # print(sum_total%len(coords))
    return coord_totals

if __name__ == "__main__":
    # pig_latin("idden-hay essage-may")
    # pickingNumbers([1,2,2,3,1,2])
    # pickingNumbers([4,6,5,3,3,1])
    # pickingNumbers([1,1,2,2,4,4,5,5,5])
    # pickingNumbers([14,18,17,10,9,20,4,13,19,19,8,15,15,17,6,5,15,12,18,2,18,7,20,8,2,8,11,2,16,2,12,9,3,6,9,9,13,7,4,6,19,7,2,4,3,4,14,3,4,9,17,9,4,20,10,16,12,1,16,4,15,15,9,13,6,3,8,4,7,14,16,18,20,11,20,14,20,12,15,4,5,10,10,20,11,18,5,20,13,4,18,1,14,3,20,19,14,2,5,13])

    formingMagicSquare(s=[[4,8,2],[4,5,7],[6,1,6]])
    # formingMagicSquare(s=[[4,9,2],[3,5,7],[8,1,6]])
    formingMagicSquare(s= [[5, 3, 4], [1, 5, 8], [6, 4, 2]])
    # formingMagicSquare(s= [[8, 3, 4], [1, 5, 9], [6, 7, 2]])
    formingMagicSquare(s= [[4,9,2],[3,5,7],[8,1,5]])
    # formingMagicSquare(s= [[4,9,2],[3,5,7],[8,1,6]])
    