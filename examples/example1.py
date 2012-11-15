import sys
from PyQt4 import QtCore, QtGui
import treedisplay
import treelayout

class Tree:
    def __init__(self, node="", *children):
        self.node = node
        self.width = len(node)
        if children: self.children = children
        else:        self.children = []
    
    def __str__(self): 
        return "%s" % (self.node)
    def __repr__(self):
        return "%s" % (self.node)

    def __getitem__(self, key):
        if isinstance(key, int) or isinstance(key, slice): 
            return self.children[key]
        if isinstance(key, str):
            for child in self.children:
                if child.node == key: return child

    def __iter__(self): return self.children.__iter__()

    def __len__(self): return len(self.children)

the_tree = Tree("root", 
  Tree("l1", 
    Tree("l2", 
      Tree("l3", 
        Tree("l4", 
          Tree("l5"),
          Tree("l6")),
        Tree("l7")),
      Tree("l8")),
    Tree("l9")),
  Tree("r1", 
    Tree("r2", 
      Tree("r3"),
      Tree("r4")),
    Tree("r5")))


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    QtCore.qsrand(QtCore.QTime(0,0,0).secsTo(QtCore.QTime.currentTime()))

    the_tree = treelayout.layout(the_tree)
    graph = treedisplay.convert_DrawTree_to_graph(the_tree, 50)
    print(graph)

    widget = treedisplay.GraphWidget(graph)
    widget.show()

    sys.exit(app.exec_())
