---
title: LeetCode 965. Univalued Binary Tree
layour: post
uuid: ftw2d-a0ad-11ed-fasfw-wqr2fa
tags: [LeetCode]
categories: LeetCode
index_img:  https://img.164314.xyz/img/2024/05/fde38c072002d7b5dd92d5fd3a9c6721.png
date: 2024-05-12 18:07:08
---

# 请看题

![](https://img.164314.xyz/img/2024/05/fde38c072002d7b5dd92d5fd3a9c6721.png)

## Example 

![](https://img.164314.xyz/img/2024/05/224c43b468c1dd07321c03b2d375541c.png)

![](https://img.164314.xyz/img/2024/05/b20c130425f9ada0e09ded69ff3c8513.png)
# 思路

还是熟悉的二叉树结构，我们还是可以继续用递归来解决

这道题就是来判断当前树是否都是同样的值
对于判断是否相等我们可以传入一个初始值，这个初始值为一个不变的值，如果在比较中有一处不同，那么这个树的答案为false，反之true

直接上代码了

## Code

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    bool isUni(TreeNode *root, int val)
    {        
        if(!root){return true;}

        if(root->val != val)
        {
            return false;
        }
        return isUni(root->left, val) && isUni(root->right, val);
    }

    bool isUnivalTree(TreeNode* root) 
    {
        return isUni(root, root->val);
    }
};
```

## 代码解析

这一道题非常简单，只需要传入一个val值然后根据这个val值来判断是否和当前节点相同。

val值是固定的，不会改变。如果有一个为不相等的话，那么返回false，另外 and 条件也就不成立，返回false，一路false到最后答案就是false。如果一直相等，一路true最后也肯定还是true。
---

---
结束
