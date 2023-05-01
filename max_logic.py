
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
y = int(len(student_scores)) - 1
print(y)
for x in range(0 , y):
  if int(student_scores[x]) > int(student_scores[x + 1]) and x <= y:
    max_score = int(student_scores[x])
  else:
    max_score = int(student_scores[x+1])
    print(max_score)
print(max_score)
