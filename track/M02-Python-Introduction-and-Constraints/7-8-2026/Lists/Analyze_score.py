n=int(input())
scores=[]
for i in range(n):
    num=int(input())
    scores.append(num)
search_score=int(input("Enter the score to be searched:"))
print("Highest Score:",max(scores))
print("Lowest Score:",min(scores))
print("Total Score:",sum(scores))
if(search_score in scores):
    print("Score found")
else:
    print("Score not found")