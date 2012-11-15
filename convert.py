
def convert_DrawTree_to_graph(tree, scale):
    node_positions = {}
    edge_list = []

    def _helper_tree(node):
        node_positions[id(node)] = (node.x * scale, node.y * scale)
        for child in node.children:
            edge_list.append((id(node), id(child)))
            _helper_tree(child)

    _helper_tree(tree)
    return (node_positions, edge_list)


