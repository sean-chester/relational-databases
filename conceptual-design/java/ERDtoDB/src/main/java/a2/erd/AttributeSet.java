package a2.erd;

import java.util.ArrayList;
import java.util.Collection;

/**
 * A collection of attributes
 */
public class AttributeSet extends ArrayList<Attribute> {

    public AttributeSet() {
        super();
    }

    public AttributeSet(Collection<? extends Attribute> c) {
        super(c);
    }

    /**
     * joins all attributes with a comma into a single SQL style attribute list
     * example `A`, `B`, `C`, `D`
     *
     * @return String
     */
    @Override
    public String toString() {
        if (this.isEmpty()) return "";

        StringBuilder builder = new StringBuilder();
        String commaPrefix = "";
        for (final Attribute attr : this) {
            builder.append(commaPrefix)
                    .append("`")
                    .append(attr.name)
                    .append("`");
            commaPrefix = ", ";
        }
        return builder.toString();
    }

    /**
     * joins all attributes with a comma into a single SQL style attribute list, each having the specified
     * type (aka attributeType parameter)
     * example type="INT" =>  `A` INT, `B` INT, `C` INT, `D` INT
     *
     * @return String
     */
    public String toString(String attributeType) {
        if (this.isEmpty()) return "";

        StringBuilder builder = new StringBuilder();
        String commaPrefix = "";
        for (final Attribute attr : this) {
            builder.append(commaPrefix)
                    .append("`")
                    .append(attr.name)
                    .append("`")
                    .append(" ")
                    .append(attributeType);
            commaPrefix = ", ";
        }
        return builder.toString();
    }

    @Override
    public int hashCode() {
        int hash = 0;
        for (Attribute a : this) {
            hash ^= a.hashCode();
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
