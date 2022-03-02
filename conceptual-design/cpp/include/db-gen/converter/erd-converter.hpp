/**
 * Methods for converting an Entity-Relationship Diagram (ERD) into a set of SQL DDL queries.
 */

#include "db-gen/common/erd-types.hpp"
#include "db-gen/common/sql-table-types.hpp"

namespace csc370 {
namespace a2 {

/**
 * Given an entity-relationship diagram (ERD) in the format of the erd::ERD class,
 * returns a set of corresponding tables in the format of the sql::Database< tname, aname > class.
 * 
 * @TODO: Complete the implementation of this method!
 */
template < typename tname, typename aname >
  sql::Database< tname, aname > convert_to_table( erd::ERD )
  {
      return sql::Database< tname, aname >{};
  }

} // namespace a2
} // namespace csc370
