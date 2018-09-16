class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        down = max(B, F)
        left = max(A, E)
        right = min(C, G)
        up = min(D, H)
        S = (C - A)*(D - B) + (G - E)*(H - F)
        if right > left and up > down:
            overlap = (right - left) * (up - down)
            return S - overlap
        return S