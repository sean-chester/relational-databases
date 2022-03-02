package a2.erd;

import java.util.HashMap;

/**
 * An Entity-Relationship Diagram (ERD) is simply the collection of entity sets, relationships, and attributes thereon.
 */

public class ERD {
    public RelationshipList relationships;
    public EntitySetList entitySets;

    public ERD() {
        relationships = new RelationshipList();
        entitySets = new EntitySetList();
    }

    public ERD(RelationshipList relationships, EntitySetList entitySets) {
        this.relationships = relationships;
        this.entitySets = entitySets;
    }

    @Override
    public int hashCode() {
        return relationships.hashCode() ^ entitySets.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        return this.hashCode() == obj.hashCode();
    }
}
