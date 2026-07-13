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
    public boolean isValidBST(TreeNode root) {
        return check(root,Integer.MAX_VALUE,Integer.MIN_VALUE);
        
    }

    public boolean check(TreeNode node,int maxVal,int minVal){
        if(node == null){
            return true;
        }
        if(node.val<= minVal || node.val>= maxVal){
            return false;
        }
        return check(node.left,node.val,minVal) && check(node.right,maxVal,node.val);
        
    }
}
