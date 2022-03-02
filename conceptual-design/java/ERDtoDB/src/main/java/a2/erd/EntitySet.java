package a2.erd;

import a2.sql.Key;

/**
 * An Entity Set corresponds to some abstract object or thing.
 * It is described by a name and set of attributes as well as the connections it has to other entity sets.
 * The regular, IsA, and supporting relationships are separated into distinct collections.
 */
public class EntitySet {
    public String name;
    public AttributeSet attributes;
    public Key primaryKey;
    public ConnectionList connections;
    public ParentList parents;
    public SupportingRelationshipList supportingRelations;

    public EntitySet(String name, AttributeSet attributes, Key primaryKey, ConnectionList connections, ParentList parents,
                     SupportingRelationshipList supportingRelations) {
        this.name = name;
        this.attributes = attributes;
        this.primaryKey = primaryKey;
        this.connections = connections;
        this.parents = parents;
        this.supportingRelations = supportingRelations;
    }

    public EntitySet() {
        this.name = "";
        this.attributes = new AttributeSet();
        this.connections = new ConnectionList();
        this.parents = new ParentList();
        this.supportingRelations = new SupportingRelationshipList();
    }

    @Override
    public int hashCode() {
        return name.hashCode()
                ^ attributes.hashCode()
                ^ primaryKey.hashCode()
                ^ connections.hashCode()
                ^ parents.hashCode()
                ^ supportingRelations.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        return this.hashCode() == obj.hashCode();
    }
}
