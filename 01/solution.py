# Part 1
with open("input.txt", "r") as input_file:
    numbers = input_file.readlines()

first = [int(i.split()[0]) for i in numbers]
second = [int(i.split()[1]) for i in numbers]

first.sort()
second.sort()

distances = []
for i in range(len(first)):
    distances.append(abs(first[i]-second[i]))

total_distance = sum(distances)
print(f'Total distance: {total_distance}')

# Part 2
similarity = [] 
for i in first:
    similarity.append(i * second.count(i))

similarity_score = sum(similarity)
print(f'Similarity score: {similarity_score}')