import A4.PointerSet;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PointerSetTest {

    @Test
    @DisplayName("Equality Test")
    public void equalityTest() throws Exception {


        PointerSet a = new PointerSet(new int[]{2, 3, 4});
        PointerSet a_duplicate = new PointerSet(new int[]{2, 3, 4});
        PointerSet b = new PointerSet(new int[]{3, 2, 4});
        PointerSet c = new PointerSet(new int[]{0, 0, 0});

        assertEquals(a, a_duplicate);
        assertNotEquals(a, b);
        assertNotEquals(b, c);
    }

}