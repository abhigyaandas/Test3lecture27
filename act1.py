student1={"name":"Ava","test_score":"98"}
student2={"name":"Bob","test_score":"91"}
student3={"name":"Joe","test_score":"76"}
student4={"name":"Max","test_score":"81"}
student5={"name":"Dan","test_score":"100"}

maxim=max(student1["test_score"],student2["test_score"],student3["test_score"],student4["test_score"],student5["test_score"])
print(maxim)
minim=min(student1["test_score"],student2["test_score"],student3["test_score"],student4["test_score"],student5["test_score"])
print(minim)

find=input(print("Ask for any name, Ava, Bob, Joe, Max, Dan:"))
names=[student1,student2,student3,student4,student5]
for finds in names:
    if finds.get("name")==find:
        print(finds.get("name"))