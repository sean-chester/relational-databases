package a2;

import a2.erd.Attribute;
import a2.erd.AttributeSet;
import a2.sql.*;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class ExampleTest {

    @Test
    @DisplayName("Test equality operator of two Database objects")
    void loadDatabase() {
        //exact replica of the Example Database provided in the Example.java file

        //----------------- BEGIN FIRST TABLE -----------------------------
        Table firstTable = new Table();
        firstTable.name = "A";
        firstTable.attributes = new AttributeSet(List.of(
                new Attribute("a2"),
                new Attribute("a1")
        ));
        firstTable.primaryKey = new Key(new AttributeSet(List.of(
                new Attribute("a1")
        )));
        firstTable.foreignKeys = new ForeignKeySet(); // empty fk set

        //----------------- END FIRST TABLE --------------------------------

        //----------------- BEGIN SECOND TABLE -----------------------------
        Table secondTable = new Table();
        secondTable.name = "B";
        secondTable.attributes = new AttributeSet(List.of(
                new Attribute("b2"),
                new Attribute("b1")
        ));
        secondTable.primaryKey = new Key(new AttributeSet(List.of(
                new Attribute("b1")
        )));
        secondTable.foreignKeys = new ForeignKeySet(); // empty fk set
        //----------------- END SECOND TABLE --------------------------------

        //----------------- BEGIN THIRD TABLE -----------------------------
        Table thirdTable = new Table();
        thirdTable.name = "R1";
        thirdTable.attributes = new AttributeSet(List.of(
                new Attribute("b1"),
                new Attribute("a1"),
                new Attribute("x")
        ));
        thirdTable.primaryKey = new Key(new AttributeSet(List.of(
                new Attribute("a1"),
                new Attribute("b1")
        )));
        thirdTable.foreignKeys = new ForeignKeySet(List.of(
                new ForeignKey(
                        new AttributeSet(List.of(new Attribute("a1"))),
                        firstTable,
                        new AttributeSet(List.of(new Attribute("a1")))
                ),
                new ForeignKey(
                        new AttributeSet(List.of(new Attribute("b1"))),
                        secondTable,
                        new AttributeSet(List.of(new Attribute("b1")))
                )
        ));
        //----------------- END THIRD TABLE --------------------------------

        Database replica_db = new Database();
        replica_db.add(firstTable);
        replica_db.add(secondTable);
        replica_db.add(thirdTable);


        assertEquals(Example.loadDatabase(), replica_db);
    }
}