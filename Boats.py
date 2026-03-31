class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        s = len(people)
        r = []
        i = 0
        j = s - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                r.append((people[i], people[j]))
                i += 1
                j -= 1
            else:
                r.append((people[j],))
                j -= 1
        return len(r)
