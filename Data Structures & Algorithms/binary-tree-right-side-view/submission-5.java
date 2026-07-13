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
    public List<Integer> rightSideView(TreeNode root) {
        Deque<TreeNode> cur = new LinkedList<>();
        List<Integer> res = new ArrayList<>();
        if(root == null){
            return res;
        }
        cur.addLast(root);
        TreeNode rightNode = root;
        while(cur.size()>0){
            Deque<TreeNode> child = new LinkedList<>();
            while(cur.size()>0){
                rightNode = cur.removeFirst();
                if(rightNode.left != null){
                    child.addLast(rightNode.left);
                }
                if(rightNode.right != null){
                    child.addLast(rightNode.right);
                }
            }
            res.add(rightNode.val);
            cur = child;
        }
        return res;

        
    }
}
