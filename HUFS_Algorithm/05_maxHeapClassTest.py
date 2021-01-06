
from maxHeapClass import *      # 원활한 모듈 호출을 위하여
from math import ceil           # 해당 소스코드의 import 문에서는
from random import *            # maxHeapClass 이름에 영문만 사용하여 표기

def print_testcase(num_list):
    print("\tList\t: %s" % num_list)

    max_heap = MaxHeap(num_list)
    print("\tBuild\t: %s" % max_heap)

    sorted_list = max_heap.heap_sort()
    print("\tSorted\t: (ascending)  %s" % max_heap)
    print("\t\t\t  (descending) %s\n" % sorted_list)

    while True:
        # insert할 node를 적절한 범위를 설정한 뒤 중복이 안되게 임의 선정
        rand_node = randint(0, max(num_list) + ceil(len(num_list) * 0.1))
        if rand_node not in num_list:
            break

    max_heap.insert(rand_node)
    print("\tInsert\t: %s (Inserted node : %s)" %(max_heap, rand_node))

    ai_sorted_list = max_heap.heap_sort()  # after insert
    print("\tSorted\t: (ascending)  %s" % max_heap)
    print("\t\t\t  (descending) %s\n\n" % ai_sorted_list)


if __name__ == "__main__":
    print("=======================================================================\n")

    print("\t- Test case 1 -")
    num_list = [7, 9, 4, 8, 6, 3]
    print_testcase(num_list)

    print("\t- Test case 2 -")
    num_list = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    print_testcase(num_list)

    print("\t- Test case 3 -")
    # 0~25 범위를 가진 길이 5의 랜덤 리스트를 생성
    num_list = sample([i for i in range(0, 26)], 26)[:5]
    print_testcase(num_list)

    print("\t- Test case 4 -")
    # 0~50 범위를 가진 길이 10의 랜덤 리스트를 생성
    num_list = sample([i for i in range(0, 51)], 51)[:10]
    print_testcase(num_list)

    print("=======================================================================")