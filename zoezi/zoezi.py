# def add(num1, num2, num3):
#     return num1+num2+num3
# print(add(1,2,3))

# names = ["Dann","Christopher","Dorothy","Stephen"]
# for name in names:
#     print(name)

# d = [student for student in names if student.startswith('D')]
# print(d)
# print(names)

def alphaToDigit(A):
    result = []
    for alpha in A:
        if alpha.isalpha():
            alp = ord(alpha.lower()) - ord('a') + 1

            result.append(str(alp))

    return ' '.join(result)

# A = 'Hello world'
print(alphaToDigit('Hello world'))