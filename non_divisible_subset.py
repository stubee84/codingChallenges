def nonDivisibleSubset(k, s):
    sets = list()

    def check_number(num, numbers):
        for number in numbers:
            if (num+number)%k == 0:
                return False
            elif num == number:
                return False
        return True
    
    count=0
    while count<len(s):
        non_divisible = list()
        num = s.pop(0)
        non_divisible.append(num)
        for i in s:
            if (num+i) % k != 0:
                if check_number(i, non_divisible):
                    non_divisible.append(i)

        s.append(num)
        sets.append(non_divisible)
        count += 1
    
    return max([len(items) for items in sets])

if __name__ == "__main__":
    print(nonDivisibleSubset(4, [10,12,19,10,24,25,22]))
    print(nonDivisibleSubset(3, [1,2,4,7]))
    print(nonDivisibleSubset(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]))
    # with open('testcase.txt') as f:
    #     cases = f.readline()
    #     cases = cases.split(' ')

    # print(nonDivisibleSubset(50, [int(c) for c in cases]))