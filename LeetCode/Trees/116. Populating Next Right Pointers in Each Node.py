'''
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = collections.deque()
        q.append(root)

        while q:  # while q is not ()
            cur = q.popleft()

            if cur.left:  # if it has a children
                cur.left.next = cur.right  # here we established a pointer btn children of same node
                if cur.next:  # if not null go inside else skip
                    cur.right.next = cur.next.left  # here we establish a pointer btn childrens of different node
                q.append(cur.left)
                q.append(cur.right)

        return root
