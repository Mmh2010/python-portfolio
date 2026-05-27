#list of scores
scores = [
88, 42, 95, 70, 63, 82, 55, 91, 74, 85,
38, 77, 90, 61, 89, 72, 59, 98, 45, 81,
67, 73, 88, 52, 94, 79, 100, 68, 83, 71
]
#2.1 prints the lowest and highest score
print(min(scores))
print(max(scores))
#2.2 prints the average score
print(sum(scores)/len(scores))
#2.3 sorts the list lowest to highest and prints worst three scores
scores.sort()
print(scores)
print(scores[0], scores[1], scores[2])
#2.4 makes a loop that adds 5 to each test score
def main():
    for i in range(len(scores)):
        scores[i]=scores[i]+5
main()
print(scores)
