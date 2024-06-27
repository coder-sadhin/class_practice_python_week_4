def find_survivor(a):
    n = int(a)
    people = list(range(1, n + 1))
    kill_index = 0

    while len(people) > 1:
        kill_index = (kill_index + 1) % len(people)
        people.pop(kill_index)

    return people[0]
a = input()
result = find_survivor(a)
print(result)