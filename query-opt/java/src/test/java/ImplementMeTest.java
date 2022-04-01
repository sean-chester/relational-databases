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
        int key = 42;

        Index expectedOutput = new Index();
        expectedOutput.nodes.add(new Node(new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 0})));

        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 02")
    public void testCase02() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 0})));
        int key = 42;

        Index expectedOutput = new Index();
        expectedOutput.nodes.add(new Node(new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 0})));

        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 03")
    public void testCase03() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 0})));
        int key = 99;

        Index expectedOutput = new Index();
        expectedOutput.nodes.add(new Node(new KeySet(new int[]{42, 99}), new PointerSet(new int[]{0, 0, 0})));

        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 04")
    @Description("Insert into full node")
    public void testCase04() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{42, 99}), new PointerSet(new int[]{0, 0, 0})));
        int key = 7;

        Index expectedOutput = new Index();
        expectedOutput.nodes.add(new Node( // node #1
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{1, 2, 0})));
        expectedOutput.nodes.add(new Node( // node #2
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 2})));
        expectedOutput.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, 99}), new PointerSet(new int[]{0, 0, 0})));
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
                new KeySet(new int[]{66, 99}), new PointerSet(new int[]{0, 0, 0})));

        int key = 68;

        Index expectedOutput = new Index(13);
        expectedOutput.nodes.set(0, new Node( // node #1
                new KeySet(new int[]{66, -1}), new PointerSet(new int[]{1, 2, 0})));

        expectedOutput.nodes.set(1, new Node( // node #2
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{4, 5, 0})));

        expectedOutput.nodes.set(2, new Node( // node #3
                new KeySet(new int[]{68, -1}), new PointerSet(new int[]{7, 8, 0})));

        expectedOutput.nodes.set(4, new Node( // node #5
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 5})));

        expectedOutput.nodes.set(5, new Node( // node #6
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 7})));

        expectedOutput.nodes.set(7, new Node( // node #8
                new KeySet(new int[]{66, -1}), new PointerSet(new int[]{0, 0, 8})));

        expectedOutput.nodes.set(8, new Node( // node #9
                new KeySet(new int[]{68, 99}), new PointerSet(new int[]{0, 0, 0})));


        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 06")
    @Description("Insert into full node with full parent, but does not cause a root split")
    public void testCase06() throws Exception {
        Index btree = new Index(); //TODO: Not provided
        int key = 87;

        Index expectedOutput = new Index(); //TODO: Not provided

        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 07")
    @Description("Insertion causes splits that propagates at least three times")
    public void testCase07() throws Exception {
        Index btree = new Index(); //TODO: Not provided
        int key = 87;

        Index expectedOutput = new Index(); //TODO: Not provided

        assertEquals(expectedOutput, ImplementMe.insertIntoIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 08")
    @Description("Lookup key outside range of tree's keys")
    public void testCase08() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{42, 99}), new PointerSet(new int[]{0, 0, 0})));
        int key = 7;

        boolean expectedOutput = false;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 09")
    @Description("Lookup key within tree's range but not in tree")
    public void testCase09() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{42, 99}), new PointerSet(new int[]{0, 0, 0})));
        int key = 66;

        boolean expectedOutput = false;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 10")
    @Description("Boundary case: lookup smallest key in tree")
    public void testCase10() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{42, 99}), new PointerSet(new int[]{0, 0, 0})));
        int key = 42;

        boolean expectedOutput = true;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 11")
    @Description("Boundary case: lookup largest key in tree")
    public void testCase11() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node(new KeySet(new int[]{42, 99}), new PointerSet(new int[]{0, 0, 0})));
        int key = 99;

        boolean expectedOutput = true;

        assertEquals(expectedOutput, ImplementMe.lookupKeyInIndex(btree, key));
    }

    @Test
    @DisplayName("Test Case 12")
    @Description("Lookup key strictly within the tree's range")
    public void testCase12() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node( // node #1
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
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
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.add(new Node( // node #4
                new KeySet(new int[]{66, 99}), new PointerSet(new int[]{0, 0, 0})));

        int lowerBound = 66;
        int upperBound = 87;

        int[] expectedOutput = {66};

        assertEquals(expectedOutput, ImplementMe.rangeSearchInIndex(btree, lowerBound, upperBound));
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
                new KeySet(new int[]{66, 99}), new PointerSet(new int[]{0, 0, 0})));

        int lowerBound = 0;
        int upperBound = 42;

        int[] expectedOutput = {7};

        assertEquals(expectedOutput, ImplementMe.rangeSearchInIndex(btree, lowerBound, upperBound));
    }

    @Test
    @DisplayName("Test Case 15")
    @Description("Range query half-open to the right")
    public void testCase15() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node( // node #1
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.add(new Node( // node #2
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.add(new Node( // node #4
                new KeySet(new int[]{66, 87}), new PointerSet(new int[]{0, 0, 0})));

        int lowerBound = 7;
        int upperBound = 99;

        int[] expectedOutput = {7, 42, 66, 87};

        assertEquals(expectedOutput, ImplementMe.rangeSearchInIndex(btree, lowerBound, upperBound));
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
                new KeySet(new int[]{66, 87}), new PointerSet(new int[]{0, 0, 0})));

        int lowerBound = 7;
        int upperBound = 7;

        int[] expectedOutput = {};

        assertEquals(expectedOutput, ImplementMe.rangeSearchInIndex(btree, lowerBound, upperBound));
    }

    @Test
    @DisplayName("Test Case 17")
    @Description("Multi-leaf range query in middle of tree")
    public void testCase17() throws Exception {
        Index btree = new Index();
        btree.nodes.add(new Node( // node #1
                new KeySet(new int[]{42, 66}), new PointerSet(new int[]{1, 2, 3})));
        btree.nodes.add(new Node( // node #2
                new KeySet(new int[]{7, -1}), new PointerSet(new int[]{0, 0, 2})));
        btree.nodes.add(new Node( // node #3
                new KeySet(new int[]{42, -1}), new PointerSet(new int[]{0, 0, 3})));
        btree.nodes.add(new Node( // node #4
                new KeySet(new int[]{66, 99}), new PointerSet(new int[]{0, 0, 0})));

        int lowerBound = 42;
        int upperBound = 87;

        int[] expectedOutput = {42, 66};

        assertEquals(expectedOutput, ImplementMe.rangeSearchInIndex(btree, lowerBound, upperBound));
    }

    @Test
    @DisplayName("Test Case 18")
    @Description(">>> Not disclosed")
    public void testCase18() throws Exception {
        Index btree = new Index(); // Not disclosed

        boolean expectedOutput = false; // Not disclosed

        assertEquals(expectedOutput, expectedOutput);
    }

    @Test
    @DisplayName("Test Case 19")
    @Description(">>> Not disclosed")
    public void testCase19() throws Exception {
        Index btree = new Index(); // Not disclosed

        boolean expectedOutput = false; // Not disclosed

        assertEquals(expectedOutput, expectedOutput);
    }

    @Test
    @DisplayName("Test Case 20")
    @Description(">>> Not disclosed")
    public void testCase20() throws Exception {
        Index btree = new Index(); // Not disclosed

        boolean expectedOutput = false; // Not disclosed

        assertEquals(expectedOutput, expectedOutput);
    }


}