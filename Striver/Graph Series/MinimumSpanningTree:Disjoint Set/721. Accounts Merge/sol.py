class Disjoint:
    def __init__(self, n):
        self.rank = [1] * (n + 1)
        self.parent = [i for i in range(n)]
        
    def findParent(self, x):
        if self.parent[x] != x:
            # path compression
            self.parent[x] = self.findParent(self.parent[x])
        
        return self.parent[x]
    
    def union_rank(self, u, v):
        # step 1: Find the ultimate parent
        pu = self.findParent(u)
        pv = self.findParent(v)
        
        # if they belong to same connected component
        if pv == pu:
            return
        
        # step 2: Get rank of parent
        rank_pv = self.rank[pv]
        rank_pu = self.rank[pu]
        
        # step 3: attach smaller rank to larger rank
        if rank_pu < rank_pv:
            self.parent[pu] = pv
        elif rank_pv < rank_pu:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1



from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        
        disjoint_obj = Disjoint(n)
        
        # Creting Union ---------------------
        
        #  create a dictionary set to store email --> index of acc
        # if there is a duplicate email create union
        mapping = defaultdict() 
        
        for idx, col in enumerate(accounts):
            # print(idx ,col)
            emails = col[1: ]
            for email in emails:
                if email in mapping:
                    u = mapping[email]
                    v = idx
                    disjoint_obj.union_rank(u , v)
                else:
                    mapping[email] = idx
        
        # print(mapping)
        
        
       # Traversing in the nodes and appending email to ultimate parents ---------------
        mergedEmail = defaultdict(list) 
        
        for email ,idx in mapping.items():
            ultimateParent = disjoint_obj.findParent(idx)
            mergedEmail[ultimateParent].append(email)
        
        # print(mergedEmail)
            
        # creating a sorted list on  name and email  -------------------
        mergedAccounts = []
        
        for idx, emails in mergedEmail.items():
            name = accounts[idx][0]
            # merging
            mergedAccounts.append([name]+ sorted(emails))
        
        # print(mergedAccounts)
        
        return mergedAccounts