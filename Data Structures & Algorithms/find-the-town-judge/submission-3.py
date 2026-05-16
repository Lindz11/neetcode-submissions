class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people_in_town = [0] * 10000
        trust_no_one = set()
        # Loop through every person and we only care about the person that perosn trusts
        for element in trust:
            people_in_town[element[1]] += 1
            trust_no_one.add(element[0])
        
        # See if everyone we have a person in the town everybody else trusts
        for i in range(0, len(people_in_town)):
            if people_in_town[i] == n - 1 and i not in trust_no_one:
                return i
        
        return -1
