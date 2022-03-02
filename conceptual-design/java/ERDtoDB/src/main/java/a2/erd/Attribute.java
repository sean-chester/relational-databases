package a2.erd;

/**
 * An attribute of either an Entity Set or a Relationship in an ERD
 */
public class Attribute {
    public String name;

    public Attribute(String name) {
        this.name = name;
    }

    @Override
    public int hashCode() {
        return this.name.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        return this.hashCode() == obj.hashCode();
    }
}

