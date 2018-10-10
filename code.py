# tag::import[]
from neo4j.v1 import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost", auth = ("neo4j", "neo"))
driver
# end::import[]


# tag::find-movies[]
with driver.session() as session:
    result = session.run("""
    MATCH (movie:Movie)<-[:ACTED_IN]-(actor)
    RETURN movie, actor
    """)

    for row in result:
        display(row)
# end::find-movies[]
