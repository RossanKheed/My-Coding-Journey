#check eligibility 
def eligibility_check(physics, math):
    if physics >=80 and math >=80:
        return "ELIGIBLE "
    else:
        return "NOT ELIGIBLE "
#get those phyiscs and math scores
p_score=int(input("What is your physics score:"))
m_score=int(input("What is your math score:"))
# check status
status= eligibility_check(p_score,m_score)
#result
print("Result is , "  + status)