class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corner_set = set()
        area = 0
        for rec in rectangles:
            top_left = (rec[0], rec[1])
            top_right = (rec[0], rec[3])
            bottom_left = (rec[2], rec[1])
            bottom_right = (rec[2], rec[3])
            area += (rec[2] - rec[0]) * (rec[3] - rec[1])
            for c in [top_left, top_right, bottom_left, bottom_right]:
                if c not in corner_set:
                    corner_set.add(c)
                else:
                    corner_set.remove(c)
        if len(corner_set) != 4:
            return False
        corner_set = sorted(corner_set)
        bottom_left = corner_set[0]
        top_right = corner_set[-1]

        return area == (top_right[0] - bottom_left[0]) * (top_right[1] - bottom_left[1])