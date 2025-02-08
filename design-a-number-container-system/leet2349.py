class NumberContainers:

    def __init__(self):
        self.container = {}

    def change(self, index: int, number: int) -> None:
        self.container[index] = number

    def find(self, number: int) -> int:
        if number in self.container.values():
            for k in sorted(self.container):
                if self.container[k]==number:
                    return k
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)