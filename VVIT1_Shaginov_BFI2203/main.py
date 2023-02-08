from mygroup import groupmates

def filter(middle):
    for i in groupmates:
        if (sum(i["marks"]) / 3) > middle:
            print(i["name"], i["surname"])


middle = float(input())

filter(middle)
