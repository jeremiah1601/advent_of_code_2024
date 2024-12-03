
def solution(list_1: list[int], list_2: list[int]) -> int:
    # 1. sort the two lists 
    # 2. sum their individual differences

    return sum([abs(i - j) 
                for i,j in 
                list(zip(sorted(list_1), sorted(list_2)))])