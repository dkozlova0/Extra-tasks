from statistics import mean

with open('students.txt', 'r') as file:
    lines = file.readlines()

students = {}

for line in lines:
    name, score = line.split()
    score = int(score)

    if name in students:
        students[name].append(score)
    else:
        students[name] = [score]

average_scores = {name: mean(scores) for name, scores in students.items()}

all_scores = [score for scores in students.values() for score in scores]
highest_score = max(all_scores)
lowest_score = min(all_scores)
overall_average = mean(all_scores)

with open('results.txt', 'w') as file:
    for name, avg_score in average_scores.items():
        file.write(f'{name} {avg_score:.2f}\n')

    file.write('\n')
    file.write(f'Highest Score: {highest_score}\n')
    file.write(f'Lowest Score: {lowest_score}\n')
    file.write(f'Overall Class Average: {overall_average:.2f}\n')
