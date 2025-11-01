from collections import Counter

class Solution:
    def search(self, pat, txt):
        m, n = len(pat), len(txt)
        result = []
        pat_count = Counter(pat)

        for i in range(n - m + 1):
            window = txt[i:i + m]
            if Counter(window) == pat_count:
                result.append(i)

        return result if result else [-1]
    
# # class Solution {
#     ArrayList<Integer> search(String pat, String txt) {
#         // code here
#         ArrayList<Integer> result = new ArrayList<>();
#         int m=pat.length();
#         int n=txt.length();
        
#         for(int i =0;i<=n-m;i++)
#         {
#             if(txt.substring(i,i+m).equals(pat))
#             {
#                 result.add(i);
#             }
#         }
       
#         return result;
#     }
# }