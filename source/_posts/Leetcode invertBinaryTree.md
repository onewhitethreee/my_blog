---
title: LeetCode 226 invert binary tree
layour: post
uuid: fasw2d-a0ad-dwrd-fasfw-wqr2fa
tags: [LeetCode]
categories: LeetCode
index_img:  https://img.164314.xyz/img/2024/05/3ad0682e0d42b168d1284066712d1f9e.png
date: 2024-05-05 18:07:08
---

# 请看题
![](https://img.164314.xyz/img/2024/05/f3cd89f881cceeb5c15e759eeaa08b28.png)

![](https://img.164314.xyz/img/2024/05/c708a5ac1a34ef1a2150580b9c393f29.png)

还是熟悉的二叉树，还是熟悉的递归。

# 思路

首先是第三种情况，咱们直接解决掉好了。当目前节点为空的情况下直接返回，代码可以这么写

```
if(root == nullptr)
{
    return root;
}
```
第三种情况就这样解决了，接下来看另外两种情况。

首先一开始我的思路是通过遍历或者递归来获取所有的节点然后重新插入，按照左大右小的方式，但是后来我发现这样子也太麻烦了。这种题怎么可以会这么麻烦呢，我苦思苦想，就是想不到啊，然后我打开了solution，看到了别人的答案，我才发现原来这么简单啊！

通过一个swap函数或者手动写一个交换节点的规则然后在加上递归就能成功的解决这道题，代码如下

```
swap(root->left, root->right);
invertTree(root->left);
invertTree(root->right);
return root;
```

首先交换了左右节点的值，进入递归，加上上面的那个if来进行判断，一直这样直到无法交换，最后返回。这种解题方法真是牛掰至极啊！可惜的是我没有想到，看到了答案才懂的，可惜

```


class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root == nullptr)
        {
            return root;
        }
        swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root;

    }
};
```
