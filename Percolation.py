"""
Percolation.py
Brianna Brost
5/5/2023
Create forest, set it on fire, see if it gets to the other side, determine probabilites of it getting to other side from its density, do calcs with that info and graph the probabilities vs densities
"""
import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, v, n):
        """
            Description of Function:
                initialize value and next
            Parameters:
                v: value
                n: node
            Return:
                None
        """
        self.value = v
        self.next = n

    def __repr__(self):
        """
            Description of Function: 
                returns value
            Parameters: 
                None
            Return: 
                str
        """
        return f"{self.value}"
    
    def __eq__(self, other):
        """
            Description of Function: 
                compares two nodes
            Parameters:
                other: node
            Return:
                bool
        """
        return self.value == other.value

    def __str__(self):
        """
            Description of Function: 
                returns string representation of node
            Parameters: 
                None
            Return: 
                str
        """
        return str(self.value)

class SinglyLinkedList:
    def __init__(self):
        """
            Description of Function:
                initialize empty list
            Parameters:
                None
            Return:
                None
        """
        self.head = None
        self.size = 0
    
    def __str__(self):
        """
            Description of Function: 
                return string representing list
            Parameters: 
                None
            Return: 
                str
        """
        if self.head is None:
            return '[]'
        result = '['
        temp_node = self.head
        while temp_node.next is not None:
            result += str(temp_node) + " "
            temp_node = temp_node.next
        return result + str(temp_node) + ']'
    
    def first(self):
        """
            Description of Function:
                returns first value in list
            Parameters:
                None
            Return:
                int?
        """
        return self.head.value
    
    def get_size(self)->int:
        """
            Description of Function: 
                return size of list
            Parameters: 
                None
            Return: 
                int
        """
        return self.size

    def is_empty(self)->bool:
        """
            Description of Function: 
                returns True if list empty, false if not
            Parameters: 
                None
            Return: 
                bool
        """
        return self.head is None

    def add_first(self, v):  
        """
            Description of Function: 
                adds the value v at the head of the list
            Parameters:
                value
            Return:
                None
        """  
        new_node = Node(v, self.head)
        self.head = new_node
        self.size += 1

    def add_last(self, v):
        """
            Description of Function:
                adds v at tail of list
            Parameters:
                v:value
            Return:
                None
        """
        new_node = Node(v, None)
        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next 
            temp_node.next = new_node
        self.size += 1
        
    def remove_first(self):
        """
            Description of Function:
                remove and return first value in list
            Parameters:
                None
            Return:
                value that was removed
        """
        if self.head is None:
            raise ValueError("List is empty.")
        return_value = self.head.value
        self.head = self.head.next
        self.size -=1
        return return_value
    
    def remove_last(self):
        """
            Description of Function:
                remove and return last value in list
            Parameters:
                None
            Return:
                value that was removed
        """
        if self.head is None:
            raise ValueError("List is empty.")          
        return_value = None
        if self.head.next is None:
                return_value = self.head.value
                self.head = None
        else: 
            temp_node = self.head
            while temp_node.next.next is not None:
                temp_node = temp_node.next          
            return_value = temp_node.next.value
            temp_node.next = None
        self.size -= 1   
        return return_value
    
    def get(self, index: int):
        """
            Description of Function:
                return value stored at given index position
            Parameters:
                index
            Return:
                value at given index
        """
        if index >= self.size:
            raise IndexError("Index is out of range.")
        idx_value = 0
        temp_node = self.head
        while True:
            if idx_value == index:
                return temp_node.value
            temp_node = temp_node.next
            idx_value += 1       
    
    def remove_at_index(self, index: int):
        """
            Description of Function:
                removes node at index from list, return its value
            Parameters:
                index
            Return:
                value and desired index
        """
        if self.head is None:
            raise ValueError("List is empty.")  
        if index >= self.size:
            raise IndexError("Index is out of range.")
            self.size -= 1
        idx_value = 0
        current_node = self.head
        while idx_value <= index:
            node_before = current_node
            current_node = current_node.next
            idx_value += 1
            if index == 0:
                deleted_value = self.head.value
                self.head = self.head.next
                return deleted_value
            elif idx_value == index:
                deleted_value = current_node.value
                node_before.next = current_node.next
                return deleted_value

class Stack:
    def __init__(self):
        """
            Description of Function:
                initializes empty singley-linked list for stack
            Parameters:
                None
            Return:
                None
        """
        self.the_stack = SinglyLinkedList()
    
    def push(self, e):
        """
            Description of Function:
                adds a node to the top of the stack
            Parameters:
                e: the value of the node
            Return:
                None
        """
        return self.the_stack.add_first(e)

    def pop(self):
        """
            Description of Function:
                remove and return value of top element of the stack
            Parameters:
                None
            Return:
                the generic type E of the top element
        """
        return self.the_stack.remove_first()

    def top(self):
        """
            Description of Function:
                returns the value of the top element of the stack, 
                without removing it from the stack
            Parameters:
                None
            Return:
                the generic type E of the top element
        """
        return self.the_stack.first()

    def get_size(self):
        """
            Description of Function:
                return number elements in the stack
            Parameters:
                None
            Return:
                int
        """
        return self.the_stack.get_size()

    def is_empty(self):
        """
            Description of Function:
                return True is the stack is empty, False otherwise
            Parameters:
                None
            Return:
                bool
        """
        return self.the_stack.is_empty()

class Queue:
    def __init__(self):
        """
            Description of Function:
                initializes an empty signely-linked list for the queueueue
            Parameters:
                None
            Return:
                None
        """
        self.the_queue = SinglyLinkedList()
    
    def enqueue(self, e):
        """
            Description of Function:
                adds an element e to the back of the queue
            Parameters:
                e: the value of the element
            Return:
                None
        """
        return self.the_queue.add_last(e)

    def dequeue(self):
        """
            Description of Function:
                remove and return value of the first element of the queue
            Parameters:
                None
            Return:
                the generic type E of the first element
        """
        return self.the_queue.remove_first()

    def first(self):
        """
            Description of Function:
                returns the value of the first element of the queue, 
                without removing it from the queue
            Parameters:
                None
            Return:
                the generic type E of the first element
        """
        return self.the_queue.first()

    def get_size(self):
        """
            Description of Function:
                return number elements in the queue
            Parameters:
                None
            Return:
                int
        """
        return self.the_queue.get_size()

    def is_empty(self):
        """
            Description of Function:
                return True is the queue is empty, False otherwise
            Parameters:
                None
            Return:
                bool
        """
        return self.the_queue.is_empty()

class Forest:
 
    forest = [[]]
    width = int(20)
    length = int(20)

    def __init__(self, d: float, width = width, length = length) -> None:
        """
        Description of Function:
            creates 2d list of 1-tree 0-empty with probablitly of (1-d)
        Parameters:
            width: int; width of the grid, length: int; length of the grid, d: float; density of the forest
        Return:
            None
        """
        self.forest = np.random.choice(2, size = (width, length), p = [(1 - d), d])

    def __str__(self) -> str:
        """
        Description of Function:
            returns a string representation of the two-dimensional array
        Parameters:
            None
        Return:
            str
        """
        return str(self.forest)

    def depth_first_search(self):
        """
        Description of Function:
            true if fire makes it to bottom false if no, store in stack
        Parameters:
            None
        Return:
            bool
        """
        cells_to_explore=Stack()
        for i in range(self.width):
            if self.forest[0][i] == 1:
                self.forest[0][i]=2
                cells_to_explore.push(Cell(0, i))

        while not cells_to_explore.is_empty():
            current_cell=cells_to_explore.pop()
            if current_cell.row==self.length-1:
                return True
            for j,i in [(current_cell.row+1,current_cell.col), (current_cell.row-1,current_cell.col),(current_cell.row,current_cell.col+1),(current_cell.row,current_cell.col-1)]:
                if i>0 and i<self.length and j>0 and j<self.width and self.forest[j][i]==1:
                    self.forest[j][i]=2
                    cells_to_explore.push(Cell(j,i))
        return False

    def breadth_first_search(self):
        """
        Description of Function:
            true if fire spread false if no, store in queueueueue
        Parameters:
            None
        Return:
            bool
        """
        cells_to_explore=Queue()
        for i in range(self.width):
            if self.forest[0][i] == 1:
                self.forest[0][i]=2
                cells_to_explore.enqueue(Cell(0, i))

        while not cells_to_explore.is_empty():
            current_cell=cells_to_explore.dequeue()
            if current_cell.row==self.length-1:
                return True
            for j,i in [(current_cell.row+1,current_cell.col), (current_cell.row-1,current_cell.col),(current_cell.row,current_cell.col+1),(current_cell.row,current_cell.col-1)]:
                if i>0 and i<self.length and j>0 and j<self.width and self.forest[j][i]==1:
                    self.forest[j][i]=2
                    cells_to_explore.enqueue(Cell(j,i))

        return False
        
class Cell:
    def __init__(self, row, col):
        """
        Description of Function:
            contains a row and column value
        Parameters:
            row: int; row value
            col: int; col value
        Return:
            None
        """
        self.row=row
        self.col=col

#Part II:
class Fire_Probability:
    def fire_spread_probability_dfs(density)-> float:
        """
        Description of Function:
            finds probability of fire success of specified density using depth first search
        Parameters:
            density
        Return:
            float
        """
        fire_spread_count=0
        for i in range(100):
            f=Forest(density)
            if f.depth_first_search()== True:
                fire_spread_count+=1
        fire_spread_prob=fire_spread_count/100
        return fire_spread_prob

    def fire_spread_probability_bfs(density)->float:
        """
        Description of Function:
            finds probability of fire success of specified density using breadth first search
        Parameters:
            density
        Return:
            float
        """
        fire_spread_count=0
        for i in range(100):
            f=Forest(density)
            if f.breadth_first_search()==True:
                fire_spread_count+=1
        fire_spread_prob=fire_spread_count/100
        return fire_spread_prob

    def highest_density_dfs()->float:
        """
        Description of Function:
            finds the maximum density of the forest that the prob of fire spreading in density is less than .5 - dfs
        Parameters:
            None
        Return:
            float
        """
        low_density = 0.0
        high_density = 1.0
        for i in range(20):
            density=(high_density+low_density)/2.0
            p=Fire_Probability.fire_spread_probability_dfs(density)
            if p<0.5:
                low_density=density
            else:
                high_density=density
        return density

    def highest_density_bfs()->float:
        """
        Description of Function:
            finds the maximum density of the forest that the prob of fire spreading in density is less than .5 - bfs
        Parameters:
            None
        Return:
            float
        """
        low_density = 0.0
        high_density = 1.0
        for i in range(20):
            density=(high_density+low_density)/2.0
            p=Fire_Probability.fire_spread_probability_bfs(density)
            if p<0.5:
                low_density=density
            else:
                high_density=density
        return density

def graph():
    """
    Description of Function:
        graphs probability of fire spread vs density of forest
    Parameters:
        None
    Return:
        None but makes the graphs
    """
    densities=[]
    probabilities_bfs=[]
    probabilities_dfs=[]
    # computer sucks so i did 100 not 1000 or 10000, computer would have exploded
    for density in range(1, 100):
        density_value=density/100
        densities.append(density_value)
        probabilities_bfs.append(Fire_Probability.fire_spread_probability_bfs(density_value))
        probabilities_dfs.append(Fire_Probability.fire_spread_probability_dfs(density_value))
    plt.plot(densities, probabilities_bfs)
    plt.title("Probability of Fire Spreading in Density Breadth First")
    plt.xlabel("Densities")
    plt.ylabel("Probability")
    plt.show()
    plt.plot(densities, probabilities_dfs)
    plt.title("Probability of Fire Spreading in Density Depth First")
    plt.xlabel("Densities")
    plt.ylabel("Probability")
    plt.show()

def driver():
    """
    Description of Function:
        tests the functions
    Parameters:
        None
    Return:
        None but prints stuff
    """
    dfs=Forest(.6)
    print(dfs)
    print(dfs.breadth_first_search())
    print(dfs)
    print(Fire_Probability.fire_spread_probability_dfs(0.6))
    print(Fire_Probability.highest_density_dfs())
    bfs=Forest(.6)
    print(bfs)
    print(bfs.depth_first_search())
    print(bfs)
    print(Fire_Probability.fire_spread_probability_bfs(0.6))
    print(Fire_Probability.highest_density_bfs())

driver()
graph()
