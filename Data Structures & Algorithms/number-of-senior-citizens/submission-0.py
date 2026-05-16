class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details:
            for i in range(len(passenger)):
                if passenger[i].isalpha():
                    print("We enter here")
                    age = int(passenger[i+ 1: i + 3])
                    print(age)
                    if age > 60:
                        count += 1

        return count
                    