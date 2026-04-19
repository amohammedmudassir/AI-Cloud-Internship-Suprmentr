#Assignment 5 (19/02/2026) 
#Assignment Name : Student Data Manager Description : Store data for 5 students using dictionaries, 
# print topper, class average, and assign grades.
n=5
students=[]
for i in range(1,n+1):
    name=input(f"Enter your name for student {i}:")
    marks=int(input(f"Enter your marks for student {i}:"))
    student={"name":name, "marks":marks}
    students.append(student)
print(students)
#finding topper
topper=max(students, key=lambda x: x['marks'])
print(f"The topper is {topper['name']} with marks {topper['marks']}")
#finding class avh
total_sum=sum(students[i]['marks'] for i in range(n))
class_avg=total_sum/n
print(f"The class average is {class_avg}")
#Grading each student
for i in range(n):
    if students[i]['marks']>=90:
        grade='A'
    elif students[i]['marks']>=80:
        grade='B'
    elif students[i]['marks']>=70:
        grade='C'
    elif students[i]['marks']>=60:
        grade='D'
    else:
        grade='F'
    print(f"The grade for student {students[i]['name']} is {grade}")