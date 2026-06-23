class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CustomStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return value

    def is_empty(self):
        return self.top is None

class GameGraph:
    def __init__(self):
        self.adj = {}          # Список смежности: узел -> стек слов
        self.in_degree = {}    # Входящие степени вершин
        self.out_degree = {}   # Исходящие степени вершин
        self.total_words = 0

    def get_last_char(self, word):
        if word.endswith('ь') and len(word) > 1:
            return word[-2]
        return word[-1]

    def add_word(self, word):
        word = word.lower().strip()
        if not word:
            return
        
        start_char = word[0]
        end_char = self.get_last_char(word)
        
        if start_char not in self.adj:
            self.adj[start_char] = CustomStack()
        if end_char not in self.adj:
            self.adj[end_char] = CustomStack()
            
        self.adj[start_char].push(word)
        
        self.out_degree[start_char] = self.out_degree.get(start_char, 0) + 1
        self.in_degree[end_char] = self.in_degree.get(end_char, 0) + 1
        self.in_degree[start_char] = self.in_degree.get(start_char, 0)
        self.out_degree[end_char] = self.out_degree.get(end_char, 0)
        self.total_words += 1

    def check_eulerian_circuit(self):
        for node in self.out_degree:
            if self.in_degree.get(node, 0) != self.out_degree.get(node, 0):
                return False
        return True

    def find_chain(self):
        if self.total_words == 0:
            return []
            
        if not self.check_eulerian_circuit():
            raise ValueError("Цепочка невозможна: степени букв не совпадают.")

        start_node = None
        for node, count in self.out_degree.items():
            if count > 0:
                start_node = node
                break
                
        if not start_node:
            return []

        stack = CustomStack()
        stack.push((start_node, None))
        circuit_words = []
        
        while not stack.is_empty():
            curr_node, _ = stack.top.value
            
            if curr_node in self.adj and not self.adj[curr_node].is_empty():
                next_word = self.adj[curr_node].pop()
                next_node = self.get_last_char(next_word)
                stack.push((next_node, next_word))
            else:
                _, popped_edge = stack.pop()
                if popped_edge is not None:
                    circuit_words.append(popped_edge)
                    
        circuit_words.reverse()
        
        if len(circuit_words) != self.total_words:
            raise ValueError("Цепочка невозможна: набор слов распадается на несвязные группы.")
            
        return circuit_words

def process_words(words_list):
    """Функция-фасад для вызова из main.py."""
    graph = GameGraph()
    for word in words_list:
        graph.add_word(word)
    return graph.find_chain()