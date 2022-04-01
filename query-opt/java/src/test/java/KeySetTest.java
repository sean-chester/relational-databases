import A4.KeySet;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class KeySetTest {
    @Test
    @DisplayName("Equality Test")
    public void equalityTest() throws Exception {


        KeySet a = new KeySet(new int[]{2, 3});
        KeySet a_duplicate = new KeySet(new int[]{2, 3});
        KeySet b = new KeySet(new int[]{3, 2});
        KeySet c = new KeySet(new int[]{-1, -1});

        assertEquals(a, a_duplicate);
        assertNotEquals(a, b);
        assertNotEquals(b, c);
    }
}