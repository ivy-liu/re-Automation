#2018-3-18上午模块文件异常其他

def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums) - i - 1):  # j为列表下标
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
 
print(bubble_sort([45, 32, 8, 33, 12, 22, 19, 97]))
# 输出：[8, 12, 19, 22, 32, 33, 45, 97]


print('\n---from 文件名---')
import sum
print(sum.add_two_num(1,2))

print('\n---from 文件名 import 函数/类----')
from sum import add_two_num
print(add_two_num(2,2))

print('\n---from 文件名 import 文件名----')
from test_folder import test_sum
print(test_sum.test_add_two_num(2,3))