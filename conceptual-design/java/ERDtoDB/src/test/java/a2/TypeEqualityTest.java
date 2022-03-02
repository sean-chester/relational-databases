package a2;

import a2.erd.*;
import a2.sql.Key;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;


import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class TypeEqualityTest {

    @Test
    @DisplayName("Attribute Equality Check")
    @Tag("equality")
    void attributeEquality() {
        Attribute a = new Attribute("A");
        Attribute a_replica = new Attribute("A");
        Attribute b = new Attribute("B");

        // object state/content check (aka equal() method)
        assertEquals(a, a);
        assertEquals(a, a_replica);
        assertNotEquals(a, b);

        // object identity check (aka == operator)
        assertSame(a, a); // a == a
        assertNotSame(a, a_replica); // a != a_replica
        assertNotSame(a, b); // a != b
    }

    @Test
    @DisplayName("AttributeSet Equality Check")
    @Tag("equality")
    void attributeSetEquality() {
        AttributeSet a_ordered = new AttributeSet(List.of(
                new Attribute("A"),
                new Attribute("B"),
                new Attribute("C"),
                new Attribute("D"),
                new Attribute("E")
        ));

        AttributeSet a_unordered = new AttributeSet(List.of(
                new Attribute("D"),
                new Attribute("C"),
                new Attribute("B"),
                new Attribute("A"),
                new Attribute("E")
        ));

        AttributeSet b = new AttributeSet(List.of(
                new Attribute("A"),
                new Attribute("B"),
                new Attribute("C")
        ));

        // object state/content check (aka equal() method)
        assertEquals(a_ordered, a_ordered);
        assertEquals(a_ordered, a_unordered);
        assertNotEquals(a_ordered, b);

        // object identity check (aka == operator)
        assertSame(a_ordered, a_ordered); // a_ordered == a_ordered
        assertNotSame(a_ordered, a_unordered); // a_ordered != a_unordered
        assertNotSame(a_ordered, b); // a_ordered != b
    }

    @Test
    @DisplayName("Connection Equality Check")
    @Tag("equality")
    void connectionEquality() {
        Connection a = new Connection(new Relationship("R1", new AttributeSet(), new Key()), Multiplicity.MANY);
        Connection a_replica = new Connection(new Relationship("R1", new AttributeSet(), new Key()), Multiplicity.MANY);
        Connection b = new Connection(new Relationship("R1", new AttributeSet(), new Key()), Multiplicity.ONE);
        Connection c = new Connection(new Relationship("R2", new AttributeSet(), new Key()), Multiplicity.ONE);

        // object state/content check (aka equal() method)
        assertEquals(a, a);
        assertEquals(a, a_replica);
        assertNotEquals(a, b);
        assertNotEquals(b, c);

        // object identity check (aka == operator)
        assertSame(a, a); // a == a
        assertNotSame(a, a_replica); // a != a_replica
        assertNotSame(a, b); // a != b
    }

}


