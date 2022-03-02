/**
 * Defines the data types used to describe an Entity-Relationship Diagram (ERD)
 */

#include <string>  // std::string
#include <vector>  // std::vector


namespace csc370 {
namespace a2 {
namespace erd {

using Name = std::string;
using Flag = bool;

/**
 * An attribute of either an Entity Set or a Relationship in an ERD,
 * including a flag that indicates whether it is part of the primary key
 */
struct Attribute
{
	Name name;
	Flag is_primary_key;
};

/**
 * A collection of attributes
 */
using AttributeSet = std::vector< Attribute >;

/**
 * A relationship in an ERD that connects at least two (not necessarily distinct)
 * entity sets. This class does not specify any connections, just the name of the
 * relationship and any attributes attached thereto. 
 */
struct Relationship
{
	Name name;
	AttributeSet attributes;
};

/**
 * The number of times in which the tuple of an entity set could participate in
 * a relationship.
 */
enum class Multiplicity
{
	one,  /**< Each tuple of this entity set is unique in the relationship, if it exists at all */
	many, /**< Each tuple of this entity set can appear an arbitrary number of times in the relationship, including zero. */
};

/** A Connection specifies a relationship and a Multiplicity and corresponds to where an arrow meets an entity set */
using Connection = std::pair< Relationship const*, Multiplicity >;

/** A ConnectionList is a collection of Connections, since an Entity Set can be involved in multiple relationships. */
using ConnectionList = std::vector< Connection >;

/** A specialised connection list in which the multiplicity is dropped because all relationships are "IsA" relationships. */
using ParentList = std::vector< Relationship const * >;

/** A specialised connection list in which the multiplicity is dropped because all relationships are "supporting" relationships. */
using SupportingRelationshipList = std::vector< Relationship const * >;

/**
 * An Entity Set corresponds to some abstract object or thing.
 * It is described by a name and set of attributes as well as the connections it has to other entity sets.
 * The regular, IsA, and supporting relationships are separated into distinct collections.
 */
struct EntitySet
{
	Name name;
	AttributeSet attributes;
	ConnectionList connections;
	ParentList parents;
	SupportingRelationshipList supporting_relations;
};

/** A collection of entity sets. */
using EntitySetList = std::vector< EntitySet >;

/** A collection of relationships */
using RelationshipList = std::vector< Relationship >;

/** An Entity-Relationship Diagram (ERD) is simply the collection of entity sets, relationships, and attributes thereon. */
using ERD = std::pair< RelationshipList, EntitySetList >;


} // namespace erd
} // namespace a2
} // namespace csc370
