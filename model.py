from sqlobject import *
import os.path

dbfile = 'small_taxa.db3'

def init(new=False):
    conn_str = os.path.abspath(dbfile)
    conn_str = "sqlite:"+conn_str
    print(conn_str)
    sqlhub.processConnection = connectionForURI(conn_str)

    if new:
        Taxonomy.dropTable(ifExists=True)
        Name.dropTable(ifExists=True)
        Taxonomy.createTable()
        Name.createTable()

class Taxonomy(SQLObject):
    taxid = IntCol(alternateID=True)
    scientific_name = StringCol()
    rank = StringCol()
    parent = ForeignKey("Taxonomy", default=None)
    children = MultipleJoin("Taxonomy", joinColumn="parent_id")
    names = MultipleJoin("Name")

class Name(SQLObject):
    taxonomy = ForeignKey("Taxonomy")
    name = StringCol()
    name_class = StringCol()
