# roman number to integer

nums = []
def romanToInt(roman):
    
    sum = 0
    for letter in roman:
        if letter is '':
            nums.append(0)
        elif letter is 'I' or letter is 'i':
            nums.append(1)
        elif letter is 'V' or letter is 'v':
            nums.append(5)
        elif letter is 'X' or letter is 'x':
            nums.append(10)
        elif letter is 'L' or letter is'l':
            nums.append(50)
        elif letter is 'C' or letter is 'c':
            nums.append(100)
        elif letter is 'D' or letter is 'd':
            nums.append(500)
        elif letter is 'M' or letter is 'm':
            nums.append(1000)
        else:
            print('Please input a correct roman number!')
            raise TypeError
    '''
    倒序查看，指针从倒数第二个数字开始查找
    如果当前数字小于后一个数字
    则当前数字取负
    '''
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            nums[i] = nums[i]*(-1)

    for i in nums:
        sum = sum + i

    return sum

print(romanToInt('CMXCIX'))

# integer to roman number



# def integerToList(integer):
#     代码优化
#     '''将数字转换为列表形式
#     '''
#     numList = []
#     list_number_one = integer // 1000
#     numList.append(list_number_one)
#     list_number_two = (integer % 1000) // 100
#     numList.append(list_number_two)
#     list_number_three = ((integer % 1000) % 100) // 10
#     numList.append(list_number_three)
#     list_number_four = ((integer % 1000) % 100) % 10
#     numList.append(list_number_four)
#     return numList


def integerToRoman(integer):
    '''
    将数字列表转换为罗马数字
    '''
    numList = [integer // 1000,
                (integer % 1000) // 100,
                ((integer % 1000) % 100) // 10,
                ((integer % 1000) % 100) % 10]
    roman = ''
    # numList = integerToList(integer)
    one = 'M' * numList[0]
    two = 'CM' * (numList[1] // 9) + 'D' * ((numList[1] % 9) // 5) + 'CD' * (((numList[1] % 9) % 5) // 4) + 'C' * (((numList[1] % 9) % 5) % 4)
    three = 'XC' * (numList[2] // 9) +  'L' * ((numList[2] % 9) // 5) + 'XL' * (((numList[2] % 9) % 5) // 4) + 'X' * (((numList[2] % 9) % 5) % 4)
    four = 'IX' * (numList[3] // 9) + 'V' * ((numList[3] % 9)  // 5) + 'IV' * (((numList[3] % 9) % 5) // 4) + 'I' * (((numList[3] % 9) % 5) % 4)
    roman = roman.join(one + two + three + four)
    return roman

print(integerToRoman(99))
