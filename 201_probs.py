from itertools import permutations

def number_permutations(numbers):
    return [p for p in permutations(numbers)]

example_numbers = [10,11,12,13,14]

permutations_result = number_permutations(example_numbers)

fixed_perm = (14,13,12,11,10)


def fixed_comparison_func(perms, fixed_perm):
    comparison_results  = []
    for i in range(len(perms)):
        temp_list = []
        for j in range(5):
            if perms[i][j] < fixed_perm[j]:
                temp_list.append("L")
            elif perms[i][j] > fixed_perm[j]:
                temp_list.append("W")
            else:
                temp_list.append("T")
        comparison_results.append(temp_list)
    return(comparison_results)
    
comparison_fixed= fixed_comparison_func(permutations_result, fixed_perm)
            
def cond_prob_calculator(comparisons, cutoff, perms):
    p1_wins = []
    for perm in comparisons:
        if perm.count("W")>=cutoff:
            p1_wins.append(1)
        else:
            p1_wins.append(0)      
    cond_probp1win = sum(p1_wins)/len(perms)
    return(cond_probp1win)

cond_prob_calculator(comparison_fixed, 3, permutations_result)     

def unfixed_comparison_func(perms):
    comparison_results2  = []
    for k in range(len(perms)):
        for i in range(len(perms)):
            temp_list = []
            for j in range(5):
                if perms[i][j] < perms[k][j]:
                    temp_list.append("L")
                elif perms[i][j] > perms[k][j]:
                    temp_list.append("W")
                else:
                    temp_list.append("T")
            comparison_results2.append(temp_list)
    return(comparison_results2)

comparison_unfixed = unfixed_comparison_func(permutations_result)

len(comparison_fixed)

def uncond_prob_calculator(comparisons, cutoff, perms):
    p1_wins_2 = []
    for perm in comparisons:
        if perm.count("W")>=cutoff:
            p1_wins_2.append(1)
        else:
            p1_wins_2.append(0)
    uncond_probp1win = sum(p1_wins_2)/(len(perms)**2)
    return(uncond_probp1win) 


p1_wins_m4 = uncond_prob_calculator(comparison_unfixed, 4, permutations_result)
p1_wins_m4

    
