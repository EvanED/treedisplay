
def convert_DrawTree_to_graph(tree, scale):
    node_specs = {}
    edge_list = []

    def _helper_tree(node):
        node_specs[id(node)] = {
            "position": (node.x * scale, node.y * scale)
            }
        for child in node.children:
            edge_list.append((id(node), id(child)))
            _helper_tree(child)

    _helper_tree(tree)
    return (node_specs, edge_list)


