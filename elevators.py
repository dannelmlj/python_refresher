e = int(input())
floors = int(input())

elevators_index = []
start_time_sorted = []

for i in range(e):
    time = int(input())
    mypair = [time, -1]
    elevators_index.append(mypair)
    start_time_sorted.append(time)

start_time_sorted.sort()
values = []
for i in range(e):
    value = 0
    additional = 0
    if i == 0:
        values.append(0)
    else:
        value = values[i-1]
        additional = ((start_time_sorted[i] - start_time_sorted[i-1])*i)
        total = value + additional
        if total >= (floors-2):
            break
        values.insert(i, value+additional)
        # values[i] = value + additional
    for j in range(e):
        if elevators_index[j][0] == start_time_sorted[i] and elevators_index[j][1] == -1:
            elevators_index[j][1] = values[i]
            break

print(elevators_index)
print(start_time_sorted)
print(values)
for i in range(e):
    if elevators_index[i][1] != -1:
        for j in range(i):
            if elevators_index[j][0] <= elevators_index[i][0]:
                elevators_index[i][1] += 1
    if elevators_index[i][1] > (floors-2):
        print(-1)
    else:
        print(elevators_index[i][1])
