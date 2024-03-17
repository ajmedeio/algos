class Solution:
    def wiggleSort(self, A: List[int]) -> None:
        n = len(A)
        A.sort()
        median = A[n // 2]

        get = lambda i: (2*i + 1) % (n|1)
        lt, eq, gt = 0, 0, n-1
        while eq <= gt:
            if A[get(eq)] > median:
                A[get(eq)], A[get(lt)] = A[get(lt)], A[get(eq)]
                eq += 1
                lt += 1
            elif A[get(eq)] < median:
                A[get(eq)], A[get(gt)] = A[get(gt)], A[get(eq)]
                gt -= 1
            else:
                eq += 1
