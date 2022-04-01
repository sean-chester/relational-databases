package A4;

/**
 * Defines the set of pointers in a ternary B+-tree. These should point to array
 * indices at which the children can be found, or use the 0 sentinel value in the
 * i'th position iff there is no (i+1)'st child. Order, again, is important.
 */

public class PointerSet {
    // must contain three and only three values
    public int[] pointers;

    public PointerSet(int[] pointers) throws Exception {
        if (pointers != null && pointers.length != 3) {
            throw new Exception("A4.PointerSet must not be null and have a length of 3");
        }
        this.pointers = pointers;
    }

    public PointerSet() {
        pointers = new int[]{0, 0, 0};
    }

    @Override
    public String toString() {
        return "P(" + pointers[0] + ", " + pointers[1] + ", " + pointers[2] + ")";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        PointerSet otherKeySet = (PointerSet) o;
        return (this.pointers[0] == otherKeySet.pointers[0])
                && (this.pointers[1] == otherKeySet.pointers[1])
                && (this.pointers[2] == otherKeySet.pointers[2]);
    }

    @Override
    public int hashCode() {
        return (pointers[0] * Constant.PRIME) ^ (pointers[1] * Constant.PRIME) ^ (pointers[2] * Constant.PRIME);
    }
}
