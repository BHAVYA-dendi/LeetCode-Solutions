class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        ans=[]
        for person in people:
            ans.insert(person[1],person)
        return ans
