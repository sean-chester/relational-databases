package a2;

import a2.erd.*;
import a2.sql.*;

import java.util.List;

public class Example {
    public static ERD loadERD() {
        ERD erd = new ERD();

        erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "R1",
                        new AttributeSet(List.of(new Attribute("x"))),
                        new Key())
        ));
        erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "A", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("a1"),
                                new Attribute("a2"))),
                        new Key(new AttributeSet(List.of(new Attribute("a1")))), // primary key
                        new ConnectionList(List.of(new Connection(new Relationship("R1"), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() // IsA relationship list = empty
                ),
                new EntitySet(
                        "B", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("b1"),
                                new Attribute("b2"))),
                        new Key(new AttributeSet(List.of(new Attribute("b1")))), // primary key
                        new ConnectionList(List.of(new Connection(new Relationship("R1"), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() // IsA relationship list = empty
                )
        ));

        return erd;
    }

    public static Database loadDatabase() {


        //----------------- BEGIN FIRST TABLE -----------------------------
        Table firstTable = new Table();
        firstTable.name = "A";
        firstTable.attributes = new AttributeSet(List.of(
                new Attribute("a1"),
                new Attribute("a2")
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
                new Attribute("b1"),
                new Attribute("b2")
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
                new Attribute("a1"),
                new Attribute("b1"),
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

        Database db = new Database();
        db.add(firstTable);
        db.add(secondTable);
        db.add(thirdTable);

        return db;
    }
}
