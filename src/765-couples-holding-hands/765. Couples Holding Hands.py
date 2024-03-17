class Solution:
    def minSwapsCouples(self, A: List[int]) -> int:
        n = len(A)
        id_to_pos = {}
        n_swaps = 0
        
        for i in range(n):
            id_to_pos[A[i]] = i

        for i in range(0, n, +2):
            rando_pos, rando_id = i+1, A[i+1]
            partner_id = A[i]+1 if A[i] % 2 == 0 else A[i]-1
            if rando_id != partner_id:
                # need to swap this rando next to me with my partner
                partner_pos = id_to_pos[partner_id]
                A[rando_pos], A[partner_pos] = A[partner_pos], A[rando_pos]
                id_to_pos[rando_id], id_to_pos[partner_id] = partner_pos, rando_pos
                n_swaps += 1
        return n_swaps
