package a2.sql;

import a2.erd.AttributeSet;
import a2.erd.EntitySet;

/**
 * A Foreign Key is a special type of key that uniquely identifies
 * a row in a different table. It subclasses a Key because it is a
 * subset of attributes (or columns) in this table, but those attributes can be
 * referenced in a separate table
 */

public class ForeignKey extends Key {


    /**
     * An ordered list of attributes in this table to which the FK is applied
     * this is implemented in the {@link Key} superclass as the {@link Key.attributes} member variable
     **/

    /**
     * The table that the foreign key should reference to
     */
    public Table referencedTable;

    /**
     * An ordered list of attributes in the foreign table that are being referenced
     */
    public AttributeSet referencedAttributes;

    public ForeignKey(AttributeSet attributeKeys, Table referencedTable, AttributeSet referencedAttributes) {
        super(attributeKeys);
        this.referencedTable = referencedTable;
        this.referencedAttributes = referencedAttributes;
    }

    /**
     * generates a SQL script for this foreign key in the format below:
     * example: FOREIGN KEY(`A`, `B`) REFERENCES `foreign_table`(`X`, `Y`)
     *
     * @return String
     */
    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();

        builder.append("FOREIGN KEY(")
                .append(super.attributes.toString())
                .append(") REFERENCES `")
                .append(this.referencedTable.name)
                .append("`(")
                .append(this.referencedAttributes.toString())
                .append(")");

        return builder.toString();
    }

    @Override
    public int hashCode() {
        return attributes.hashCode() ^ referencedTable.name.hashCode() ^ referencedAttributes.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        return this.hashCode() == obj.hashCode();
    }
}
