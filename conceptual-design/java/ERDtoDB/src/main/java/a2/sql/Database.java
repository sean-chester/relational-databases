package a2.sql;

import java.util.ArrayList;
import java.util.Collection;

/**
 * A (relational) Database is thus just a collection of Tables.
 */
public class Database extends ArrayList<Table> {
    public Database(int initialCapacity) {
        super(initialCapacity);
    }

    public Database() {
        super();
    }

    public Database(Collection<? extends Table> c) {
        super(c);
    }

    @Override
    public String toString() {
        if (this.isEmpty()) return "";
        StringBuilder builder = new StringBuilder();
        String lineBreak = "";
        for (Table t : this) {
            builder.append(lineBreak);
            builder.append(t.toString());
            lineBreak = "\n";
        }
        return builder.toString();
    }

    @Override
    public int hashCode() {
        int hash = 0;
        for (Table t : this) {
            hash ^= t.hashCode();
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
