# https://school.programmers.co.kr/learn/courses/30/lessons/64064

import re
import itertools
"""
def solution(user_id, banned_id):
    answer = 0
    regex_ids = (b_id.replace('*', '\w') for b_id in banned_id)
    
    b_u_ids = []
    for regex in regex_ids:
        b_u_ids.append(re.findall("'" + regex + "'", str(user_id)))
            
    cases = list(itertools.product(*b_u_ids))
    #print(cases)
    refined = []
    
    for case in cases:
        case = set(case)
        if len(case) == len(banned_id) and case not in refined:
            refined.append(case)
        
    return len(refined)
"""
#################################################
def dfs (matrix):
    paths = []
    if len(matrix) == 1:
        for item in matrix[0]:
            paths.append([item])
    else:
        sub_paths = dfs(matrix[1:])
        for item in matrix[0]:
            for sub_path in sub_paths:
                if item not in sub_path:
                    paths.append([item] + sub_path)
    return paths

def solution(user_id, banned_id):
    answer = 0
    founds = []
    for b_id in banned_id:
        b_u_ids = []
        for u_id in user_id:
            b_len = len(b_id)
            if b_len == len(u_id):
                found = True
                for i in range(b_len):
                    if b_id[i] != "*" and b_id[i] != u_id[i]:
                        found = False
                        break
                if found:
                    b_u_ids.append(u_id)
        #print(b_u_ids)            
        founds.append(b_u_ids)
    
    #print(founds)
    cases = dfs(founds)
    #print(cases)
    
    uniqued = []
    for case in cases:
        case = set(case);
        if case not in uniqued:
            uniqued.append(case)
    
    return len(uniqued)