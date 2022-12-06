from collections import Counter
class Solution:
    def substringAnagrams(self, strs):
        len_str = len(strs)
        anagram = []
        start = 0

        while start < len_str:
            for i in range(start+1, len_str - 1):
                np = strs[ start : i+1]
                # print("np: ",np)
                ns = strs[start+1 : len_str]
                # print("ns: ",ns)

                all_anagram = self.findAllAnagram(ns, np)
                # print(all_anagram)

                if not all_anagram:
                    continue

                for i in range(len(all_anagram)):
                    anagram.append(all_anagram[i])
            
            start += 1
            # print("\n")

        # Flatten lists of list
        # result = []
        # for pairs in anagram:
        #     for pair in pairs:
        #         result.append(pair)
        result = [pair for pairs in anagram for pair in pairs]
        return result

    def findAllAnagram(self, s, p):
        op = []
        ns = len(s)
        np = len(p)
        
        counter_p = Counter(p)
        counter_s = Counter()

        # print(counter_p)

        for i in range(ns):
            counter_s[s[i]] += 1

            if i >= np:
                idx_to_remove = i - np
                
                if counter_s[s[idx_to_remove]] == 0:
                    del counter_s[s[idx_to_remove]]
                else:
                    counter_s[s[idx_to_remove]] -= 1

            if counter_p == counter_s:
                window_to_append = i - np + 1
                res = [p ,s[window_to_append : i+1] ]
                op.append(res)
                # print("op: ",op)

        # print("op: ",op)
        return op

            

if __name__ == '__main__':
    S = Solution()
    ip = 'abccba'
    print(S.substringAnagrams(ip))

    # result List : ab ba bc cb abc cba bcc ccb abcc ccba abccb bccba