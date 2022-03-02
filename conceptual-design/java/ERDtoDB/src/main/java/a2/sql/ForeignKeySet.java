package a2.sql;

import a2.erd.EntitySet;

import java.util.ArrayList;
import java.util.Collection;

/**
 * Provides a container for multiple foreign keys
 */
public class ForeignKeySet extends ArrayList<ForeignKey> {
    public ForeignKeySet(int initialCapacity) {
        super(initialCapacity);
    }

    public ForeignKeySet() {
        super();
    }

    public ForeignKeySet(Collection<? extends ForeignKey> c) {
        super(c);
    }

    @Override
    public int hashCode() {
        int hash = 0;
        for (ForeignKey fk : this) {
            hash ^= fk.hashCode();
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
