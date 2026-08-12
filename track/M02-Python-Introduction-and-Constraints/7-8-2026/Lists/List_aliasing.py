original_scores=[]
for i in range(3):
    i=int(input("Enter Score:"))
    original_scores.append(i)
alias_scores=original_scores

replacement_score=int(input("Enter Replacement Score:"))
additional_score=int(input("Enter Additional Score:"))

alias_scores[0]=replacement_score
alias_scores.append(additional_score)

print("Original Scores",original_scores)
print("Alias Scores:",alias_scores)
print("Shared Object:",original_scores is alias_scores)