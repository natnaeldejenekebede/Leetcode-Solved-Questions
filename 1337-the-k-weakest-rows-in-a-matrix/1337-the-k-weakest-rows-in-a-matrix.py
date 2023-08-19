class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_strengths = [(sum(row), idx) for idx, row in enumerate(mat)]
        row_strengths.sort()
        return [idx for _, idx in row_strengths[:k]]
