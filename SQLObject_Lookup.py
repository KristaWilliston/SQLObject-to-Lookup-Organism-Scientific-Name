#Write a python program using SQLObject to lookup the scientific name for a user-supplied organism name

import sys
from sqlobject import *
import os.path

if len(sys.argv) < 2:
    print("Usage: python script.py <organism_name>")
    sys.exit(1)

# Database connection setup
dbfile = "taxa.db3"

conn_str = os.path.abspath(dbfile)
conn_str = 'sqlite:'+conn_str

sqlhub.processConnection = connectionForURI(conn_str)

# Define the data model for legacy database
class Taxonomy(SQLObject):
    class sqlmeta:
        idName = "tax_id"
        fromDatabase = True
    names = MultipleJoin("Name", joinColumn="tax_id")

class Name(SQLObject):
    class sqlmeta:
        fromDatabase = True
    taxa = ForeignKey("Taxonomy", dbName="tax_id")

# Function to lookup the scientific name
def lookup_scientific_name(organism_name):
    try:
        # Search the Name table for the organism name
        name_query = Name.selectBy(name=organism_name)
        name_entry = list(name_query)
        if not name_entry:
            print("Can't find name",organism_name,"in the database")
            return

        # Get the Taxonomy object through the foreign key
        taxonomy_entry = name_entry[0].taxa
        print("Scientific name of",organism_name, "is",taxonomy_entry.scientificName)
    except SQLObjectNotFound:
        print("Can't find scientific name for",organism_name)

organism_name = " ".join(sys.argv[1:])
lookup_scientific_name(organism_name)
