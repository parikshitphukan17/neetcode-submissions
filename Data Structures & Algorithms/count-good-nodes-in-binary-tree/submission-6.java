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
    Integer res = 0;
    public int goodNodes(TreeNode root) {
        count(root,-101);
        return res;
    }

    public void count(TreeNode node, int maxVal){
        if(node == null){
            return;
        }
        if(node.val>=maxVal){
            maxVal = node.val;
            res++;
        }
        count(node.left,maxVal);
        count(node.right,maxVal);
    }
}
