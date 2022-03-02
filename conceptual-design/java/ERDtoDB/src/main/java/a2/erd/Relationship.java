package a2.erd;

import a2.sql.Key;

/**
 * A relationship in an ERD that connects at least two (not necessarily distinct)
 * entity sets. This class does not specify any connections, just the name of the
 * relationship and any attributes attached thereto.
 */
public class Relationship {
    public String name;
    public AttributeSet attributes;
    public Key primaryKey;

    public Relationship(String name, AttributeSet attributes, Key primaryKey) {
        this.name = name;
        this.attributes = attributes;
        this.primaryKey = primaryKey;
    }

    public Relationship(String name) {
        this.name = name;
        this.attributes = new AttributeSet();
        this.primaryKey = new Key();
    }

    public Relationship() {
        this.name = "";
        this.attributes = new AttributeSet();
        this.primaryKey = new Key();
    }

    @Override
    public int hashCode() {
        return name.hashCode() ^ attributes.hashCode() ^ primaryKey.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        return this.hashCode() == obj.hashCode();
    }
}
