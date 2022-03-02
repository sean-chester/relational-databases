package a2.sql;

import a2.erd.AttributeSet;

import java.util.Objects;

/**
 * A key is a subset of attributes (or columns) that uniquely identify each row of a table.
 */
public class Key {
    // columns (or attributes) that are part of the key (or primary key)
    public AttributeSet attributes;

    public Key() {
        this.attributes = new AttributeSet();
    }

    public Key(AttributeSet keys) {
        this.attributes = keys;
    }

    @Override
    public int hashCode() {
        return this.attributes.hashCode();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        return this.hashCode() == o.hashCode();
    }


}
