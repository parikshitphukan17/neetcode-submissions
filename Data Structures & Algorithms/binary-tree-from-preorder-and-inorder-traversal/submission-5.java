/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */




class Solution {
    Map<Integer,Integer> map = new HashMap<>();
    int preorderIdx = 0;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for(int i=0;i<inorder.length;i++){
            map.put(inorder[i],i);
        }
        return dfs(preorder,0,inorder.length-1);

        
    }
    //                 4
    //     2                    6
    // 1       3             5       7

    // preorder =[4,2,1,3,6,5,7]
    // inOrder = [1,2,3,4,5,6,7]

    public TreeNode dfs(int[] preorder,int l,int r){
        if(l>r)
            return null;
        var node = new TreeNode(preorder[preorderIdx++]);
        var index = map.get(node.val);
        node.left = dfs(preorder,l,index-1);
        node.right = dfs(preorder,index+1,r);
        return node;
    }
}
