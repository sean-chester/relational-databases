package a2.erd;

/**
 * A Connection specifies a relationship and a Multiplicity and corresponds to where an arrow meets an entity set
 */
public class Connection {
    public Relationship relationship;
    public Multiplicity multiplicity;

    public Connection() {
        relationship = new Relationship();
        multiplicity = Multiplicity.UNDEFINED;
    }

    public Connection(Relationship relationship, Multiplicity multiplicity) {
        this.relationship = relationship;
        this.multiplicity = multiplicity;
    }

    @Override
    public int hashCode() {
        return this.multiplicity.hashCode() ^ this.relationship.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        return this.hashCode() == obj.hashCode();
    }
}
