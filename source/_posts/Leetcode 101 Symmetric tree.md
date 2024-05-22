---
title: Leetcode 101 Symmetric tree
layour: post
uuid: 2f2d-a0ad-11ed-faswf-wqr2fa
tags: [LeetCode]
categories: LeetCode
index_img:  https://img.164314.xyz/img/2024/05/88ed5dd895fed0ca934f11e82973c09f.png
date: 2024-05-21 18:07:08
---
![](https://img.164314.xyz/img/2024/05/88ed5dd895fed0ca934f11e82973c09f.png)

# 请看题
![](https://img.164314.xyz/img/2024/05/b2753a2ae48ab599f391ac3fea4d7225.png)

# Example

![](https://img.164314.xyz/img/2024/05/b2c1f1348e5eff68aafb6a7588766a35.png)

![](https://img.164314.xyz/img/2024/05/d8e0c4e2d456371c654b753513bb2c89.png)

# 思路

从Leetcode给我们的例子中可以看出来，两颗树是对称的是当元素的位置和元素内容都是对称的，如果有任意一颗树含有多余节点那么就不是对称的

还是递归，从leetcode模板中可以知道传入的是一颗完整的树，而我们需要去进行判断，怎么判断呢？

## 新建函数传入左右节点

我们可以新建一个函数用来接收左节点的和右节点的内容，如果

1. 有任意节点的元素不一样那就不是对称的
2. 一个为空一个不为空也是不对称的
3. 两者为空时对称的


根据上方三条规则可以写出以下代码

这里只有一个知识点，在我们的函数中传入的时左节点的左孩子和右节点的右孩子然后加一个and条件，左节点的右孩子和右节点的左孩子

----

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
    bool isSymmetricAux(TreeNode* left, TreeNode*right)
    {
        if(!left && !right)
        {
            return true;
        }
        if(!left || !right || left->val != right->val)
        {
            return false;
        }
        return isSymmetricAux(left->left, right->right) && 
        isSymmetricAux(left->right, right->left);
    }
    bool isSymmetric(TreeNode* root) {
        if(!root){return true;}

        return isSymmetricAux(root->left, root->right);
    }
};
```
---
结束。