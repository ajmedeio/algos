class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = len(req_skills)
        n = len(people)
        skill_index = {v: i for i, v in enumerate(req_skills)}
        cand = []
        for skills in people:
            val = 0
            for skill in skills:
                val |= 1 << skill_index[skill]
            cand.append(val)

        @cache
        def f(i, acquired):
            if acquired == 0:
                return []
            if i == n:
                return [0] * 100
            return min(f(i+1, acquired), [i] + f(i+1, acquired & ~cand[i]), key=len)
        return f(0, (1 << m) - 1)
