

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        # COMBINE THE THREE LIST
        webInfo = []
        for time, usr, web in zip(timestamp, username, website):
            webInfo.append((time, usr, web))
        print("webInfo before sort : ",webInfo)
        print("\n")
            
        # SORT THE WEBSITE INFO BASED ON THE TIMESTAMPS
        # The timestamps may not always be pre-ordered (one of the testcases)
		# Sort first based on user, then time (grouping by user)
		# This also helps to maintain order of websites visited in the later part of the solution
        # To get pattern visited in the same order
        webInfo.sort(key=lambda x:x[0])
        print("webInfo : ",webInfo)
        print("\n")
        
        # FIND THE WEBSITES VISITED BY PARTICULAR USERS
        websiteVisit = defaultdict(list)
        for _, usr, web in webInfo:
            websiteVisit[usr].append(web)
            
        print("websiteVisit: ",websiteVisit)
        print("\n")
        
        
        # FIND THE ROUTES IN THE FORM OF TUPLES OF LENGTH 3
        # A pattern is a list of three websites
        possibleTuples = defaultdict(int)
        for usr in websiteVisit:
            # print("combinations(websiteVisit[usr], 3): ",set(combinations(websiteVisit[usr], 3)))
            # print("\n")
            webRoutes = set(combinations(websiteVisit[usr], 3))
            for webRoute in webRoutes:
                possibleTuples[webRoute] += 1
                
        print("possibleTuples: ",possibleTuples)
        print("\n")
        
        # FIND MAX VALUE OF USERS VISITED
        maxVal = max(possibleTuples.values())
        routes = []
        for r, val in possibleTuples.items():
            if val == maxVal:
                routes.append(r)
        print("routes: ",routes)
                
        if len(routes) > 1:
            # SORTS LEXICOGRAPHICALLY
            routes.sort()
        
         #  If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.
        return routes[0]