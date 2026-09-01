class Solution:
    def trap(self, height: List[int]) -> int:
        def calculateElevation(l, r) -> int:
            elev = 0
            while l < r:
                elev += height[l]
                l += 1
            return elev
        l, r = 0, 0
        total = 0
        elevations = 0
        while l < len(height) - 1:
            r = l + 1
            while r < len(height) and height[r] < height[l]:
                r += 1
            if r >= len(height):
                break
            elevations = calculateElevation(l + 1, r)
            total += min(height[l], height[r]) * (r - l - 1) - elevations
            l = r
        meeting_point = l
        l, r = len(height) - 1, len(height) - 1
        elevations = 0
        totaltwo = 0
        while r > meeting_point:
            l = r - 1
            while l >= meeting_point and height[l] < height[r]:
                l -= 1
            if l < meeting_point:
                break
            elevations = calculateElevation(l + 1, r)
            totaltwo += min(height[r], height[l]) * abs(r - l - 1) - elevations
            r = l

        return total + totaltwo