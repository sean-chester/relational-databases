package a2.erd;

import java.util.ArrayList;
import java.util.Collection;

/**
 * A ConnectionList is a collection of Connections, since an Entity Set can be involved in multiple relationships.
 */

public class ConnectionList extends ArrayList<Connection> {
    public ConnectionList(int initialCapacity) {
        super(initialCapacity);
    }

    public ConnectionList() {
        super();
    }

    public ConnectionList(Collection<? extends Connection> c) {
        super(c);
    }

    @Override
    public int hashCode() {
        int hash = 0;
        for (Connection c : this) {
            hash ^= c.hashCode();
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
