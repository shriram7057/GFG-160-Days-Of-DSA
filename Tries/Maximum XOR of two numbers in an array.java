class TrieNode {
    TrieNode[] children = new TrieNode[2];
}

class Solution {
    private TrieNode root = new TrieNode(); // 'Private' → 'private'

    private void insert(int num) {
        TrieNode node = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (node.children[bit] == null) {
                node.children[bit] = new TrieNode();
            }
            node = node.children[bit];
        }
    }

    private int findMaxXor(int num) {
        TrieNode node = root; // 'Node' → 'node'
        int maxXor = 0;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            int oppositeBit = 1 - bit;
            if (node.children[oppositeBit] != null) {
                maxXor |= (1 << i);
                node = node.children[oppositeBit];
            } else {
                node = node.children[bit];
            }
        }
        return maxXor;
    }

    public int maxXor(int[] arr) {
        int max = 0;
        for (int num : arr) {
            insert(num);
        }
        for (int num : arr) {
            max = Math.max(max, findMaxXor(num));
        }
        return max;
    }
}
