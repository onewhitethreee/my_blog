---
title: 94. Binary Tree Inorder Traversal
layour: post
uuid: ft22d-a0ad-11ed-fasfw-wqr2fa
tags: [LeetCode]
categories: LeetCode
index_img:  https://img.164314.xyz/img/2024/05/892f29bb3667a600f95ad4712e8ea48e.png
date: 2024-05-15 18:07:08
---
# 请看题

![](https://img.164314.xyz/img/2024/05/892f29bb3667a600f95ad4712e8ea48e.png)

## Example 

![](https://img.164314.xyz/img/2024/05/ab99b54754ed080c0bcbc67ddcd0ea74.png)

# 思路

这道题太简单了，直接上代码了



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
    vector<int> result;
    void InordenAux(TreeNode *root)
    {
        if(!root){return;}
        InordenAux(root->left);
        result.push_back(root->val);
        InordenAux(root->right);
    }
    vector<int> inorderTraversal(TreeNode* root) {
        if(!root)
        {
            return result;
        }
        InordenAux(root);
        return result;
    }
};
```

## 代码解析

这一道题非常简单，二叉树无序遍历无非就是递归，只需要一直递归然后保存就好了，太简单了这道题。没啥可说的
---

---
结束

# Preorden And Postorden
```
vector<int> result;
    void preorderTraversalAux(TreeNode *root)
    {
        if(!root){return;}
        result.push_back(root->val);
        preorderTraversalAux(root->left);
        preorderTraversalAux(root->right);
    }
    vector<int> preorderTraversal(TreeNode* root) {
        if(!root)
        {
            return result;
        }
        preorderTraversalAux(root);
        return result;
    }
```

```
class Solution {
public:
vector<int> result;
    void postorderTraversalAux(TreeNode *root)
    {
        if(!root){return;}
        postorderTraversalAux(root->left);
        postorderTraversalAux(root->right);
        result.push_back(root->val);
    }
    vector<int> postorderTraversal(TreeNode* root) {
        if(!root)
        {
            return result;
        }
        postorderTraversalAux(root);
        return result;
    }
    
};
```
---
结束
