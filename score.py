scores = [2, 3, 6, 8, 5]   

first = -999999
second = -999999

for score in scores:
    if score > first:
        second = first
        first = score
    elif score > second and score != first:
        second = score

print("Runner-up score:", second)
