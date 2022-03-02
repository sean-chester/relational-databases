package a2.erd;

import java.util.ArrayList;
import java.util.Collection;

/**
 * A collection of entity sets.
 */

public class EntitySetList extends ArrayList<EntitySet> {
    public EntitySetList(int initialCapacity) {
        super(initialCapacity);
    }

    public EntitySetList() {
        super();
    }

    public EntitySetList(Collection<? extends EntitySet> c) {
        super(c);
    }

    @Override
    public int hashCode() {
        int hash = 0;
        for (EntitySet e : this) {
            hash ^= e.hashCode();
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
