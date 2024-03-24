#1
def grades(di):
    result = 0
    for name, grades in di.items():
        if grades >= 60:
            result += 1
    return result

#2
def grades_2(di):
    result = []
    for name, grades in di.items():
        if grades >= 60:
            result.append(name)
    return result

#3
def grades_3(di):
    for name, grades in di.copy().items():
        if grades <= 60:
            del di[name]
    return di

#4
def reverse(di):
    result = {}
    for name, grades in di.items():
        result[grades] = name
    return result
