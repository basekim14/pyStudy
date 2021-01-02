
from maxHeapClass import *      # 원활한 모듈 호출을 위하여
import random                   # 해당 소스코드의 import 문에서는
                                # maxHeapClass 이름에 영문만 사용하여 표기
if __name__ == "__main__":
    print("========================================================\n")
    print("\t- Test case 1 -")
    num_list = [7, 9, 4, 8, 6, 3]
    max_heap = MaxHeap(num_list)
    sorted_list = max_heap.heap_sort()

    print("\tList\t:", num_list)
    print("\tBuild\t:", max_heap)
    print("\tSorted\t:", sorted_list)


    print("\n========================================================")