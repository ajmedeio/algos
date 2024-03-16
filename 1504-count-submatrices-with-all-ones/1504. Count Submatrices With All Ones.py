class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n, cnt = len(mat), len(mat[0]), 0
        for i, row in enumerate(mat): # Iterate through the rows
            # Pre-processing current row by iterating through the columns, skipped for first row
            for j in range(n):
                if i and row[j]:
                    row[j] += mat[i-1][j]
            
            # Now row[j] stores maximum consecutive 1s counting upward from row i.
            # Can try to imagine row[j] as the height of `1s matrix` standing on row i.
            # Can also imagine those `1s matrices` as buildings.
            stack, sub = [-1], 0 # store height stack and submatrices count, respectively
                                 # -1 is placeholder element for convenience.
            for j, h in enumerate(row): # Iterate through the `1s matrices`
                # In each iteration we append current building to the stack,
                # adding its contribution to submatrices when it is the rightmost building. 
                # Before that, make sure its height is larger than the one on the top of the 
                # stack. So that we can be sure  the stack is monotonically increasing, and for
                # any neighboring building, `stack[k] - stack[k-1]` is the width of the buildings.
                while stack[-1] >= 0 and row[stack[-1]] >= h:
                    # If not so(appending current building will break the monotonicity), pop the stack and subtract possible submatrices contributed by
                    # the popped building as right boundary. The reason doing so is because we have
                    # to remove the effect of appending it previously. Note that `j0-stack[-1]` is
                    # the width of the buildings, as in `j-stack[-1]` when adding.
                    j0 = stack.pop()
                    sub -= row[j0] * (j0-stack[-1])
                # Adding the contribution and then appending the building.
                sub += h * (j-stack[-1])
                cnt += sub
                stack.append(j)
        return cnt