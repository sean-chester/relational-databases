package a2.erd;

import java.util.ArrayList;
import java.util.Collection;

/**
 * A collection of relationships
 */
public class RelationshipList extends ArrayList<Relationship> {
    public RelationshipList(int initialCapacity) {
        super(initialCapacity);
    }

    public RelationshipList() {
        super();
    }

    public RelationshipList(Collection<? extends Relationship> c) {
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
