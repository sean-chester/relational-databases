// Implementation of B+-tree functionality.

import A4.Index;

/**
 * You should implement all of the static functions declared
 * in the ImplementMe class and submit this (and only this!) file.
 */
public class ImplementMe {

    /**
     * Returns a B+-tree obtained by inserting a key into a pre-existing
     * B+-tree index if the key is not already there. If it already exists,
     * the return value is equivalent to the original, input tree.
     * <p>
     * Complexity: Guaranteed to be asymptotically linear in the height of the tree
     * Because the tree is balanced, it is also asymptotically logarithmic in the
     * number of keys that already exist in the index.
     *
     * @param btree
     * @param key
     * @return
     */
    //TODO: Implement me
    public static Index insertIntoIndex(Index btree, int key) {
        return null;
    }

    /**
     * Returns a boolean that indicates whether a given key
     * is found among the leaves of a B+-tree index.
     * <p>
     * Complexity: Guaranteed not to touch more nodes than the
     * height of the tree
     *
     * @param btree
     * @param key
     * @return
     */
    //TODO: Implement me
    public static boolean lookupKeyInIndex(Index btree, int key) {
        return false;
    }

    /**
     * Returns a list of keys in a B+-tree index within the half-open
     * interval [lower_bound, upper_bound)
     * <p>
     * Complexity: Guaranteed not to touch more nodes than the height
     * of the tree and the number of leaves overlapping the interval.
     *
     * @param btree
     * @param lowerBound
     * @param upperBound
     * @return
     */
    //TODO: Implement me
    public static int[] rangeSearchInIndex(Index btree, int lowerBound, int upperBound) {
        return null;
    }
}
