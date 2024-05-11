---
title: 【LeetCode】做题家之563. Binary Tree Tilt
layour: post
uuid: ffw22d-a0ad-11ed-fasfw-wqr2fa
tags: [LeetCode]
categories: LeetCode
index_img:  ![](https://img.164314.xyz/img/2024/05/0b06136ccc3c9178ab9a2f199a27b5a3.png)
date: 2024-05-11 18:07:08
---

# 请看题

![](https://img.164314.xyz/img/2024/05/0b06136ccc3c9178ab9a2f199a27b5a3.png)

## Example 

![](https://img.164314.xyz/img/2024/05/128fe0ceaa7c3791d7641c5bc475c3bc.png)
![](https://img.164314.xyz/img/2024/05/241d543045ff7078582feba47c19c4c9.png)
![](https://img.164314.xyz/img/2024/05/1537a88d239a19d8bbb7c1a11d7a9a45.png)

# 思路

还是熟悉的二叉树结构，我们还是可以继续用递归来解决


首先要判断的几个点是如果左节点或者右节点为空那么Tilt为0，如果不为空那么使用递归来进行获取到节点的值。每个节点的值都要进行 *abs(left - right)* 操作，题目要求的。

首先要获取到左节点的孩子们所有的值，然后获取右节点孩子们的所有值，再然后进行获取Tilt，有点绕脑，但是递归能够很好的为我们解决这个问题

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
    int answer;
    int solution(TreeNode *root)
    {
        int left = (root->left ? solution(root->left) : 0);
        int right = (root->right ? solution(root->right) : 0);
        answer += abs(left - right);

        return left + right + root->val;
    }
    int findTilt(TreeNode* root) {
        if(root)solution(root);
        return answer;
    }
};
```

## 代码解析

我定义了一个answer的值，此值用来返回Tilt答案，另外我还定义了一个solution函数来获取每个节点的值并且返回

在solution中，我使用了三元表达式，提一个小知识点
```
if(root != nullptr)和if(root)一个意思
if(root==nullptr)和if(!root)一个意思
```
如果当前节点不为空那么进行递归下一个节点，否则返回0；

然后进行对answer变量的值更改，每一次递归都会有新的值。

solution 返回的值为int，每一个int都会赋值给left 和 right 然后再对answer进行增加

---

在主函数中 findTilt(TreeNode *root) 需要对当前节点进行判断是否为空，如果不为空，进行递归。

最后递归结束，answer的值已经达到了要求，返回answer
---
---
结束
