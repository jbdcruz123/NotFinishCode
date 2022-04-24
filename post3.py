# Created by: Nino Dulay

from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    data: Any
    next: Node = None

class LinkedList:
    def __init__(self):
        self.head = None   

    def __str__(self):
        return f"This Linked List contains {len(self)} elements\n{self.printNodes()}"

    def __len__(self) -> int:
        currentNode = self.head
        count = 0
        while currentNode:
            count += 1
            currentNode = currentNode.next
        print(f"L10 count {count}")
        return count

    def push(self, newnode):
        if self.head:
            newnode.next = self.head
            self.head = newnode
        else:
            self.head = newnode

    def addNode(self, node: Node) -> None:
        if self.head:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = node
        else:
            self.head = node

    def insertNode(self, pos: int, newnode: Node) -> None:
        if pos == 0:
            if self.head:
                newnode.next = self.head
                self.head = newnode
            else:
                self.head = newnode
        elif pos == len(self):
            self.addNode(newnode)
        else:
            # Traverse to the said position 
            count = 1 # Converted to 1 as we need to get the previous node before the said position
            currentNode = self.head
            while count != pos:
                currentNode = currentNode.next
                count += 1

            # Add the new node 
            nextnode = currentNode.next # Get the position node, assign to variable
            currentNode.next = newnode # Get the previous node before the said position, assign the new node next to it
            newnode.next = nextnode # Re link the new node to the previous node in the n position

    def printNodes(self) -> str:
        currentNode = self.head
        result = ""
        while currentNode:
            result += str(currentNode.data) + " -> "
            currentNode = currentNode.next
        print(result)

    def deleteNode(self, pos: int) -> None:
        temp = None
        if pos == 0:
            if len(self) == 0:
                raise Exception('No need to delete, there are no nodes in this Linked List')
            else:
                if self.head:
                    temp = self.head.next
                    self.head = temp
                else:
                    raise Exception('No need to delete, there are no nodes in this Linked List')
        
        elif pos == len(self):
            # Traverse to the said last position 
            count = 2 # Converted to 2 as we need to get the previous node before the said position (the very last node is a None, so we need to backtrack two times)
            currentNode = self.head
            while count != pos:
                currentNode = currentNode.next
                count += 1

            # Delete the next node by just clearing the next address to the node of the current node
            currentNode.next = None

        else:
            # Traverse to the said position 
            count = 1 # Converted to 1 as we need to get the previous node before the said position
            currentNode = self.head
            while count != pos:
                currentNode = currentNode.next
                count += 1

            # Delete the new node and reconnect
            newConnectedNode = currentNode.next.next
            currentNode.next = newConnectedNode

ll = LinkedList()

while 1:
    print(f"\n\n********************\nlinked list Testing \nq to quit, a add, p Display, d Delete, i insert\n******************")	
    inputV= input()
	    
    if inputV == "q":
        print("\n\npaalis na ng program...", end ="")
        input()
        break
    elif inputV == "a":
        print(f"\n\ninput data para sa add:  ", end="")
        inputV = input()
        inputNode = Node(int(inputV))
        ll.addNode(inputNode)
    elif inputV == "p":
        print("\n\nDisplay all:  ")
        ll.printNodes()
		
    elif inputV == "d":
        print(f"\n\ninput index para i-delete:  ", end="")
        inputV = input()
        ll.deleteNode(int(inputV))
	
    elif inputV == "i":
        print(f"\n\ninput index para i-insert:  ", end="")
        inputV = input()
        print(f"\n\ninput data para i-insert:  ", end="")
        inputDataV = input()
        inputNode = Node(int(inputDataV))
        ll.insertNode(int(inputV), inputNode)
	   	
	








