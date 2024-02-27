from typing import List, Tuple


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    # complexity is O(n^2)
    for i in range(len(li)):
        for j in range(len(li)):
            if (li[i] + li[j]) == target:
                return i, j


assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    # complexity is O(n)
    new_dic = {}
    for i, num1 in enumerate(li):
        num2 = target - num1
        if num2 in new_dic:
            return li.index(num2), i
        new_dic[num1] = i


assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
