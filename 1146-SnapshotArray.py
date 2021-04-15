class SnapshotArray:

    def __init__(self, length: int):
        self.cur_ver = 0
        self.snapArr = [[(-1, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.snapArr[index].append((self.cur_ver, val))

    def snap(self) -> int:
        self.cur_ver += 1
        return self.cur_ver - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.snapArr[index], (snap_id + 1, 0)) - 1
        return self.snapArr[index][i][1]