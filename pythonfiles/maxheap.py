class MaxHeap:
    def __init__(self):
        """
        Initialize an empty MaxHeap.

        Attributes:
            heap (list): List to store the elements of the heap.
        """
        self.heap = []

    def parent(self, i):
        """
        Get the index of the parent of the element at index i.

        Args:
            i (int): Index of the element.

        Returns:
            int: Index of the parent of the element at index i.
        """
        return (i - 1) // 2

    def left_child(self, i):
        """
        Get the index of the left child of the element at index i.

        Args:
            i (int): Index of the element.

        Returns:
            int: Index of the left child of the element at index i.
        """
        return 2 * i + 1

    def right_child(self, i):
        """
        Get the index of the right child of the element at index i.

        Args:
            i (int): Index of the element.

        Returns:
            int: Index of the right child of the element at index i.
        """
        return 2 * i + 2

    def swap(self, i, j):
        """
        Swap the elements at indices i and j in the heap.

        Args:
            i (int): Index of the first element.
            j (int): Index of the second element.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        """
        Insert an item into the heap.

        Args:
            item: Item to be inserted into the heap.
        """
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        """
        Restore the heap property going up from the specified index.

        Args:
            i (int): Index to start the heapify process from.
        """
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_max(self):
        """
        Extract the maximum element from the heap.

        Returns:
            The maximum element.
        """
        if len(self.heap) == 0:
            return "Heap is empty"
        if len(self.heap) == 1:
            return self.heap.pop()

        max_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max_element

    def heapify_down(self, i):
        """
        Restore the heap property going down from the specified index.

        Args:
            i (int): Index to start the heapify process from.
        """
        left = self.left_child(i)
        right = self.right_child(i)
        largest = i

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.swap(i, largest)
            self.heapify_down(largest)

    def get_max(self):
        """
        Get the maximum element from the heap.

        Returns:
            The maximum element.
        """
        return self.heap[0]

    def display(self):
        """
        Display the elements of the heap.

        Returns:
            The list representation of the heap.
        """
        return self.heap



# Time Complexity:
# Insertion (insert): O(log n)
# Extraction of maximum (extract_max): O(log n)
# Get maximum (get_max): O(1)
# Space Complexity:
# Space required for the heap data structure: O(n)


max_heap = MaxHeap()
max_heap.insert(20)
max_heap.insert(30)
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(15)

print("Max Heap:", max_heap.display())  # [30, 20, 10, 5, 15]

print("Extract Max:", max_heap.extract_max())  # 30

print("Max Heap after extracting max:", max_heap.display())  # [20, 15, 10, 5]
