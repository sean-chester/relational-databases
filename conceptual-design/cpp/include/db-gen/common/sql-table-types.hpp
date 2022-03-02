/**
 * Defines the data types used to describe a SQL CREATE TABLE DDL query
 */

#include <string>        // std::string
#include <vector>        // std::vector

#include <algorithm>     // std::copy()
#include <numeric>       // std::accumulate
#include <iterator>      // std::ostream_iterator

#include<iostream>
namespace { // anon

/**
 * Determines whether every element in the range [begin1, end1)
 * can be found within the range [begin2, end2)
 */
template < typename ForwardIterator, class BinaryPredicate  >
    bool set_containment( ForwardIterator begin1
                        , ForwardIterator end1
                        , ForwardIterator begin2
                        , ForwardIterator end2
                        , BinaryPredicate p )
    {
        return std::accumulate( begin1, end1, true, [ begin2, end2, p ]( bool b, auto const& x )
        {
            return b && std::find_if( begin2, end2, [ &x, p ]( auto const& y )
            {
                return p(x,y);
            } ) != end2;
        } );
    }

/**
 * Determines whether two sets contain the same set of elements.
 */
template < typename ForwardIterator, class BinaryPredicate >
    bool set_equality( ForwardIterator begin1
                     , ForwardIterator end1
                     , ForwardIterator begin2
                     , ForwardIterator end2
                     , BinaryPredicate p )
    {
        return set_containment( begin1, end1, begin2, end2, p )
            && set_containment( begin2, end2, begin1, end1, p );
    }

} // anonymous namespace

namespace csc370 {
namespace a2 {
namespace sql {

// forward declarations

/**
 * A Table is the basic construct of a relational database.
 * It consists of a schema (name and set of attributes)
 * and constraints (primary keys and foreign keys)
 */
template < typename tname, typename aname >
    struct Table;



/**
 * An attribute set describes the columns of a table
 */
template < typename aname >
    using AttributeSet = std::vector< aname >;

/**
 * This provides one level of indirection over an AttributeSet so
 * that one can refer to a set of attributes that have been defined elsewhere.
 */
template < typename aname >
    using AttributeRefs = std::vector< aname const * >;

/**
 * A key is a subset of attributes, defined with a level of indirection,
 * that uniquely identify each row of a table.
 */
template < typename aname >
    struct Key
    {
    	AttributeRefs< aname > attributes;
    };

/**
 * A TableRef provides one level of indirection from a Table
 */
template < typename tname, typename aname >
    using TableRef = Table< tname, aname > const *;

/**
 * A Foreign Key is a special type of key that uniquely identifies
 * a row in a different table. It subclasses a Key because it is a
 * subset of attributes in this table, but those attributes can be
 * referenced in a separate table
 */
template < typename tname, typename aname >
    struct ForeignKey : Key< aname >
    {
        TableRef< tname, aname > references;
    };

/**
 * Provides a container for multiple foreign keys
 */
template < typename tname, typename aname >
    using ForeignKeySet = std::vector< ForeignKey< tname, aname > >;


template < typename tname, typename aname >
    struct Table
    {
    	tname name;
    	AttributeSet< aname > attributes;
    	Key< aname > primary_key;
        ForeignKeySet< tname, aname > foreign_keys;
    };

/**
 * A (relational) Database is thus just a collection of Tables.
 */
template < typename tname, typename aname >
    using Database = std::vector< Table< tname, aname > >;


// Comparators

/**
 * Determines whether two keys refer to the same set of attributes,
 * where two sets {a,b} and {a,b} are considered equal if their elements
 * are the same, not if their addresses are the same.
 */
template < typename T >
    bool operator == ( Key< T > const& k1, Key< T > const& k2 )
    {
        if ( k1.attributes.size() != k2.attributes.size() ) { return false; }
        return set_equality( k1.attributes.cbegin(), k1.attributes.cend()
                           , k2.attributes.cbegin(), k2.attributes.cend()
                           , []( T const * a1, T const* a2 ){ return *a1 == *a2; } );
    }

/**
 * The negation of equality. Determines if two keys are distinct, i.e., there is at least
 * one attribute in one key but not the other.
 */
template < typename T >
    bool operator != ( Key< T > const& k1, Key< T > const& k2 )
    {
        return ! operator == ( k1, k2 );
    }

/**
 * Determines whether two foreign keys refer both to the same attributes and the same table.
 * Equality is determined with respect to dereferenced values, not addresses.
 */
template < typename S, typename T >
bool inline operator == ( ForeignKey< S, T > const& k1, ForeignKey< S, T > const& k2 )
    {
        if( *( k1.references ) != *( k2.references ) ) { return false; }
        return static_cast< Key< T > const >( k1 ) == static_cast< Key< T > const >( k2 );
    }

/**
 * The negation of equality. Determines if two foreign keys are distinct.
 */ 
template < typename S, typename T >
    bool inline operator != ( ForeignKey< S, T > const& k1, ForeignKey< S, T > const& k2 )
    {
        return ! operator == ( k1, k2 );
    }

/**
 * Determines whether two tables are the equal. Tables are considered to be equal if they have
 * the same schema (name and attribute names) and constraints (primary keys have the same attribute
 * names and foreign keys refer to tables with the same names).
 */ 
template < typename tname, typename aname >
    bool inline operator == ( Table< tname, aname > const& t1, Table< tname, aname > const& t2 )
    {
        return t1.name == t2.name
            && t1.attributes == t2.attributes
            && t1.primary_key == t2.primary_key
            && t1.foreign_keys == t2.foreign_keys;
    }

/**
 * The negation of equality. Tables have different schemata or different constraints.
 */
template < typename tname, typename aname >
    bool inline operator != ( Table< tname, aname > const& t1, Table< tname, aname > const& t2 )
    {
        return ! operator == ( t1, t2 );
    }


/**
 * Copies to stream s the primary key indicated by key. For key {a,b}, uses the format:
 * PRIMARY KEY (`a`, `b`)
 */
template < typename aname >
    std::ostream & operator << ( std::ostream & s, Key< aname > const& key )
    {
        // check if PK is empty
        if( key.attributes.size() == 0 ) { return s; }

        // else copy all but last element with a comma separator and add back element afterwards
        s << "PRIMARY KEY (`";
        std::transform( key.attributes.cbegin(), key.attributes.cend() - 1
                      , std::ostream_iterator< aname >( s, "`, `"), []( auto const& attribute_ref )
        {
            return *attribute_ref;
        } );
        s << *( key.attributes.back() ) << "`)";

        return s;
    }

/**
 * Copies to stream s the ForeignKey fkey. For a foreign key {a,b} that references a Table T
 * with attributes of the same name, the format is:
 * FOREIGN KEY (`a`, `b`) REFERENCES `T`(`a`, `b`)
 */
template < typename tname, typename aname >
    std::ostream & operator << ( std::ostream & s, ForeignKey< tname, aname > const& fkey )
    {
        // check if FK is empty
        if( fkey.attributes.size() == 0 ) { return s; }

        // else copy key attributes:
        s << "FOREIGN KEY (`";
        std::transform( fkey.attributes.cbegin(), fkey.attributes.cend() - 1
                      , std::ostream_iterator< aname >( s, "`, `"), []( auto const& attribute_ref )
        {
            return *attribute_ref;
        } );
        s << *( fkey.attributes.back() ) << "`)";

        // copy referencing relation
        s << " REFERENCES `"
          << fkey.references->name
          << "`(`";

        std::transform( fkey.references->primary_key.attributes.cbegin(), fkey.references->primary_key.attributes.cend() - 1
                      , std::ostream_iterator< aname >( s, "`, `"), []( auto const& attribute_ref )
        {
            return *attribute_ref;
        } );
        
        s << *( fkey.references->primary_key.attributes.back() ) << "`)";
        
        return s;
    }

/**
 * Copies to stream s the ForeignKeySet fkey. Each foreign key is delimited by a comma.
 */
template < typename tname, typename aname >
    std::ostream & operator << ( std::ostream & s, ForeignKeySet< tname, aname > const& fkey )
    {
        // check if any FK's
        if( fkey.size() == 0 ) { return s; }

        // else copy each FK with a separating comma, handling the last one differently
        std::copy( fkey.cbegin(), fkey.cend() - 1, std::ostream_iterator< ForeignKey< tname, aname > >( s, ", ") );
        s << fkey.back();
        
        return s;
    }

/**
 * Copies to stream s the entire table t. For a table S with attributes {a,b} on which a is a primary key
 * and b is a foreign key to a table T in which it has the same name, the format is:
 * CREATE TABLE `S`(`a` INT, `b` INT, PRIMARY KEY(`a`), FOREIGN KEY(`b`) REFERENCES `T`(`b`));
 */
template < typename tname, typename aname >
    std::ostream & operator << ( std::ostream & s, Table< tname, aname > const& t )
    {
        s << "CREATE TABLE `"
          << t.name
          << "`(";

        if( t.attributes.size() > 0 )
        {
            s << "`";
            std::copy( t.attributes.cbegin(), t.attributes.cend() - 1, std::ostream_iterator< aname >( s, "` INT, `") );
            s << t.attributes.back() << "` INT";

            if( t.primary_key.attributes.size() > 0 )
            {
                s << ", " << t.primary_key;
                if( t.foreign_keys.size() > 0 )
                {
                    s << ", " << t.foreign_keys;
                }
            }
        }

        s << ");";

        return s;
    }

/**
 * Prints to stream s the Database db. The tables in db are new-line separated.
 */
template < typename tname, typename aname >
    std::ostream & operator << ( std::ostream & s, Database< tname, aname > const& db )
    {
        std::copy( db.cbegin(), db.cend(), std::ostream_iterator< Table< tname, aname > >( s, "\n" ) );
        return s;
    }

} // namespace sql
} // namespace a2
} // namespace csc370
