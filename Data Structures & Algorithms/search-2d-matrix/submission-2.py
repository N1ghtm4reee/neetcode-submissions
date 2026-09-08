class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, rr = 0, len(matrix) - 1
        column_length = len(matrix[0])
        while lr <= rr:
            mr = lr + (rr - lr) // 2
            if target >= matrix[mr][0] and target <= matrix[mr][column_length - 1]:
                arr = matrix[mr]
                lc = 0
                rc = column_length - 1
                while lc <= rc:
                    mc = lc + (rc - lc) // 2
                    if arr[mc] == target:
                        return True
                    elif arr[mc] > target:
                        rc = mc - 1
                    else:
                        lc = mc + 1
                break
            elif target >= matrix[mr][column_length - 1]:
                lr = mr + 1
            else:
                rr = mr - 1
        return False
