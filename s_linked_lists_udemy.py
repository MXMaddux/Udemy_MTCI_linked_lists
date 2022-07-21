class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printl(self):
        temp_node = self.head
        while temp_node != None:
            print(temp_node.data, end=' ')
            temp_node = temp_node.next
        print()
        print('Length = '+str(self.length))

    def remove(self, index):
        i = 0
        temp_node = self.head
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        if index > self.length:
            print("Index out of range. Can't delete shit.")
        while i < self.length:
            if i == index - 1:
                self.temp_node.next = self.temp_node.next.next
                self.length -= 1
                break
            temp_node = temp_node.next
            i += 1

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return self

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return self

    def insert(self, index, data):
        new_node = Node(data)
        i = 0
        temp_node = self.head
        if index >= self.length:
            self.append(data)
            return
        if index == 0:
            self.prepend(data)
            return
        while i < self.length:
            if i == index-1:
                temp_node.next, new_node.next = new_node, temp_node.next
                self.length += 1
                break
            temp_node = temp_node.next
            i += 1

    def remove(self, index):
        temp_node = self.head
        i = 0
        if index >= self.length:
            print("Entered wrong index")

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        while i < self.length:
            if i == index-1:
                temp_node.next = temp_node.next.next
                self.length -= 1
                break
            i += 1
            temp_node = temp_node.next

    def reverse(self):
        if not self.head.next:
            return self.head
        prev_node = None
        self.tail = self.head
        while self.head != None:
            temp_node = self.head
            self.head = self.head.next
            temp_node.next = prev_node
            prev_node = temp_node
        self.head = temp_node
        return self

    def contains(self, val):
        temp_node = self.head
        while temp_node:
            if temp_node.data == val:
                print("True")
                return True
            temp_node = temp_node.next
        print("False")
        return False

    def max(self):
        max = 0
        temp_node = self.head
        while temp_node:
            if temp_node.data > max:
                max = temp_node.data
            temp_node = temp_node.next
        print(max)
        return max

    def min(self):
        max = 0
        min = 0
        temp_node = self.head
        while temp_node:
            if temp_node.data > max:
                max = temp_node.data
                min = max
                break
        while temp_node:
            if temp_node.data < min:
                min = temp_node.data
            temp_node = temp_node.next
        print(min)

    def avg(self):
        sum_nums = 0
        length = 0
        temp_node = self.head
        while temp_node:
            sum_nums += temp_node.data
            temp_node = temp_node.next
            length += 1
        average = sum_nums/length
        print(average)
        return average


ll1 = LinkedList()
ll1.append(10)
ll1.append(5)
ll1.append(16)
ll1.prepend(1)
# ll1.insert(2, 76)
# ll1.insert(99, 20)
# ll1.print_ll()
# ll1.remove(1)
# ll1.reverse()
# ll1.contains(5)
# ll1.printl()
# ll1.max()
# ll1.min()
ll1.avg()
