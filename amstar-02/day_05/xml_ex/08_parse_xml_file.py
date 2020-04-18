


#-----------------------------------------------------------------------------
# Import any needed libraries below
#-----------------------------------------------------------------------------
# We need the ElementTree module
import xml.etree.ElementTree


#-----------------------------------------------------------------------------
# Place any necessary functions below this.
#-----------------------------------------------------------------------------
def print_movie(movie, year):
    print ("The movie \"%s\" was released in %s.\n" % (movie, year))


#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------

# Load an XML file into the tree and get the root element.
xml = xml.etree.ElementTree.ElementTree(file='movies.xml')
root = xml.getroot()

# Get a list of all the movie elements in the file.
movies = root.findall('movie')

# Parse the movie element to get the "id" attribute, the title element and the 
# released element. 
for movie in movies:
    # Get the value of the "id" attribute
    id = movie.attrib['id']
    print ( "Parsing movie #" + id )
    
    # Get the text inside the first "title" tag. Returns None if the "title" 
    # tag is not found. Returns an empty string is returned if the tag was 
    # found but no text was found in the tag.
    title = movie.findtext('title')
    year = movie.findtext('released')
    
    print_movie(title, year)

