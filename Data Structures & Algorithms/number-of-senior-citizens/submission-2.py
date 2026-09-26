class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num_of_old_passengers = 0
        for passenger in details:
            for i in range(0, len(passenger)):
                if passenger[i].isalpha():
                    age = passenger[i+ 1: i + 3]
                    if  int(age) > 60:
                        num_of_old_passengers += 1
        
        return num_of_old_passengers