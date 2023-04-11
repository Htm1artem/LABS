from abc import ABC, abstractmethod

class PriorityQueueInterface(ABC):

    @abstractmethod
    def empty(self) -> bool:
        pass

    @abstractmethod
    def get_length(self) -> int:
        pass

    @abstractmethod
    def add(self, elem) -> None:
        pass

    @abstractmethod
    def delete(self, elem) -> None:
        pass

    @abstractmethod
    def get_max(self) -> None:
        pass

class PriorityQueue(PriorityQueueInterface):

    def __init__(self, *elements) -> None:
        self.container = []
        self.container_length = 0

        for elem in elements:
            self.add(elem)

    def _heapify(self, n, i) -> None:
        while True:
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and self.container[l] > self.container[largest]:
               largest = l

            if r < n and self.container[r] > self.container[largest]:
                largest = r

            if largest == i:
                break

            self.container[i], self.container[largest] = self.container[largest], self.container[i]
            i = largest

    def add(self, elem) -> None:
        if elem not in self.container:
            if self.container_length == 0:
                self.container.append(elem)
                self.container_length = 1
                return

            self.container.append(elem)
            for i in range((self.container_length // 2) - 1, -1, -1):
                self._heapify(self.container_length, i)
            self.container_length += 1

    def delete(self, elem) -> None:
        try:
            self.container.remove(elem)
            self.container_length -= 1
            for i in range((self.container_length // 2) - 1, -1, -1):
                self._heapify(self.container_length, i)
        except ValueError:
            pass

    def get_max(self):
        return self.container[0] if self.container_length else None

    def get_length(self) -> int:
        return self.container_length

    def empty(self) -> bool:
        return self.container_length == 0
    def pop(self):
        if not self.container_length:
            return None

        self.container[0], self.container[-1] = self.container[-1], self.container[0]
        popped_elem = self.container.pop()
        self.container_length -= 1
        self._heapify(self.container_length, 0)

        return popped_elem