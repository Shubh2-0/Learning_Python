# # S1 D4 Assignment - Set 4

# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

word1 = "cinema"
word2 = "iceman"
print(is_anagram(word1, word2))



# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

input_array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(input_array)
print(input_array)



# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"
def longest_common_prefix(strs):
    if not strs:
        return ""
    common_prefix = strs[0]
    for word in strs[1:]:
        while word.find(common_prefix) != 0:
            common_prefix = common_prefix[:-1]
    return common_prefix

input_strings = ["flower", "flow", "flight"]
result = longest_common_prefix(input_strings)
print(result)



# 4. **String Permutations**: Write a Python function to calculate all permutations of a given string.
#     - *Input*: "abc"
#     - *Output*: "['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"

from itertools import permutations

def string_permutations(s):
    return ["".join(p) for p in permutations(s)]

input_string = "abc"
permutations_list = string_permutations(input_string)
print(permutations_list)



# 5. **Implement Queue using Stack**: Use Python's stack data structure to implement a queue.
#     - *Input*: enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue(), dequeue()
#     - *Output*: "1, None, 3, None, None"

class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return None

queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
queue.enqueue(3)
print(queue.dequeue())
print(queue.dequeue())



# 6. **Missing Number**: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#     - *Input*: [3, 0, 1]
#     - *Output*: "2"

def missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

input_nums = [3, 0, 1]
result = missing_number(input_nums)
print(result)



# 7. **Climbing Stairs**: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#     - *Input*: 3
#     - *Output*: "3"

def climb_stairs(n):
    if n <= 2:
        return n
    prev_1, prev_2 = 1, 2
    for i in range(3, n+1):
        curr = prev_1 + prev_2
        prev_1, prev_2 = prev_2, curr
    return prev_2

steps = 3
ways = climb_stairs(steps)
print(ways)



# 8. **Invert Binary Tree**: Invert a binary tree (mirroring it).
#     - *Input*: A binary tree
#     - *Output*: Inverted binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root





# 9. **Power of Two**: Given an integer, write a function to determine if it is a power of two.
#     - *Input*: 16
#     - *Output*: "True"1

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

num = 16
print(is_power_of_two(num))


# 10. **Contains Duplicate**: Given an array of integers, find if the array contains any duplicates.
#     - *Input*: [1, 2, 3, 1]
#     - *Output*: "True"

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

input_nums = [1, 2, 3, 1]
print(contains_duplicate(input_nums))


# 11. **Binary Search**: Write a function that implements binary search on a sorted array.
#     - *Input*: [1, 2, 3, 4, 5, 6], target = 4
#     - *Output*: "3"

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_nums = [1, 2, 3, 4, 5, 6]
target = 4
index = binary_search(sorted_nums, target)
print(index)


# 12. **Depth First Search (DFS)**: Implement DFS for a graph in Python.
#     - *Input*: A graph
#     - *Output*: Vertices visited in DFS order


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, edge):
        if vertex in self.graph:
            self.graph[vertex].append(edge)
        else:
            self.graph[vertex] = [edge]

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                stack.extend(self.graph[vertex])



# 13. **Breadth First Search (BFS)**: Implement BFS for a graph in Python.
#     - *Input*: A graph
#     - *Output*: Vertices visited in BFS order
# 14. **Quick Sort**: Implement quick sort in Python.
#     - *Input*: [10, 7, 8, 9, 1, 5]
#     - *Output*: "[1, 5, 7, 8, 9, 10]"

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, edge):
        if vertex in self.graph:
            self.graph[vertex].append(edge)
        else:
            self.graph[vertex] = [edge]

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(self.graph[vertex])




# 15. **Single Number**: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#     - *Input*: [4,1,2,1,2]
#     - *Output*: "4"

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

input_nums = [4, 1, 2, 1, 2]
result = single_number(input_nums)
print(result)


# 16. **Palindrome Linked List**: Given a singly linked list, determine if it is a palindrome.
#     - *Input*: [1,2,2,1]
#     - *Output*: "True"


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values == values[::-1]



