---
title: LeetCode 257 Binary Tree Paths
layour: post
uuid: fasw2sd-a0ad-11ed-fasfw-wqr2fa
tags: [LeetCode]
categories: LeetCode
date: 2024-05-09 18:07:08
---

# 请看题

![](https://img.164314.xyz/img/2024/05/a876bc7be958fe82c3281ddf426eb196.png)

给一个二叉树结构的节点，要求输出内容为
![](https://img.164314.xyz/img/2024/05/b399bb6691b55dbbc09b82c2ddf6c75a.png)
![](https://img.164314.xyz/img/2024/05/451822356e7b305b6d35aa255b249589.png)

要求返回值为一个vector。

# 开始做题

先来看第二个Example。

一个树中只有一个节点，那么我们可以进行if判断来返回其节点，代码可为

```
if(!node->left && !node->right)
    {
        ans.push_back(path);
    }
```

###  想要理解代码，那就得先知道代码长什么样，此处为主函数用作解答

```
vector<string> binaryTreePaths(TreeNode* root) 
    {
        vector<string> ans;
        dfs(ans, "", root);
        return ans;
    }
```

那么已经解决了Example 2 在上面的if，我们就可以进行针对其他的情况来进行解答了。

二叉树，无非就是递归，递归左节点，递归右节点，这里也是一样，在使用递归后，获取每一个节点的值，将其转为string然后push到vector中，当没有可以递归的节点后那么也就是该结束的时候，贴上递归结束条件代码

```
if(!node)
    {
        return;
    }
```

以上if和node != nullptr 等价

然后就是使用递归

```
dfs(ans, path+"->", node->left);
dfs(ans, path+"->", node->right);
```
最后结束。

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

    void dfs(vector<string> &ans, string path ,TreeNode *node)
    {
        if(!node)
        {
            return;
        }
        path += to_string(node->val);
        if(!node->left && !node->right)
        {
            ans.push_back(path);
        }
        dfs(ans, path+"->", node->left);
        dfs(ans, path+"->", node->right);
    }
    vector<string> binaryTreePaths(TreeNode* root) 
    {
        vector<string> ans;

        dfs(ans, "", root);
        return ans;
    }
};
```
