package A4;

/**
 * Defines the set of keys in a ternary B+-tree. Observe that there are always
 * two such keys, though some may hold the sentinel value of -1.
 * The only member variable is a 2-tuple of integer values. Order is important.
 */
public class KeySet {
    // must contain two and only two values
    public int[] keys;

    public KeySet(int[] keys) throws Exception {
        if (keys != null && keys.length != 2) {
            throw new Exception("A4.KeySet must not be null and have a length of 2");
        }
        this.keys = keys;
    }

    public KeySet() {
        keys = new int[]{-1, -1};
    }

    @Override
    public String toString() {
        return "K(" + keys[0] + ", " + keys[1] + ")";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        KeySet otherKeySet = (KeySet) o;
        return (this.keys[0] == otherKeySet.keys[0]) && (this.keys[1] == otherKeySet.keys[1]);
    }

    @Override
    public int hashCode() {
        return (keys[0] * Constant.PRIME) ^ (keys[1] * Constant.PRIME);
    }
}
