package A4;

import java.util.ArrayList;
import java.util.Objects;

/**
 * Definition of a Linearised B+-tree index class with fan-out 3
 * The keys are unsigned (i.e., non-negative) integers.
 * <p>
 * This is a *linearised* tree, i.e., it is implemented as an array rather
 * than with pointers. As you have seen in previous classes, one can
 * implement a binary tree of height *h* with an array of length *2^h-1* as follows:
 * * the root (if it exists) is at index 0
 * * the left child of the node at index i is at 2i + 1
 * * the right child of the node at index i is at 2i + 2
 * This corresponds to a breadth-first search of a full binary tree.
 * <p>
 * In this assignment, you will use a fan-out of three, i.e., a ternary tree.
 * We can apply the same logic, and represent a ternary tree of height *h*
 * with an array of length *(1-3^h)/-2* as follows:
 * * the root (if it exists) is at index 0
 * * the left child of the node at index i is at 3i + 1
 * * the middle child of the node at index i is 3i + 2
 * * the right child of the node at index i is at 3i + 3
 * This corresponds to a breadth-first search of a full ternary tree.
 * <p>
 * This B+-tree class does not have any (non-builtin) member functions,
 * but all member variables are public. You will implement the functionality
 * in another (implementation) file.
 * <p>
 * <p>
 * A B+-tree index is thus just an ordered list of nodes. Array position
 * implies position in the tree. The length of the list should be exactly
 * *3^h*, where *h* is the height of the tree. The last nodes may very well be
 * full of nothing but sentinel values (-1 for keys and 0 for pointers).
 */
public class Index {
    public ArrayList<Node> nodes;

    public Index(ArrayList<Node> nodes) {
        this.nodes = nodes;
    }

    public Index() {
        this.nodes = new ArrayList<>();
    }

    /**
     * generates a B-tree with numNodes empty nodes
     *
     * @param numNodes
     */
    public Index(int numNodes) throws Exception {
        this.nodes = new ArrayList<>(numNodes);
        for (int i = 0; i < numNodes; i++) {
            this.nodes.add(new Node());
        }
    }

    @Override
    public String toString() {
        StringBuilder buff = new StringBuilder();
        buff.append("I{");
        String affix = "";
        for (Node n : this.nodes) {
            buff.append(affix);
            buff.append(n.toString());
            affix = ", ";
        }
        buff.append("}");
        return buff.toString();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Index otherIndex = (Index) o;
        if (this.nodes.size() != otherIndex.nodes.size()) return false;
        for (int i = 0; i < this.nodes.size(); i++) {
            // order is important
            if (!this.nodes.get(i).equals(otherIndex.nodes.get(i))) return false;
        }
        return true;
    }

    @Override
    public int hashCode() {
        return Objects.hash(nodes);
    }
}
