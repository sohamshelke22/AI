def selectionsort(students):
    n=len(students)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if students[j][1]>students[min][1]:
                min=j

        students[i],students[min]=students[min],students[i]
    
    return students


n=int(input("Enter number of students: "))
students=[]

for i in range(n):
    name=input("Enter name of student "+str(i+1)+": ")
    marks=int(input("Enter marks of "+name+": "))
    students.append((name,marks))


sorted_stud=selectionsort(students)

print("Students ranking by marks(descending order): ")

i=1
for student in sorted_stud:
    print("rank: ",str(i),student[0],"->",student[1],"marks")
    i=i+1




def sort_by_profit(job):
    return job[2]

def job_scheduling(jobs):
    jobs.sort(key=sort_by_profit,reverse=True)

    max_deadline=jobs[0][1]
    for job in jobs:
        if job[1]>max_deadline:
            max_deadline=job[1]

    slots=[None]*max_deadline
    total_profit=0

    for job in jobs:
        job_id=job[0]
        deadline=job[1]
        profit=job[2]

        for i in range(deadline-1,-1,-1):
            if slots[i] is None:
                slots[i]=(job_id,profit)
                total_profit+=profit
                break
        
    return slots,total_profit

n=int(input("Enter no of jobs: "))
jobs=[]

for i in range(n):
    print("Enter job details for ",i+1)
    job_id=input("Enter job_id: ")
    deadline=int(input("Enter deadline: "))
    profit=int(input("Enter profit: "))

    jobs.append((job_id,deadline,profit))


schedule,profit=job_scheduling(jobs)

for i in range(len(schedule)):
    print("Slot ",i+1,": ",schedule[i][0],"Profit = ",schedule[i][1])

print("Total profit",profit)

    
