package a2;

import a2.erd.*;
import a2.sql.*;

import java.util.List;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Timeout;

import java.util.concurrent.TimeUnit;

import static org.junit.jupiter.api.Assertions.*;

class ImplementMeTest {

    @Test
    @DisplayName("Single entity set with a single attribute which is the PK")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case01() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of());
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "A", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("a1"))),
                        new Key(new AttributeSet(List.of(new Attribute("a1")))), // primary key
                        new ConnectionList(), // connections = empty
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList()
                )));

        // Actual DB object
        Table firstTable = new Table();
        firstTable.name = "A";
        firstTable.attributes = new AttributeSet(List.of(
                new Attribute("a1")
        ));
        firstTable.primaryKey = new Key(new AttributeSet(List.of(
                new Attribute("a1")
        )));
        firstTable.foreignKeys = new ForeignKeySet(); // empty fk set

        Database db = new Database();
        db.add(firstTable);

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("Single entity set with two attributes, which are both part of the PK")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case02() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of());
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "A", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("a1"),
                                new Attribute("a2"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("a1"),
                                new Attribute("a2")))), // primary key
                        new ConnectionList(), // connections = empty
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                )));

        // Actual DB object
        Table firstTable = new Table();
        firstTable.name = "A";
        firstTable.attributes = new AttributeSet(List.of(
                new Attribute("a1"),
                new Attribute("a2")
        ));
        firstTable.primaryKey = new Key(new AttributeSet(List.of(
                new Attribute("a1"),
                new Attribute("a2")
        )));
        firstTable.foreignKeys = new ForeignKeySet(); // empty fk set

        Database db = new Database();
        db.add(firstTable);

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("Single entity set with two attributes, in which only one is part of the PK")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case03() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of());
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "A", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("a1"),
                                new Attribute("a2"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("a1")))), // primary key
                        new ConnectionList(), // connections = empty
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                )));

        // Actual DB object
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

        Database db = new Database();
        db.add(firstTable);

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("A many-many relationship with no attributes and single-attribute keys")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case04() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "ShopsAt",
                        new AttributeSet(),
                        new Key())
        ));
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "Customer", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("customer_id"),
                                new Attribute("customer_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("customer_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "Store", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("store_id"),
                                new Attribute("store_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("store_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                )));

        // Actual DB object
        Database db = new Database();
        db.add( new Table( "Customer",
                            new AttributeSet(List.of(
                                new Attribute("customer_id"),
                                new Attribute("customer_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("customer_id")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "Store",
                            new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("store_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("store_id")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "ShopsAt",
                            new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("customer_id"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("customer_id")))),
                            new ForeignKeySet(List.of(
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("store_id"))),
                                        db.get(1),
                                        new AttributeSet(List.of(new Attribute("store_id")))
                                ),
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("customer_id"))),
                                        db.get(0),
                                        new AttributeSet(List.of(new Attribute("customer_id")))
                                )))
        ));

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("A many-many relationship with one PK attribute and single-attribute keys")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case05() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "ShopsAt",
                        new AttributeSet(List.of( // attributes
                                new Attribute("date"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("date")))) // primary key
        )));
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "Customer", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("customer_id"),
                                new Attribute("customer_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("customer_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "Store", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("store_id"),
                                new Attribute("store_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("store_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                )));

        // Actual DB object
        Database db = new Database();
        db.add( new Table( "Customer",
                            new AttributeSet(List.of(
                                new Attribute("customer_id"),
                                new Attribute("customer_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("customer_id")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "Store",
                            new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("store_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("store_id")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "ShopsAt",
                            new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("customer_id"),
                                new Attribute("date"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("customer_id"),
                                new Attribute("date")))),
                            new ForeignKeySet(List.of(
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("store_id"))),
                                        db.get(1),
                                        new AttributeSet(List.of(new Attribute("store_id")))
                                ),
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("customer_id"))),
                                        db.get(0),
                                        new AttributeSet(List.of(new Attribute("customer_id")))
                                )))
        ));

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("A many-many relationship with one PK and one non-PK attribute and single-attribute keys")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case06() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "ShopsAt",
                        new AttributeSet(List.of( // attributes
                                new Attribute("date"),
                                new Attribute("purchase_amount"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("date")))) // primary key
        )));
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "Customer", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("customer_id"),
                                new Attribute("customer_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("customer_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "Store", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("store_id"),
                                new Attribute("store_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("store_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                )));

        // Actual DB object
        Database db = new Database();
        db.add( new Table( "Customer",
                            new AttributeSet(List.of(
                                new Attribute("customer_id"),
                                new Attribute("customer_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("customer_id")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "Store",
                            new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("store_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("store_id")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "ShopsAt",
                            new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("customer_id"),
                                new Attribute("purchase_amount"),
                                new Attribute("date"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("customer_id"),
                                new Attribute("date")))),
                            new ForeignKeySet(List.of(
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("store_id"))),
                                        db.get(1),
                                        new AttributeSet(List.of(new Attribute("store_id")))
                                ),
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("customer_id"))),
                                        db.get(0),
                                        new AttributeSet(List.of(new Attribute("customer_id")))
                                )))
        ));

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("A one-many or many-one relationship with no attributes and single-attribute keys")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case07() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "Prefers",
                        new AttributeSet(),
                        new Key(new AttributeSet())
        )));
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "Customer", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("customer_id"),
                                new Attribute("customer_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("customer_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "Store", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("store_id"),
                                new Attribute("store_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("store_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.ONE))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                )));

        // Actual DB object
        Database db = new Database();
        db.add( new Table( "Store",
                            new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("store_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("store_id")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "Customer",
                            new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("customer_id"),
                                new Attribute("customer_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("customer_id")))),
                            new ForeignKeySet(List.of(
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("store_id"))),
                                        db.get(0),
                                        new AttributeSet(List.of(new Attribute("store_id")))
                                )))
        ));

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("A one-many or many-one relationship with one PK attribute and single-attribute keys")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case08() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "Prefers",
                        new AttributeSet(List.of( // attributes
                                new Attribute("since"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("since"))))
        )));
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "Customer", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("customer_id"),
                                new Attribute("customer_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("customer_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "Store", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("store_id"),
                                new Attribute("store_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("store_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.ONE))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                )));

        // Actual DB object
        Database db = new Database();
        db.add( new Table( "Customer",
                            new AttributeSet(List.of(
                                new Attribute("customer_id"),
                                new Attribute("customer_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("customer_id")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "Store",
                            new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("store_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("store_id")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "Prefers",
                            new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("customer_id"),
                                new Attribute("since"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("store_id"),
                                new Attribute("since")))),
                            new ForeignKeySet(List.of(
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("store_id"))),
                                        db.get(1),
                                        new AttributeSet(List.of(new Attribute("store_id")))
                                ),
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("customer_id"))),
                                        db.get(0),
                                        new AttributeSet(List.of(new Attribute("customer_id")))
                                )))
        ));

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("Two entity sets, one of which is designated as a parent of the other")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case09() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "ManagerIsAnEmployee",
                        new AttributeSet(),
                        new Key()
        )));
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "Employee", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("employee_id"),
                                new Attribute("employee_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("employee_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.ONE))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "Manager", // name
                        new AttributeSet(),
                        new Key(), // primary key
                        new ConnectionList(), // connections
                        new ParentList(List.of( input_erd.relationships.get(0) )), // parents
                        new SupportingRelationshipList() 
                )));

        // Actual DB object
        Database db = new Database();
        db.add( new Table( "Employee",
                            new AttributeSet(List.of(
                                new Attribute("employee_id"),
                                new Attribute("employee_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("employee_id")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "Manager",
                            new AttributeSet(List.of(
                                new Attribute("employee_id"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("employee_id")))),
                            new ForeignKeySet(List.of(
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("employee_id"))),
                                        db.get(0),
                                        new AttributeSet(List.of(new Attribute("employee_id")))
                                )))
        ));

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("A basic weak entity set")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case10() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "FoundIn",
                        new AttributeSet(),
                        new Key()
        )));
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "Building", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("building_id"),
                                new Attribute("building_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("building_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.ONE))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "Room", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("room_number"),
                                new Attribute("max_capacity"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("room_number")))), // primary key
                        new ConnectionList(), // connections
                        new ParentList(), // parents
                        new SupportingRelationshipList(List.of( input_erd.relationships.get(0) ))
                )));

        // Actual DB object
        Database db = new Database();
        db.add( new Table( "Building",
                            new AttributeSet(List.of(
                                new Attribute("building_id"),
                                new Attribute("building_name"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("building_id")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "Room",
                            new AttributeSet(List.of(
                                new Attribute("building_id"),
                                new Attribute("room_number"),
                                new Attribute("max_capacity"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("building_id"),
                                new Attribute("room_number")))),
                            new ForeignKeySet(List.of(
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("building_id"))),
                                        db.get(0),
                                        new AttributeSet(List.of(new Attribute("building_id")))
                                )))
        ));

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("A many-many relationship using a 2-attribute FK")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case11() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "R",
                        new AttributeSet(),
                        new Key()
        )));
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "A", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("a1"),
                                new Attribute("a2"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("a1")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "B", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("b1"),
                                new Attribute("b2"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("b1"),
                                new Attribute("b2")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents
                        new SupportingRelationshipList()
                )));

        // Actual DB object
        Database db = new Database();
        db.add( new Table( "A",
                            new AttributeSet(List.of(
                                new Attribute("a1"),
                                new Attribute("a2"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("a1")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "B",
                            new AttributeSet(List.of(
                                new Attribute("b1"),
                                new Attribute("b2"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("b1"),
                                new Attribute("b2")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "R",
                            new AttributeSet(List.of(
                                new Attribute("a1"),
                                new Attribute("b1"),
                                new Attribute("b2"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("a1"),
                                new Attribute("b1"),
                                new Attribute("b2")))),
                            new ForeignKeySet(List.of(
                                new ForeignKey(
                                        new AttributeSet(List.of(new Attribute("a1"))),
                                        db.get(0),
                                        new AttributeSet(List.of(new Attribute("a1")))),
                                new ForeignKey(
                                        new AttributeSet(List.of(
                                                new Attribute("b1"),
                                                new Attribute("b2"))),
                                        db.get(1),
                                        new AttributeSet(List.of(
                                                new Attribute("b1"),
                                                new Attribute("b2"))))))
        ));

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("A many-many relationship using two 2-attribute FK's")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case12() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "R",
                        new AttributeSet(),
                        new Key()
        )));
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "A", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("a1"),
                                new Attribute("a2"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("a1"),
                                new Attribute("a2")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "B", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("b1"),
                                new Attribute("b2"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("b1"),
                                new Attribute("b2")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents
                        new SupportingRelationshipList()
                )));

        // Actual DB object
        Database db = new Database();
        db.add( new Table( "A",
                            new AttributeSet(List.of(
                                new Attribute("a1"),
                                new Attribute("a2"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("a1"),
                                new Attribute("a2")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "B",
                            new AttributeSet(List.of(
                                new Attribute("b1"),
                                new Attribute("b2"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("b1"),
                                new Attribute("b2")))),
                            new ForeignKeySet()
        ));
        db.add( new Table( "R",
                            new AttributeSet(List.of(
                                new Attribute("a1"),
                                new Attribute("a2"),
                                new Attribute("b1"),
                                new Attribute("b2"))),
                            new Key(new AttributeSet(List.of(
                                new Attribute("a1"),
                                new Attribute("a2"),
                                new Attribute("b1"),
                                new Attribute("b2")))),
                            new ForeignKeySet(List.of(
                                new ForeignKey(
                                        new AttributeSet(List.of(
                                                new Attribute("a1"),
                                                new Attribute("a2"))),
                                        db.get(0),
                                        new AttributeSet(List.of(
                                                new Attribute("a1"),
                                                new Attribute("a2")))),
                                new ForeignKey(
                                        new AttributeSet(List.of(
                                                new Attribute("b1"),
                                                new Attribute("b2"))),
                                        db.get(1),
                                        new AttributeSet(List.of(
                                                new Attribute("b1"),
                                                new Attribute("b2"))))))
        ));

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("Not pre-released")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case13() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        // Not provided
        ERD input_erd = new ERD();

        // Actual DB object
        // Not provided
        Database db = new Database();

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("Not pre-released")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case14() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        // Not provided
        ERD input_erd = new ERD();

        // Actual DB object
        // Not provided
        Database db = new Database();

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("Not pre-released")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case15() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        // Not provided
        ERD input_erd = new ERD();

        // Actual DB object
        // Not provided
        Database db = new Database();

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("Not pre-released")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case16() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        // Not provided
        ERD input_erd = new ERD();

        // Actual DB object
        // Not provided
        Database db = new Database();

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("Not pre-released")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case17() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        // Not provided
        ERD input_erd = new ERD();

        // Actual DB object
        // Not provided
        Database db = new Database();

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("Not pre-released")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case18() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        // Not provided
        ERD input_erd = new ERD();

        // Actual DB object
        // Not provided
        Database db = new Database();

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("Not pre-released")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case19() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        // Not provided
        ERD input_erd = new ERD();

        // Actual DB object
        // Not provided
        Database db = new Database();

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("Not pre-released")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void case20() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        // Not provided
        ERD input_erd = new ERD();

        // Actual DB object
        // Not provided
        Database db = new Database();

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("A weak entity set is supported by a weak entity set, at least one of which is in a non-supporting relationship")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void caseB1() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "FoundIn",
                        new AttributeSet(),
                        new Key()),
                new Relationship(
                        "PlacedIn",
                        new AttributeSet(),
                        new Key()),
                new Relationship(
                        "HeldIn",
                        new AttributeSet(),
                        new Key())
        ));
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "Building", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("building_id"),
                                new Attribute("building_name"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("building_id")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.ONE))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "Room", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("room_number"),
                                new Attribute("max_capacity"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("room_number")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(1), Multiplicity.ONE),
                                new Connection(input_erd.relationships.get(2), Multiplicity.ONE))), // connections
                        new ParentList(), // parents
                        new SupportingRelationshipList(List.of( input_erd.relationships.get(0) ))
                ),
                new EntitySet(
                        "Desk", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("desk_id"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("desk_id")))), // primary key
                        new ConnectionList(), // connections
                        new ParentList(), // parents
                        new SupportingRelationshipList(List.of( input_erd.relationships.get(1) ))
                ),
                new EntitySet(
                        "Class", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("crn"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("crn")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(2), Multiplicity.MANY))), // connections
                        new ParentList(), // parents
                        new SupportingRelationshipList()
                )));

        // Actual DB object
        // Not provided
        Database db = new Database();

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }

    @Test
    @DisplayName("A ternary relationship is provided. This test case may or may not shift")
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    void caseB2() {
        ImplementMe myImplementation = new ImplementMe();

        // Input ERD object
        ERD input_erd = new ERD();

        input_erd.relationships = new RelationshipList(List.of(
                new Relationship(
                        "R",
                        new AttributeSet(),
                        new Key())));
        input_erd.entitySets = new EntitySetList(List.of(
                new EntitySet(
                        "A", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("a1"),
                                new Attribute("a2"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("a1"),
                                new Attribute("a2")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "B", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("b1"),
                                new Attribute("b2"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("b1")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.MANY))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                ),
                new EntitySet(
                        "C", // name
                        new AttributeSet(List.of( // attributes
                                new Attribute("c1"),
                                new Attribute("c2"))),
                        new Key(new AttributeSet(List.of(
                                new Attribute("c1")))), // primary key
                        new ConnectionList(List.of(
                                new Connection(input_erd.relationships.get(0), Multiplicity.ONE))), // connections
                        new ParentList(), // parents = empty
                        new SupportingRelationshipList() 
                )));

        // Actual DB object
        // Not provided
        Database db = new Database();

        assertEquals(db, myImplementation.convertToDatabase(input_erd));
    }
}