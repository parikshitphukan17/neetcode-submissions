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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(p.val>q.val){
            var temp = p;
            p = q;
            q = temp;
        }
        return findAncestor(root,p.val,q.val);
    }
    public TreeNode findAncestor(TreeNode node,int p, int q){
        if(node.val>=p && node.val<=q){
            return node;
        }
        if(q<node.val){
            return findAncestor(node.left,p,q);
        }
        return findAncestor(node.right,p,q);
    }
}
