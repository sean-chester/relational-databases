package a2.erd;

import java.util.ArrayList;
import java.util.Collection;

/**
 * A specialised connection list in which the multiplicity is dropped because all relationships are "IsA" relationships.
 */

public class ParentList extends ArrayList<Relationship> {
    public ParentList(int initialCapacity) {
        super(initialCapacity);
    }

    public ParentList() {
        super();
    }

    public ParentList(Collection<? extends Relationship> c) {
        super(c);
    }

    @Override
    public int hashCode() {
        int hash = 0;
        for (Relationship r : this) {
            hash ^= r.hashCode();
        }
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        return this.hashCode() == obj.hashCode();
    }
}
