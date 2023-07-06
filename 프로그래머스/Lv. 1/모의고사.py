# Version 1
def solution(answers):
    student1 = [1,2,3,4,5]*(len(answers)//5) + [1,2,3,4,5][:len(answers)%5]
    student2 = [2,1,2,3,2,4,2,5]*(len(answers)//8) + [2,1,2,3,2,4,2,5][:len(answers)%8]
    student3 = [3,3,1,1,2,2,4,4,5,5]*(len(answers)//10) + [3,3,1,1,2,2,4,4,5,5][:len(answers)%10]
    
    counts = [0] * 3
    for i in range(len(answers)):
        if answers[i] == student1[i]:
            counts[0] += 1
        if answers[i] == student2[i]:
            counts[1] += 1
        if answers[i] == student3[i]:
            counts[2] += 1
    max_count = max(counts)
    
    student = []
    for i in range(len(counts)):
        if counts[i] == max_count:
            student.append(i+1)
    
    return student


# Version 2
def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    counts = [0] * 3
    for i in range(len(answers)):
        if answers[i] == student1[i%len(student1)]:
            counts[0] += 1
        if answers[i] == student2[i%len(student2)]:
            counts[1] += 1
        if answers[i] == student3[i%len(student3)]:
            counts[2] += 1
    
    return [i+1 for i, count in enumerate(counts) if count==max(counts)]
