/**
 * Set of unit tests with which to evaluate the `erd-converter.hpp` functions, such as `convert_to_table()`.
 */

#include "catch2/catch.hpp"
#include "db-gen/converter/erd-converter.hpp"

namespace csc370 {
namespace a2 {
namespace tests {

using tname = std::string;
using aname = std::string;




TEST_CASE( "Equality operator" )
{
    auto table1 = sql::Table< tname, aname >{ std::string{}
                                            , sql::AttributeSet< aname >{ "A" }
                                            , sql::Key< aname >{}
                                            , sql::ForeignKeySet< tname, aname >{} };
    table1.name = "R";
    table1.primary_key = sql::Key< aname >{ sql::AttributeRefs< aname >{ &( table1.attributes [ 0 ] ) } };


    auto table2 = sql::Table< tname, aname >{ std::string{}
                                            , sql::AttributeSet< aname >{ "B", "C" }
                                            , sql::Key< aname >{}
                                            , sql::ForeignKeySet< tname, aname >{} };
    table2.name = "S";
    table2.primary_key = { { &(table2.attributes [ 0 ] ) } };
    table2.foreign_keys = { { { { &(table2.attributes [ 0 ] ) } }, &( table1 ) } };


    auto result2 = sql::Database< tname, aname >{ table1, table2 };


    REQUIRE( ( "Test equality comparator with a foreign key" && ( result2 == result2 ) ) );
    REQUIRE( ( "Test inequality comparator with a foreign key" && ( table1 != table2 ) ) );
}



TEST_CASE( "1. Single entity set with a single attribute" )
{
    // Mock unit test input
    auto diagram1 = erd::ERD( erd::RelationshipList{}
                            , erd::EntitySetList{ erd::EntitySet{ std::string{ "R" }
                                                    , erd::AttributeSet{ erd::Attribute{ "A", true } }
                                                    , erd::ConnectionList{}
                                                    , erd::ParentList{}
                                                    , erd::SupportingRelationshipList{} } } );

    // Mock expected output
    auto table1 = sql::Table< tname, aname >{ std::string{ "R" }
                                            , sql::AttributeSet< aname >{ "A" }
                                            , sql::Key< aname >{}
                                            , sql::ForeignKeySet< tname, aname > {} };
    table1.primary_key = { { &(table1.attributes [ 0u ] ) } };


    auto result1 = sql::Database< tname, aname >{ table1 };


    // Run test
    REQUIRE( result1 == convert_to_table< tname, aname >( diagram1 ) );
}



TEST_CASE( "2. Single entity set with two attributes, which are both part of the PK" )
{
    // Mock unit test input
    auto diagram2 = erd::ERD( erd::RelationshipList{}
                            , erd::EntitySetList{ erd::EntitySet{ std::string{ "R" }
                                                    , erd::AttributeSet{ erd::Attribute{ "A", true }, erd::Attribute{ "B", true } }
                                                    , erd::ConnectionList{}
                                                    , erd::ParentList{}
                                                    , erd::SupportingRelationshipList{} } } );

    // Mock expected output
    auto table2 = sql::Table< tname, aname >{ std::string{ "R" }
                                            , sql::AttributeSet< aname >{ "A", "B" }
                                            , sql::Key< aname >{}
                                            , sql::ForeignKeySet< tname, aname > {} };
    table2.primary_key = { { &(table2.attributes [ 0u ] ), &(table2.attributes [ 1u ] ) } };


    auto result2 = sql::Database< tname, aname >{ table2 };


    // Run test
    REQUIRE( result2 == convert_to_table< tname, aname >( diagram2 ) );
}



TEST_CASE( "3. Single entity set with two attributes, in which only one is part of the PK" )
{
    // Mock unit test input
    auto diagram3 = erd::ERD( erd::RelationshipList{}
                            , erd::EntitySetList{ erd::EntitySet{ std::string{ "R" }
                                                    , erd::AttributeSet{ erd::Attribute{ "A", true }, erd::Attribute{ "B", false } }
                                                    , erd::ConnectionList{}
                                                    , erd::ParentList{}
                                                    , erd::SupportingRelationshipList{} } } );

    // Mock expected output
    // Not provided
    auto table3 = sql::Table< tname, aname >{ std::string{}
                                            , sql::AttributeSet< aname >{}
                                            , sql::Key< aname >{}
                                            , sql::ForeignKeySet< tname, aname > {} };


    auto result3 = sql::Database< tname, aname >{ table3 };


    // Run test
    REQUIRE( result3 == convert_to_table< tname, aname >( diagram3 ) );
}



TEST_CASE( "4. Two entity sets, each with two attributes, one of which is the PK attribute + a m-n relationship between them with no attributes" )
{
    // Mock unit test input
    auto diagram4 = erd::ERD(
        erd::RelationshipList{
            erd::Relationship{
                std::string{"ShopsAt"}
              , {} } }
      , erd::EntitySetList{} );

    diagram4.second = erd::EntitySetList{
        erd::EntitySet{
            std::string{ "Customer" }
          , erd::AttributeSet{
                erd::Attribute{ "customer_id", true }
              , erd::Attribute{ "customer_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram4.first[ 0 ] ), erd::Multiplicity::many ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} }
      , erd::EntitySet{
            std::string{ "Store" }
          , erd::AttributeSet{
                erd::Attribute{ "store_id", true }
              , erd::Attribute{ "store_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram4.first[ 0 ] ), erd::Multiplicity::many ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } };

    // Mock expected output
    auto table4a = sql::Table< tname, aname >{
        std::string{ "Customer" }
      , sql::AttributeSet< aname >{ "customer_id", "customer_name" }
      , sql::Key< aname >{}
      , sql::ForeignKeySet< tname, aname > {} };

    table4a.primary_key = { { &(table4a.attributes [ 0u ] ) } };

    auto table4b = sql::Table< tname, aname >{
        std::string{ "Store" }
      , sql::AttributeSet< aname >{ "store_id", "store_name" }
      , sql::Key< aname >{}
      , sql::ForeignKeySet< tname, aname > {} };

    table4b.primary_key = { { &(table4b.attributes [ 0u ] ) } };

    auto table4c = sql::Table< tname, aname >{
        std::string{ "ShopsAt" }
      , sql::AttributeSet< aname >{ "store_id", "customer_id" }
      , sql::Key< aname >{}
      , sql::ForeignKeySet< tname, aname > {} };

    table4c.primary_key = { { &(table4c.attributes [ 0u ] ), &(table4c.attributes [ 1u ] ) } };
    table4c.foreign_keys = sql::ForeignKeySet< tname, aname >{ { sql::Key< aname >{ { &(table4c.attributes [ 1u ] ) } }, &( table4a ) }
                                                             , { sql::Key< aname >{ { &(table4c.attributes [ 0u ] ) } }, &( table4b ) } };


    auto result4 = sql::Database< tname, aname >{ table4a, table4b, table4c };


    // Run test
    REQUIRE( result4 == convert_to_table< tname, aname >( diagram4 ) );
}



TEST_CASE( "5. Two entity sets, each with two attributes, one of which is the PK attribute + a m-n relationship with a PK attribute." )
{
    // Mock unit test input
    auto diagram5 = erd::ERD(
        erd::RelationshipList{
            erd::Relationship{
                std::string{"ShopsAt"}
              , erd::AttributeSet{
                    erd::Attribute{ "date", true } } } }
      , erd::EntitySetList{} );

    diagram5.second = erd::EntitySetList{
        erd::EntitySet{
            std::string{ "Customer" }
          , erd::AttributeSet{
                erd::Attribute{ "customer_id", true }
              , erd::Attribute{ "customer_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram5.first[ 0 ] ), erd::Multiplicity::many ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} }
      , erd::EntitySet{
            std::string{ "Store" }
          , erd::AttributeSet{
                erd::Attribute{ "store_id", true }
              , erd::Attribute{ "store_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram5.first[ 0 ] ), erd::Multiplicity::many ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } };

    // Mock expected output
    auto table5a = sql::Table< tname, aname >{
        std::string{ "Customer" }
      , sql::AttributeSet< aname >{ "customer_id", "customer_name" }
      , sql::Key< aname >{}
      , sql::ForeignKeySet< tname, aname > {} };

    table5a.primary_key = { { &(table5a.attributes [ 0u ] ) } };

    auto table5b = sql::Table< tname, aname >{
        std::string{ "Store" }
      , sql::AttributeSet< aname >{ "store_id", "store_name" }
      , sql::Key< aname >{}
      , sql::ForeignKeySet< tname, aname > {} };

    table5b.primary_key = { { &(table5b.attributes [ 0u ] ) } };

    auto table5c = sql::Table< tname, aname >{
        std::string{ "ShopsAt" }
      , sql::AttributeSet< aname >{ "store_id", "customer_id", "date" }
      , sql::Key< aname >{}
      , sql::ForeignKeySet< tname, aname > {} };

    table5c.primary_key = { { &(table5c.attributes [ 0u ] ), &(table5c.attributes [ 1u ] ), &(table5c.attributes [ 2u ] ) } };
    table5c.foreign_keys = sql::ForeignKeySet< tname, aname >{ { sql::Key< aname >{ { &(table5c.attributes [ 1u ] ) } }, &( table5a ) }
                                                             , { sql::Key< aname >{ { &(table5c.attributes [ 0u ] ) } }, &( table5b ) } };


    auto result5 = sql::Database< tname, aname >{ table5a, table5b, table5c };


    // Run test
    REQUIRE( result5 == convert_to_table< tname, aname >( diagram5 ) );
}



TEST_CASE( "6. Two entity sets, each with two attributes, one of which is the PK attribute + a m-n relationship with a PK and non-PK attribute." )
{
    // Mock unit test input
    auto diagram6 = erd::ERD(
        erd::RelationshipList{
            erd::Relationship{
                std::string{"ShopsAt"}
              , erd::AttributeSet{
                    erd::Attribute{ "date", true }
                  , erd::Attribute{ "purchase_amount", false } } } }
      , erd::EntitySetList{} );

    diagram6.second = erd::EntitySetList{
        erd::EntitySet{
            std::string{ "Customer" }
          , erd::AttributeSet{
                erd::Attribute{ "customer_id", true }
              , erd::Attribute{ "customer_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram6.first[ 0 ] ), erd::Multiplicity::many ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} }
      , erd::EntitySet{
            std::string{ "Store" }
          , erd::AttributeSet{
                erd::Attribute{ "store_id", true }
              , erd::Attribute{ "store_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram6.first[ 0 ] ), erd::Multiplicity::many ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } };

    // Mock expected output
    // Not provided
    auto result6 = sql::Database< tname, aname >{};


    // Run test
    REQUIRE( result6 == convert_to_table< tname, aname >( diagram6 ) );
}



TEST_CASE( "7. Two entity sets, each with two attributes, one of which is the PK attribute + a 1-m or m-1 relationship without attributes." )
{
    // Mock unit test input
    auto diagram7 = erd::ERD(
        erd::RelationshipList{
            erd::Relationship{
                std::string{"Prefers"}
              , erd::AttributeSet{} } }
      , erd::EntitySetList{} );

    diagram7.second = erd::EntitySetList{
        erd::EntitySet{
            std::string{ "Customer" }
          , erd::AttributeSet{
                erd::Attribute{ "customer_id", true }
              , erd::Attribute{ "customer_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram7.first[ 0 ] ), erd::Multiplicity::many ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} }
      , erd::EntitySet{
            std::string{ "Store" }
          , erd::AttributeSet{
                erd::Attribute{ "store_id", true }
              , erd::Attribute{ "store_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram7.first[ 0 ] ), erd::Multiplicity::one ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } };

    // Mock expected output
    // Not provided
    auto result7 = sql::Database< tname, aname >{};


    // Run test
    REQUIRE( result7 == convert_to_table< tname, aname >( diagram7 ) );
}



TEST_CASE( "8. Two entity sets, each with two attributes, one of which is the PK attribute + a 1-m or m-1 relationship with 1 PK attribute." )
{
    // Mock unit test input
    auto diagram8 = erd::ERD(
        erd::RelationshipList{
            erd::Relationship{
                std::string{"Prefers"}
              , erd::AttributeSet{
                    erd::Attribute{ "since", true } } } }
      , erd::EntitySetList{} );

    diagram8.second = erd::EntitySetList{
        erd::EntitySet{
            std::string{ "Customer" }
          , erd::AttributeSet{
                erd::Attribute{ "customer_id", true }
              , erd::Attribute{ "customer_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram8.first[ 0 ] ), erd::Multiplicity::many ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} }
      , erd::EntitySet{
            std::string{ "Store" }
          , erd::AttributeSet{
                erd::Attribute{ "store_id", true }
              , erd::Attribute{ "store_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram8.first[ 0 ] ), erd::Multiplicity::one ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } };

    // Mock expected output
    // Not provided
    auto result8 = sql::Database< tname, aname >{};


    // Run test
    REQUIRE( result8 == convert_to_table< tname, aname >( diagram8 ) );
}



TEST_CASE( "9. Two entity sets, one of which is designated as a parent of the other." )
{
    // Mock unit test input
    auto diagram9 = erd::ERD(
        erd::RelationshipList{
            erd::Relationship{
                std::string{"ManagerIsAnEmployee"}
              , erd::AttributeSet{} } }
      , erd::EntitySetList{} );

    diagram9.second.push_back(
        erd::EntitySet{
            std::string{ "Employee" }
          , erd::AttributeSet{
                erd::Attribute{ "employee_id", true }
              , erd::Attribute{ "employee_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram9.first[ 0 ] ), erd::Multiplicity::one ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } );

    diagram9.second.push_back(
        erd::EntitySet{ 
            std::string{ "Manager" }
          , erd::AttributeSet{}
          , erd::ConnectionList{}
          , erd::ParentList{ &( diagram9.first[ 0 ] ) }
          , erd::SupportingRelationshipList{} } );

    // Mock expected output
    auto table9a = sql::Table< tname, aname >{
        std::string{ "Employee" }
      , sql::AttributeSet< aname >{ "employee_id", "employee_name" }
      , sql::Key< aname >{}
      , sql::ForeignKeySet< tname, aname > {} };

    table9a.primary_key = { { &(table9a.attributes [ 0u ] ) } };

    auto table9b = sql::Table< tname, aname >{
        std::string{ "Manager" }
      , sql::AttributeSet< aname >{ "employee_id" }
      , sql::Key< aname >{}
      , sql::ForeignKeySet< tname, aname > {} };

    table9b.primary_key = { { &(table9b.attributes [ 0u ] ) } };
    table9b.foreign_keys = sql::ForeignKeySet< tname, aname >{ { sql::Key< aname >{ { &(table9b.attributes [ 0u ] ) } }, &( table9a ) } };
    auto result9 = sql::Database< tname, aname >{ table9a, table9b };


    // Run test
    REQUIRE( result9 == convert_to_table< tname, aname >( diagram9 ) );
}



TEST_CASE( "10. A basic weak entity set." )
{
    // Mock unit test input
    auto diagram10 = erd::ERD(
        erd::RelationshipList{
            erd::Relationship{
                std::string{"FoundIn"}
              , erd::AttributeSet{} } }
      , erd::EntitySetList{} );

    diagram10.second.push_back(
        erd::EntitySet{
            std::string{ "Building" }
          , erd::AttributeSet{
                erd::Attribute{ "building_id", true }
              , erd::Attribute{ "building_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagram10.first[ 0 ] ), erd::Multiplicity::one ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } );

    diagram10.second.push_back(
        erd::EntitySet{
            std::string{ "Room" }
          , erd::AttributeSet{
                erd::Attribute{ "room_number", true }
              , erd::Attribute{ "max_capacity", false } }
          , erd::ConnectionList{}
          , erd::ParentList{}
          , erd::SupportingRelationshipList{ &( diagram10.first[ 0 ] ) } } );

    // Mock expected output
    // Not provided
    auto result10 = sql::Database< tname, aname >{};


    // Run test
    REQUIRE( result10 == convert_to_table< tname, aname >( diagram10 ) );
}



TEST_CASE( "11. Not released." )
{
    // Mock unit test input
    // Not provided
    auto diagram11 = erd::ERD(
        erd::RelationshipList{}
      , erd::EntitySetList{} );

    // Mock expected output
    // Not provided
    auto result11 = sql::Database< tname, aname >{};

    // Run test
    REQUIRE( result11 == convert_to_table< tname, aname >( diagram11 ) );
}
TEST_CASE( "12. Not released." )
{
    // Mock unit test input
    // Not provided
    auto diagram12 = erd::ERD(
        erd::RelationshipList{}
      , erd::EntitySetList{} );

    // Mock expected output
    // Not provided
    auto result12 = sql::Database< tname, aname >{};

    // Run test
    REQUIRE( result12 == convert_to_table< tname, aname >( diagram12 ) );
}
TEST_CASE( "13. Not released." )
{
    // Mock unit test input
    // Not provided
    auto diagram13 = erd::ERD(
        erd::RelationshipList{}
      , erd::EntitySetList{} );

    // Mock expected output
    // Not provided
    auto result13 = sql::Database< tname, aname >{};

    // Run test
    REQUIRE( result13 == convert_to_table< tname, aname >( diagram13 ) );
}
TEST_CASE( "14. Not released." )
{
    // Mock unit test input
    // Not provided
    auto diagram14 = erd::ERD(
        erd::RelationshipList{}
      , erd::EntitySetList{} );

    // Mock expected output
    // Not provided
    auto result14 = sql::Database< tname, aname >{};

    // Run test
    REQUIRE( result14 == convert_to_table< tname, aname >( diagram14 ) );
}
TEST_CASE( "15. Not released." )
{
    // Mock unit test input
    // Not provided
    auto diagram15 = erd::ERD(
        erd::RelationshipList{}
      , erd::EntitySetList{} );

    // Mock expected output
    // Not provided
    auto result15 = sql::Database< tname, aname >{};

    // Run test
    REQUIRE( result15 == convert_to_table< tname, aname >( diagram15 ) );
}
TEST_CASE( "16. Not released." )
{
    // Mock unit test input
    // Not provided
    auto diagram16 = erd::ERD(
        erd::RelationshipList{}
      , erd::EntitySetList{} );

    // Mock expected output
    // Not provided
    auto result16 = sql::Database< tname, aname >{};

    // Run test
    REQUIRE( result16 == convert_to_table< tname, aname >( diagram16 ) );
}
TEST_CASE( "17. Not released." )
{
    // Mock unit test input
    // Not provided
    auto diagram17 = erd::ERD(
        erd::RelationshipList{}
      , erd::EntitySetList{} );

    // Mock expected output
    // Not provided
    auto result17 = sql::Database< tname, aname >{};

    // Run test
    REQUIRE( result17 == convert_to_table< tname, aname >( diagram17 ) );
}
TEST_CASE( "18. Not released." )
{
    // Mock unit test input
    // Not provided
    auto diagram18 = erd::ERD(
        erd::RelationshipList{}
      , erd::EntitySetList{} );

    // Mock expected output
    // Not provided
    auto result18 = sql::Database< tname, aname >{};

    // Run test
    REQUIRE( result18 == convert_to_table< tname, aname >( diagram18 ) );
}
TEST_CASE( "19. Not released." )
{
    // Mock unit test input
    // Not provided
    auto diagram19 = erd::ERD(
        erd::RelationshipList{}
      , erd::EntitySetList{} );

    // Mock expected output
    // Not provided
    auto result19 = sql::Database< tname, aname >{};

    // Run test
    REQUIRE( result19 == convert_to_table< tname, aname >( diagram19 ) );
}
TEST_CASE( "20. Not released." )
{
    // Mock unit test input
    // Not provided
    auto diagram20 = erd::ERD(
        erd::RelationshipList{}
      , erd::EntitySetList{} );

    // Mock expected output
    // Not provided
    auto result20 = sql::Database< tname, aname >{};

    // Run test
    REQUIRE( result20 == convert_to_table< tname, aname >( diagram20 ) );
}



TEST_CASE( "B1. A weak entity set is supported by a weak entity set, at least one of which is involved in a non-supporting relationship" )
{
    // Mock unit test input
    auto diagramB1 = erd::ERD(
        erd::RelationshipList{
            erd::Relationship{
                std::string{"FoundIn"}
              , erd::AttributeSet{} }
          , erd::Relationship{
                std::string{"PlacedIn"}
              , erd::AttributeSet{} }
          , erd::Relationship{
                std::string{"HeldIn"}
              , erd::AttributeSet{} } }
      , erd::EntitySetList{} );

    diagramB1.second.push_back(
        erd::EntitySet{
            std::string{ "Building" }
          , erd::AttributeSet{
                erd::Attribute{ "building_id", true }
              , erd::Attribute{ "building_name", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagramB1.first[ 0 ] ), erd::Multiplicity::one ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } );

    diagramB1.second.push_back(
        erd::EntitySet{
            std::string{ "Room" }
          , erd::AttributeSet{
                erd::Attribute{ "room_number", true }
              , erd::Attribute{ "max_capacity", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagramB1.first[ 1 ] ), erd::Multiplicity::one )
              , std::make_pair( &( diagramB1.first[ 2 ] ), erd::Multiplicity::one ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{ &( diagramB1.first[ 0 ] ) } } );

    diagramB1.second.push_back(
        erd::EntitySet{
            std::string{ "Desk" }
          , erd::AttributeSet{
                erd::Attribute{ "desk_id", true } }
          , erd::ConnectionList{}
          , erd::ParentList{}
          , erd::SupportingRelationshipList{ &( diagramB1.first[ 1 ] ) } } );

    diagramB1.second.push_back(
        erd::EntitySet{
            std::string{ "Class" }
          , erd::AttributeSet{
                erd::Attribute{ "crn", true } }
          , erd::ConnectionList{
                std::make_pair( &( diagramB1.first[ 2 ] ), erd::Multiplicity::many ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } );

    // Mock expected output
    // Not provided
    auto resultB1 = sql::Database< tname, aname >{};


    // Run test
    REQUIRE( resultB1 == convert_to_table< tname, aname >( diagramB1 ) );
}



TEST_CASE( "B2. A ternary relationship is provided. Aspects of this test case are subject to change." )
{
    // Mock unit test input
    auto diagramB2 = erd::ERD(
        erd::RelationshipList{
            erd::Relationship{
                std::string{"R"}
              , erd::AttributeSet{} } }
      , erd::EntitySetList{} );

    diagramB2.second.push_back(
        erd::EntitySet{
            std::string{ "A" }
          , erd::AttributeSet{
                erd::Attribute{ "a1", true }
              , erd::Attribute{ "a2", true } }
          , erd::ConnectionList{
                std::make_pair( &( diagramB2.first[ 0 ] ), erd::Multiplicity::many ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } );

    diagramB2.second.push_back(
        erd::EntitySet{
            std::string{ "B" }
          , erd::AttributeSet{
                erd::Attribute{ "b1", true }
              , erd::Attribute{ "b2", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagramB2.first[ 0 ] ), erd::Multiplicity::many ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } );

    diagramB2.second.push_back(
        erd::EntitySet{
            std::string{ "C" }
          , erd::AttributeSet{
                erd::Attribute{ "c1", true }
              , erd::Attribute{ "c2", false } }
          , erd::ConnectionList{
                std::make_pair( &( diagramB2.first[ 0 ] ), erd::Multiplicity::one ) }
          , erd::ParentList{}
          , erd::SupportingRelationshipList{} } );


    // Mock expected output
    // Not provided
    auto resultB2 = sql::Database< tname, aname >{};


    // Run test
    REQUIRE( resultB2 == convert_to_table< tname, aname >( diagramB2 ) );
}


} // namespace tests
} // namespace a2
} // namespace csc370
