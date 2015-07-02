from bin_tree import Node
import math

def is_balanced(tree):
    if tree.is_leaf():
        print "Is leaf"
        return True
    print
    print tree.left.height(),
    print tree.right.height(),
    print math.fabs(tree.left.height() - tree.right.height()) > 1
    if (math.fabs(tree.left.height() - tree.right.height())) > 1.0:
        print "returning False"
        return False
    else:
        return is_balanced(tree.left)
        return is_balanced(tree.right)


my_bst = Node()
#print my_bst
print is_balanced(my_bst)
print    
my_bst.insert(6)
#print my_bst
#print "Is it balanced? " + str(is_balanced(my_bst))
my_bst.insert(7)
#print my_bst
#print "Is it balanced? " + str(is_balanced(my_bst))
my_bst.insert(7)
#print my_bst
#print "Is it balanced? " + str(is_balanced(my_bst))
my_bst.insert(2)
print my_bst
#print "Is it balanced? " + str(is_balanced(my_bst))
#my_bst.insert(1)
#print my_bst
print "Is it balanced? " + str(is_balanced(my_bst))
print    
my_bst.insert(1)
#print my_bst
#print "Is it balanced? " + str(is_balanced(my_bst))
my_bst.insert(9)
#print my_bst
#print "Is it balanced? " + str(is_balanced(my_bst))
my_bst.insert(9)
print my_bst
print "Is it balanced? " + str(is_balanced(my_bst))
print    
my_bst.insert(9)
print my_bst
print "Is it balanced? " + str(is_balanced(my_bst))


