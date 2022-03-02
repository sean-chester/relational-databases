package a2.sql;

import a2.erd.Attribute;
import a2.erd.AttributeSet;

/**
 * A Table is the basic construct of a relational database.
 * It consists of a schema (name and set of attributes)
 * and constraints (primary keys and foreign keys)
 */
public class Table {
    public String name;
    public AttributeSet attributes;
    public Key primaryKey;
    public ForeignKeySet foreignKeys;

    public Table() {
        this.name = "";
        this.attributes = new AttributeSet();
        this.primaryKey = new Key();
        this.foreignKeys = new ForeignKeySet();
    }

    @Override
    public int hashCode() {
        return this.name.hashCode()
                ^ this.attributes.hashCode()
                ^ this.primaryKey.hashCode()
                ^ this.foreignKeys.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        return this.hashCode() == obj.hashCode();
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append("CREATE TABLE `")
                .append(this.name)
                .append("`(")
                .append(this.attributes.toString("INT"));
        if (this.primaryKey != null && this.primaryKey.attributes.size() > 0) {
            builder.append(", PRIMARY KEY(")
                    .append(primaryKey.attributes.toString())
                    .append(")");

        }
        if (this.foreignKeys != null && this.foreignKeys.size() >= 1) {
            for (final ForeignKey fk : foreignKeys) {
                builder.append(", ")
                        .append(fk.toString());
            }
        }
        builder.append(");");

        return builder.toString();
    }

    public Table(String name, AttributeSet attributes, Key primaryKey, ForeignKeySet foreignKeys) {
        this.name = name;
        this.attributes = attributes;
        this.primaryKey = primaryKey;
        this.foreignKeys = foreignKeys;
    }
}
