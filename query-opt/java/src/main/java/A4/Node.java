package A4;

/**
 * A B+-tree node consists of a set of keys and pointers. If this is a leaf
 * node, all pointers should be sentinel values (-1). If this is a directory
 * node, only those pointers that correspond to child sub-trees should be non-zero.
 */

public class Node {
    public KeySet keys;
    public PointerSet pointers;

    public Node(KeySet keys, PointerSet pointers) throws Exception {
        if (keys == null || pointers == null) {
            throw new Exception("arguments for A4.Node constructor must not be null");
        }
        this.keys = keys;
        this.pointers = pointers;
    }

    public Node() throws Exception {
        this.keys = new KeySet();
        this.pointers = new PointerSet();
    }

    @Override
    public String toString() {
        return "N[" + keys.toString() + " | " + pointers.toString() + "]";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Node otherNode = (Node) o;
        return this.keys.equals(otherNode.keys) && this.pointers.equals(otherNode.pointers);
    }

    @Override
    public int hashCode() {
        return this.keys.hashCode() ^ this.pointers.hashCode();
    }
}
