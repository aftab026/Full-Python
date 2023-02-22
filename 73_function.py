def percent(marks):
    a = (sum(marks)/400)*100
    return a

marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks2 = [34, 75, 88, 45]
percentage2 = percent(marks2)

print(percentage1, percentage2)
