import A4.Index;
import A4.KeySet;
import A4.Node;
import A4.PointerSet;
import jdk.jfr.Description;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ImplementMeTest {

    @Test
    @DisplayName("Test Case 01")
    public void testCase01() throws Exception {
        Index btree = new Index();
        int key = 99;

        Index expectedOutput = new Index();
        expectedOutput.nodes.add(new Node(new KeySet(new int[]{99, -1}), new PointerSet(new int[]{0, 0, 0})));

        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 02")
    public void testCase02() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{99, -1}), new PointerSet(new int[]{0, 0, 0})));
        int key = 99;

        Index expectedOutput = new Index();
        expectedOutput.nodes.add(new Node(new KeySet(new int[]{99, -1}), new PointerSet(new int[]{0, 0, 0})));

        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 03")
    public void testCase03() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{87, -1}), new PointerSet(new int[]{0, 0, 0})));
        int key = 66;

        Index expectedOutput = new Index();
        expectedOutput.nodes.add(new Node(new KeySet(new int[]{66, 87}), new PointerSet(new int[]{0, 0, 0})));

        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 04")
    @Description("Insert into full node")
    public void testCase04() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{66, 99}), new PointerSet(new int[]{0, 0, 0})));
        int key = 87;

        Index expectedOutput = new Index();
        expectedOutput.nodes.add(new Node( // node #1
                new KeySet(new int[]{87, -1}), new PointerSet(new int[]{1, 2, 0})));
        expectedOutput.nodes.add(new Node( // node #2
                new KeySet(new int[]{66, -1}), new PointerSet(new int[]{0, 0, 2})));
        expectedOutput.nodes.add(new Node( // node #3
                new KeySet(new int[]{87, 99}), new PointerSet(new int[]{0, 0, 0})));
        expectedOutput.nodes.add(new Node()); // node #4

        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 05")
    @Description("Insert into full node with full parent, causing root split")
    public void testCase05() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node( // node #1
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.add(new Node( // node #2
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.add(new Node( // node #4
                new KeySet(new int[]{66, 87}), new PointerSet(new int[]{0, 0, 0})));

        int key = 99;

        Index expectedOutput = new Index(13);
        expectedOutput.nodes.set(0, new Node( // node #1
                new KeySet(new int[]{66, -1}), new PointerSet(new int[]{1, 2, 0})));

        expectedOutput.nodes.set(1, new Node( // node #2
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{4, 5, 0})));

        expectedOutput.nodes.set(2, new Node( // node #3
                new KeySet(new int[]{87, -1}), new PointerSet(new int[]{7, 8, 0})));

        expectedOutput.nodes.set(4, new Node( // node #5
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 5})));

        expectedOutput.nodes.set(5, new Node( // node #6
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 7})));

        expectedOutput.nodes.set(7, new Node( // node #8
                new KeySet(new int[]{66, -1}), new PointerSet(new int[]{0, 0, 8})));

        expectedOutput.nodes.set(8, new Node( // node #9
                new KeySet(new int[]{87, 99}), new PointerSet(new int[]{0, 0, 0})));


        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 06")
    @Description("Insert into full node with full parent, but does not cause a root split")
    public void testCase06() throws Exception {
        Index btree = new Index(13);
        btree.nodes.set(0, new Node( // node #1
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{1, 2, 0})));
        btree.nodes.set(2, new Node( // node #3
                new KeySet(new int[]{27, 66}), new PointerSet(new int[]{7, 8, 9})));
        btree.nodes.set(6, new Node( // node #7
                new KeySet(new int[]{11, 11}), new PointerSet(new int[]{0, 0, 90})));
        btree.nodes.set(7, new Node( // node #8
                new KeySet(new int[]{7, 9}), new PointerSet(new int[]{0, 0, 8})));
        btree.nodes.set(8, new Node( // node #9
                new KeySet(new int[]{27, -1}), new PointerSet(new int[]{0, 0, 9})));
        btree.nodes.set(9, new Node( // node #10
                new KeySet(new int[]{66, 88}), new PointerSet(new int[]{0, 0, 0})));

        int key = 12;

        Index expectedOutput = new Index(13);
        expectedOutput.nodes.set(0, new Node( // node #1
                new KeySet(new int[]{7, 27}), new PointerSet(new int[]{1, 2, 3})));

        expectedOutput.nodes.set(2, new Node( // node #3
                new KeySet(new int[]{9, -1}), new PointerSet(new int[]{7, 8, 0})));

        expectedOutput.nodes.set(3, new Node( // node #4
                new KeySet(new int[]{66, -1}), new PointerSet(new int[]{10, 11, 0})));

        expectedOutput.nodes.set(6, new Node( // node #7
                new KeySet(new int[]{11, 11}), new PointerSet(new int[]{0, 0, 90})));

        expectedOutput.nodes.set(7, new Node( // node #8
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 8})));

        expectedOutput.nodes.set(8, new Node( // node #9
                new KeySet(new int[]{9, 12}), new PointerSet(new int[]{0, 0, 10})));

        expectedOutput.nodes.set(10, new Node( // node #11
                new KeySet(new int[]{27, -1}), new PointerSet(new int[]{0, 0, 11})));

        expectedOutput.nodes.set(11, new Node( // node #12
                new KeySet(new int[]{66, 88}), new PointerSet(new int[]{0, 0, 0})));


        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 07")
    @Description("Insertion causes splits that propagates at least three times")
    public void testCase07() throws Exception {
        Index btree = new Index(13);
        btree.nodes.set(0, new Node( // node #1
                new KeySet(new int[]{7, 99}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.set(2, new Node( // node #3
                new KeySet(new int[]{27, 66}), new PointerSet(new int[]{7, 8, 9})));
        btree.nodes.set(7, new Node( // node #8
                new KeySet(new int[]{7, 9}), new PointerSet(new int[]{0, 0, 8})));
        btree.nodes.set(8, new Node( // node #9
                new KeySet(new int[]{27, -1}), new PointerSet(new int[]{0, 0, 9})));
        btree.nodes.set(9, new Node( // node #10
                new KeySet(new int[]{66, 88}), new PointerSet(new int[]{0, 0, 0})));

        int key = 12;

        Index expectedOutput = new Index(40);
        expectedOutput.nodes.set(0, new Node( // node #1
                new KeySet(new int[]{27, -1}), new PointerSet(new int[]{1, 2, 0})));

        expectedOutput.nodes.set(1, new Node( // node #2
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{4, 5, 0})));

        expectedOutput.nodes.set(2, new Node( // node #3
                new KeySet(new int[]{99, -1}), new PointerSet(new int[]{7, 8, 0})));

        expectedOutput.nodes.set(5, new Node( // node #6
                new KeySet(new int[]{9, -1}), new PointerSet(new int[]{16, 17, 0})));

        expectedOutput.nodes.set(7, new Node( // node #8
                new KeySet(new int[]{66, -1}), new PointerSet(new int[]{22, 23, 0})));

        expectedOutput.nodes.set(16, new Node( // node #17
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 17})));

        expectedOutput.nodes.set(17, new Node( // node #18
                new KeySet(new int[]{9, 12}), new PointerSet(new int[]{0, 0, 22})));

        expectedOutput.nodes.set(22, new Node( // node #23
                new KeySet(new int[]{27, -1}), new PointerSet(new int[]{0, 0, 23})));

        expectedOutput.nodes.set(23, new Node( // node #24
                new KeySet(new int[]{66, 88}), new PointerSet(new int[]{0, 0, 0})));


        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 08")
    @Description("Lookup smallest key in tree")
    public void testCase08() throws Exception {
        Index btree = new Index(4);
        btree.nodes.set(0, new Node(
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.set(1, new Node(
                new KeySet(new int[]{9, -1}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.set(2, new Node(
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.set(3, new Node(
                new KeySet(new int[]{66, 7}), new PointerSet(new int[]{0, 0, 0})));

        int key = 9;

        boolean expectedOutput = true;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 09")
    @Description("Lookup largest key in tree")
    public void testCase09() throws Exception {
        Index btree = new Index(4);
        btree.nodes.set(0, new Node(
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.set(1, new Node(
                new KeySet(new int[]{7, 99}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.set(2, new Node(
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.set(3, new Node(
                new KeySet(new int[]{66, 87}), new PointerSet(new int[]{0, 0, 0})));

        int key = 87;

        boolean expectedOutput = true;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 10")
    @Description("Boundary case: lookup outside range of tree's keys")
    public void testCase10() throws Exception {
        Index btree = new Index(4);
        btree.nodes.set(0, new Node(
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.set(1, new Node(
                new KeySet(new int[]{9, -1}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.set(2, new Node(
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.set(3, new Node(
                new KeySet(new int[]{66, 99}), new PointerSet(new int[]{0, 0, 0})));

        int key = 7;

        boolean expectedOutput = false;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 11")
    @Description("Lookup key within tree's range but not in tree")
    public void testCase11() throws Exception {
        Index btree = new Index(4);
        btree.nodes.set(0, new Node(
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.set(1, new Node(
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.set(2, new Node(
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.set(3, new Node(
                new KeySet(new int[]{66, 9}), new PointerSet(new int[]{0, 0, 0})));

        int key = 9;

        boolean expectedOutput = false;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 12")
    @Description("Lookup key strictly within the tree's range")
    public void testCase12() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node( // node #1
                new KeySet(new int[]{41, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.add(new Node( // node #2
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.add(new Node( // node #4
                new KeySet(new int[]{66, 99}), new PointerSet(new int[]{0, 0, 0})));

        int key = 42;

        boolean expectedOutput = true;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 13")
    @Description("Range query fully contained in one leaf node")
    public void testCase13() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node( // node #1
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.add(new Node( // node #2
                new KeySet(new int[]{7, 68}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.add(new Node( // node #4
                new KeySet(new int[]{66, 99}), new PointerSet(new int[]{0, 0, 0})));

        int lowerBound = 66;
        int upperBound = 87;

        int[] expectedOutput = {66};

        assertArrayEquals(expectedOutput, ImplementMe.rangeSearchInIndex(btree, lowerBound, upperBound));
    }

    @Test
    @DisplayName("Test Case 14")
    @Description("Range query half-open to the left ")
    public void testCase14() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node( // node #1
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.add(new Node( // node #2
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.add(new Node( // node #4
                new KeySet(new int[]{66, 9}), new PointerSet(new int[]{0, 0, 0})));

        int lowerBound = 0;
        int upperBound = 42;

        int[] expectedOutput = {7};

        assertArrayEquals(expectedOutput, ImplementMe.rangeSearchInIndex(btree, lowerBound, upperBound));
    }

    @Test
    @DisplayName("Test Case 15")
    @Description("Range query half-open to the right")
    public void testCase15() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node( // node #1
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.add(new Node( // node #2
                new KeySet(new int[]{7, 68}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.add(new Node( // node #4
                new KeySet(new int[]{66, 87}), new PointerSet(new int[]{0, 0, 0})));

        int lowerBound = 42;
        int upperBound = 99;

        int[] expectedOutput = {42, 66, 87};

        assertArrayEquals(expectedOutput, ImplementMe.rangeSearchInIndex(btree, lowerBound, upperBound));
    }

    @Test
    @DisplayName("Test Case 16")
    @Description("Range query with matching upper and lower bound ")
    public void testCase16() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node( // node #1
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.add(new Node( // node #2
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.add(new Node( // node #4
                new KeySet(new int[]{66, 7}), new PointerSet(new int[]{0, 0, 0})));

        int lowerBound = 7;
        int upperBound = 7;

        int[] expectedOutput = {};

        assertArrayEquals(expectedOutput, ImplementMe.rangeSearchInIndex(btree, lowerBound, upperBound));
    }

    @Test
    @DisplayName("Test Case 17")
    @Description("Multi-leaf range query in middle of tree")
    public void testCase17() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node( // node #1
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.add(new Node( // node #2
                new KeySet(new int[]{68, -1}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.add(new Node( // node #4
                new KeySet(new int[]{66, 99}), new PointerSet(new int[]{0, 0, 0})));

        int lowerBound = 42;
        int upperBound = 87;

        int[] expectedOutput = {42, 66};

        assertArrayEquals(expectedOutput, ImplementMe.rangeSearchInIndex(btree, lowerBound, upperBound));
    }

    @Test
    @DisplayName("Test Case 18")
    @Description("Lookup recently added key")
    public void testCase18() throws Exception {
        Index btree = new Index(13);
        btree.nodes.set(0, new Node(
                new KeySet(new int[]{7, 99}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.set(2, new Node(
                new KeySet(new int[]{27, 66}), new PointerSet(new int[]{7, 8, 9})));
        btree.nodes.set(7, new Node(
                new KeySet(new int[]{7, 9}), new PointerSet(new int[]{0, 0, 8})));
        btree.nodes.set(8, new Node(
                new KeySet(new int[]{27, -1}), new PointerSet(new int[]{0, 0, 9})));
        btree.nodes.set(9, new Node(
                new KeySet(new int[]{66, 88}), new PointerSet(new int[]{0, 0, 0})));

        int key = 12;

        boolean expectedOutput = true;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(
                ImplementMe.insertIntoIndex(btree, key), key));
    }

    @Test
    @DisplayName("Test Case 19")
    @Description("Lookup range that includes recently added key")
    public void testCase19() throws Exception {
        Index btree = new Index(13);
        btree.nodes.set(0, new Node(
                new KeySet(new int[]{7, 99}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.set(2, new Node(
                new KeySet(new int[]{27, 66}), new PointerSet(new int[]{7, 8, 9})));
        btree.nodes.set(7, new Node(
                new KeySet(new int[]{7, 9}), new PointerSet(new int[]{0, 0, 8})));
        btree.nodes.set(8, new Node(
                new KeySet(new int[]{27, -1}), new PointerSet(new int[]{0, 0, 9})));
        btree.nodes.set(9, new Node(
                new KeySet(new int[]{66, 88}), new PointerSet(new int[]{0, 0, 0})));

        int key = 12;
        int lowerBound = 12;
        int upperBound = 66;

        int[] expectedOutput = {12, 27};

        assertArrayEquals(expectedOutput, ImplementMe.rangeSearchInIndex(
                ImplementMe.insertIntoIndex(btree, key), lowerBound, upperBound));
    }

    @Test
    @DisplayName("Test Case 20")
    @Description("Lookup range with nearly matching lower and upper bound equal to recently added key")
    public void testCase20() throws Exception {
        Index btree = new Index(13);
        btree.nodes.set(0, new Node(
                new KeySet(new int[]{7, 99}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.set(2, new Node(
                new KeySet(new int[]{27, 66}), new PointerSet(new int[]{7, 8, 9})));
        btree.nodes.set(7, new Node(
                new KeySet(new int[]{7, 9}), new PointerSet(new int[]{0, 0, 8})));
        btree.nodes.set(8, new Node(
                new KeySet(new int[]{27, -1}), new PointerSet(new int[]{0, 0, 9})));
        btree.nodes.set(9, new Node(
                new KeySet(new int[]{66, 88}), new PointerSet(new int[]{0, 0, 0})));

        int key = 12;
        int lowerBound = 12;
        int upperBound = 13;

        int[] expectedOutput = {12};

        assertArrayEquals(expectedOutput, ImplementMe.rangeSearchInIndex(
                ImplementMe.insertIntoIndex(btree, key), lowerBound, upperBound));
    }

    @Test
    @DisplayName("Test Case B1")
    @Description("Look up a key in an empty tree")
    public void testCase20() throws Exception {
        Index btree = new Index();

        int key = 9;

        boolean expectedOutput = false;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case B2")
    @Description("Insert in order")
    public void testCase20() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{66, -1}), new PointerSet(new int[]{0, 0, 0})));
        int key = 87;

        Index expectedOutput = new Index();
        expectedOutput.nodes.add(new Node(new KeySet(new int[]{66, 87}), new PointerSet(new int[]{0, 0, 0})));

        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }


    @Test
    @DisplayName("Test Case B3")
    @Description("Look up a key inserted into a tree with only one element")
    public void testCase20() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 0})));
        int key = 12;

        boolean expectedOutput = true;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(
                ImplementMe.insertIntoIndex(btree, key), key);
    }


    @Test
    @DisplayName("Test Case B4")
    @Description("Range query that doesn't overlap tree at all")
    public void testCase20() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node( // node #1
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.add(new Node( // node #2
                new KeySet(new int[]{7, 87}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.add(new Node( // node #4
                new KeySet(new int[]{66, 68}), new PointerSet(new int[]{0, 0, 0})));

        int lowerBound = 87;
        int upperBound = 99;

        int[] expectedOutput = {};

        assertArrayEquals(expectedOutput, ImplementMe.rangeSearchInIndex(btree, lowerBound, upperBound));
    }

}