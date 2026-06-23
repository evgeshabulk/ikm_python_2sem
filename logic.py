class OfficialNode:
    def __init__(self, obj_id, bribe):
        self.id = obj_id
        self.bribe = bribe
        self.first_child = None
        self.next_sibling = None

class MinistryTree:
    def __init__(self):
        self.nodes = {} 
        self.root = None

    def add_official(self, obj_id, boss_id, bribe):
        if bribe < 0:
            raise ValueError(f"Размер взятки не может быть отрицательным (ID: {obj_id}).")
            
        new_node = OfficialNode(obj_id, bribe)
        self.nodes[obj_id] = new_node

        if boss_id == 0:
            if self.root is not None:
                raise ValueError("Обнаружено более одного главного чиновника.")
            self.root = new_node
        else:
            if boss_id not in self.nodes:
                self.nodes[boss_id] = OfficialNode(boss_id, 0)
                
            boss_node = self.nodes[boss_id]
            if boss_node.first_child is None:
                boss_node.first_child = new_node
            else:
                current = boss_node.first_child
                while current.next_sibling is not None:
                    current = current.next_sibling
                current.next_sibling = new_node
                
        if obj_id in self.nodes and self.nodes[obj_id].bribe == 0 and bribe != 0:
            self.nodes[obj_id].bribe = bribe

    def find_min_bribe_path(self):
        if not self.root:
            raise ValueError("В министерстве отсутствует главный чиновник (корень).")
        cost, path = self._calculate_min_recursive(self.root)
        return cost, path

    def _calculate_min_recursive(self, node):
        if not node:
            return 0, []
            
        if node.first_child is None:
            return node.bribe, [node.id]

        min_child_cost = float('inf')
        best_child_path = []

        current_child = node.first_child
        while current_child is not None:
            child_cost, child_path = self._calculate_min_recursive(current_child)
            if child_cost < min_child_cost:
                min_child_cost = child_cost
                best_child_path = child_path
            current_child = current_child.next_sibling

        total_cost = node.bribe + min_child_cost
        best_child_path.append(node.id) 
        
        return total_cost, best_child_path