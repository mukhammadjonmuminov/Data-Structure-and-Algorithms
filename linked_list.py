class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Linked List Obyekti"""
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """List boshiga tugun qo'shish"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        """Biror tugundan so'ng tugun qo'shish"""
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        # Yangi tugun qo'shamiz
        new_node = Node(new_data)
        # Yangi tugunni keyingi tugunga bog'laymiz
        new_node.next = prev_node.next
        # Avvalgi tugunni yangi tugunga bog'laymiz
        prev_node.next = new_node

    def append(self, new_data):
        """List oxiriga tugun qo'shish"""
        # Yangi tugun yaratamiz
        new_node = Node(new_data)
        # List bo'sh emasligini tekshiramiz
        if self.head is None:
            # Bo'sh bo'lsa yangi tugun list boshi bo'ladi
            self.head = new_node
            return
        # Aks hoda List oxiriga boramiz
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        """Listdan qiymat o'chirish"""
        # List boshini topib olamiz
        global prev
        temp = self.head
        # Birinchi tugunni tekshiramiz
        if (temp and temp.data == key):
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # Agar qiymat topilmasa
        if temp is None:
            return
        # Tugunni listdan o'chiramiz
        prev.next = temp.next
        temp = None





llist = LinkedList()
llist.head = Node("Dushanba")
tuesday = Node("Seshanba")
wednesday = Node("Chorshanba")

llist.head.next = tuesday
tuesday.next = wednesday


