import A4.Index;
import A4.KeySet;
import A4.Node;
import A4.PointerSet;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class IndexTest {
    @Test
    @DisplayName("Equality Test")
    public void equalityTest() throws Exception {


        Index a = new Index();
        a.nodes.add(new Node(new KeySet(new int[]{2, 5}), new PointerSet(new int[]{6, 7, 8})));
        a.nodes.add(new Node(new KeySet(new int[]{6, 7}), new PointerSet(new int[]{11, 12, 13})));
        a.nodes.add(new Node(new KeySet(new int[]{80, 70}), new PointerSet(new int[]{101, 102, 103})));

        Index a_duplicate = new Index();
        a_duplicate.nodes.add(new Node(new KeySet(new int[]{2, 5}), new PointerSet(new int[]{6, 7, 8})));
        a_duplicate.nodes.add(new Node(new KeySet(new int[]{6, 7}), new PointerSet(new int[]{11, 12, 13})));
        a_duplicate.nodes.add(new Node(new KeySet(new int[]{80, 70}), new PointerSet(new int[]{101, 102, 103})));


        // same nodes as A, but in wrong order
        Index b = new Index();
        b.nodes.add(new Node(new KeySet(new int[]{6, 7}), new PointerSet(new int[]{11, 12, 13})));
        b.nodes.add(new Node(new KeySet(new int[]{80, 70}), new PointerSet(new int[]{101, 102, 103})));
        b.nodes.add(new Node(new KeySet(new int[]{2, 5}), new PointerSet(new int[]{6, 7, 8})));

        Index c = new Index();
        c.nodes.add(new Node(new KeySet(new int[]{-1, -1}), new PointerSet(new int[]{0, 0, 0})));
        c.nodes.add(new Node(new KeySet(new int[]{80, 70}), new PointerSet(new int[]{101, 102, 103})));
        c.nodes.add(new Node(new KeySet(new int[]{55, 6}), new PointerSet(new int[]{6, 10, 8})));



        assertEquals(a, a_duplicate);
        assertNotEquals(a, b);
        assertNotEquals(b, c);
    }

}