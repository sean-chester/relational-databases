import A4.KeySet;
import A4.Node;
import A4.PointerSet;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class NodeTest {

    @Test
    @DisplayName("Equality Tests")
    public void equalityTest() throws Exception {
        Node a = new Node(new KeySet(new int[]{2, 5}), new PointerSet(new int[]{6, 7, 8}));
        Node a_duplicate = new Node(new KeySet(new int[]{2, 5}), new PointerSet(new int[]{6, 7, 8}));
        Node b = new Node(new KeySet(new int[]{5, 2}), new PointerSet(new int[]{8, 7, 6}));
        Node c = new Node(new KeySet(new int[]{-1, -1}), new PointerSet(new int[]{0, 0, 0}));

        assertEquals(a, a_duplicate);
        assertNotEquals(a, b);
        assertNotEquals(b, c);
    }

}