class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        sums = sum([(1 - k & 1)*k for k in A])
        for k,i in queries:
            if k & 1 == 0:
                if A[i] & 1 == 0:
                    sums += k
            else:
                if A[i] & 1 !=0:
                    sums += (A[i] + k)
                else:
                    sums -= A[i]
            A[i] += k
            result.append(sums)
        return result
