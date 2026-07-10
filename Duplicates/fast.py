def duplicate_fast(list1):
    entry = set()

    for i in list1:
        if i in entry:
            return True
        entry.add(i)

    return False

numbers=[1,2,3,4,5]

result=duplicate_fast(numbers)

if result:
    print("Duplicate Found.")
else:
    print("No Duplicate Found.")