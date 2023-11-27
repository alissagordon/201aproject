from itertools import permutations

def number_permutations(numbers):
    return [p for p in permutations(numbers)]

example_numbers = [10,11,12,13,14]
permutations_result = number_permutations(example_numbers)


fixed_perm = (14,13,12,11,10)


comparison_results  = []
for i in range(len(permutations_result)):
    temp_list = []
    for j in range(5):
        if permutations_result[i][j] < fixed_perm[j]:
            temp_list.append("L")
        elif permutations_result[i][j] > fixed_perm[j]:
            temp_list.append("W")
        else:
            temp_list.append("T")
    comparison_results.append(temp_list)
    
    
p1_wins = []
        
for perm in comparison_results:
    if perm.count("W")>=3:
        p1_wins.append(1)
    else:
        p1_wins.append(0)
        
cond_probp1win = sum(p1_wins)/len(permutations_result)
cond_probp1win 



permutations_resultp2 = number_permutations(example_numbers)

comparison_results2  = []

for k in range(len(permutations_resultp2)):
    for i in range(len(permutations_result)):
        temp_list = []
        for j in range(5):
            if permutations_result[i][j] < permutations_resultp2[k][j]:
                temp_list.append("L")
            elif permutations_result[i][j] > permutations_resultp2[k][j]:
                temp_list.append("W")
            else:
                temp_list.append("T")
        comparison_results2.append(temp_list)
        
        
p1_wins_2 = []
for perm in comparison_results2:
    if perm.count("W")>=3:
        p1_wins_2.append(1)
    else:
        p1_wins_2.append(0)
        
uncond_probp1win = sum(p1_wins_2)/(len(permutations_resultp2)* len(permutations_result))
uncond_probp1win 

p1_p2_tie = []