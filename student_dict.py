student={
101:{"name":"aditi","score":[60,55,80]},
102:{"name":"ram","score":[70,95,40]} ,
    103:{"name":"riti","score":[80,54,67]}
}
for sid,details in student.items():
    avg=sum(details["score"])/len(details["score"])
    details["average"]=avg
    details["passed"]=avg>=50

print("students passed are:")
for sid,details in student.items():
    if details["passed"]:
        print(details["name"])
