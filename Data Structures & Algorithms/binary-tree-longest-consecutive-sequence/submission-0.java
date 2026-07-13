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
    int res = 0;
    public int longestConsecutive(TreeNode root) {
        if(root == null){
            return 0;
        }
        dfs(root,null,1);
        return res;

        
    }

    public void dfs(TreeNode node,TreeNode prev, int res){
        if(node == null){
            return;
        }
        if(prev == null){
            this.res = Math.max(res,this.res);
            dfs(node.left,node,res);
            dfs(node.right,node,res);

        } else {
            if(prev.val +1 == node.val){
                res +=1;
                this.res = Math.max(res,this.res);
            } else {
                res = 1;
            }
            dfs(node.left,node,res);
            dfs(node.right,node,res);

        }
    }
}
