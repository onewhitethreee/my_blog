---
title: Leetcode 100 Same Tree
layour: post
uuid: ft22d-a0ad-11ed-faswf-wqr2fa
tags: [LeetCode]
categories: LeetCode
index_img:  https://img.164314.xyz/img/2024/05/966553c9524f22132e529b6d3dca78ba.png
date: 2024-05-21 18:07:08
---

![](https://img.164314.xyz/img/2024/05/966553c9524f22132e529b6d3dca78ba.png)

# 请看题
![](https://img.164314.xyz/img/2024/05/71660b0823a86036623510f9b16f265b.png)

# Example

![](https://img.164314.xyz/img/2024/05/75299a975c14990c68dd2ab60e8d3ba2.png)
![](https://img.164314.xyz/img/2024/05/e210530daa2922efc336252f87cf7089.png)

![](https://img.164314.xyz/img/2024/05/b654aad0bf305079c592add9f51fd618.png)

# 思路

从Leetcode给我们的例子中可以看出来，两颗树是一样的当元素的位置和元素内容都是等于才是一样的树。那么在这里思考思考一下逻辑，反向来推导结论

首先必要的就是递归了，给的参数是两棵树，那么递归的必要条件就是每一次调用的时候都传入这两棵树的左右节点，这里的左右节点条件为and，不是or。需注意


那么如果两棵树同时为空说明是一样的，这时候返回true

按照这个道理可以推导出如果不同时为空必定不一样。

到此，我们已经有了两个关键的递归条件，分别是同时和不同时为空，接下来再补一个条件就可以解决这道题了。

这个条件是什么呢，这个也很简单，就是判断两棵树的元素相同不相同，写出if即可，最后递归到每一个新的节点。在进行if的时候也要进行一个空指针判断来防止正在访问的元素为不为空。

根据上方三条规则可以写出以下代码

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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(!p && !q)
        {
            return true;
        }
        if(!p || !q)
        {
            return false;
        }
        if(p->val != q->val || !p || !q)
        {
            return false;
        }
        return isSameTree(p->right, q->right) && isSameTree(p->left, q->left);
        
    }
};
```
---
结束。
