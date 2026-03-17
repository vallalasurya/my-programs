python_students =input("enter names and scores:").split(",")
python_students=[]
for item in python_students:
    name,score=item.split()
    python_students.append((name,float(score)))
    python_students.append((name,int(score)))
unique_scores = sorted(set([score for name, score in python_students]))
second_lowest = unique_scores[1]
for name, score in sorted(python_students):
      if score == second_lowest[1]:
          print(name)
        

