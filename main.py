#####################################################################
# @author Navdeep Singh Bagga,
#         Information Manager, Winter-Fall 2017
#   @info Website for U-M School of Information's masters student
#         association containing important info about the org as well
#         as quick resources to connect to the school administration.
#   @term Fall 2017
#####################################################################



# Import dependecies:
import os
import json
import jinja2
import webapp2
from datetime import datetime
import logging


# Setup the Jinja2 environment:
JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader( os.path.dirname( __file__ ) + "/templates" ),
    extensions = [ "jinja2.ext.autoescape" ],
    autoescape = True )


# My variables:
DATA_FILES_PATH = "data/";


# Read data files:
with open( DATA_FILES_PATH + "officers.json" ) as data_file:
    officersData = json.load( data_file )

with open( DATA_FILES_PATH + "events.json" ) as data_file:
    eventsData = json.load( data_file )



logging.info( "Booting up the web server....." )


# Handler for `/`
# -------------------------------------------------------------------
class IndexHandler( webapp2.RequestHandler ):
    def get( self ):
        yr = datetime.now().year
        logging.info( "The current year is " + str( yr ) )
        self.response.write( JINJA_ENVIRONMENT.get_template( "index.html" ).render({ "currYear": yr }) )

# Handler for `/events`
# -------------------------------------------------------------------
class EventHandler( webapp2.RequestHandler ):
    def get( self ):
        _html = JINJA_ENVIRONMENT.get_template( "cmpt.event.html" ).render({ "data": eventsData })
        self.response.write( JINJA_ENVIRONMENT.get_template( "events.html" ).render({ "eventsHtml": _html }) )

# Handler for `/org-officers`
# -------------------------------------------------------------------
class OfficersHandler( webapp2.RequestHandler ):
    def get( self ):
        _html = JINJA_ENVIRONMENT.get_template( "cmpt.officer.html" ).render({ "data": officersData })

        self.response.write( JINJA_ENVIRONMENT.get_template( "officers.html" ).render({ "officersHtml": _html }) )

# Handler for `/resources`
# -------------------------------------------------------------------
class ResourcesHandler( webapp2.RequestHandler ):
    def get( self ):
        self.response.write( JINJA_ENVIRONMENT.get_template( "resources.html" ).render() )

# Handler for `/contact`
# -------------------------------------------------------------------
class ContactHandler( webapp2.RequestHandler ):
    def get( self ):
        self.response.write( JINJA_ENVIRONMENT.get_template( "contact.html" ).render() )

# Handler for `404-error`
# -------------------------------------------------------------------
class Error404Handler( webapp2.RequestHandler ):
    def get( self ):
        self.response.write( JINJA_ENVIRONMENT.get_template( "error404.html" ).render() )


# App routes:
app = webapp2.WSGIApplication([
    ( "/", IndexHandler ),
    ( "/events", EventHandler ),
    ( "/org-officers", OfficersHandler ),
    ( "/resources", ResourcesHandler ),
    ( "/contact-us", ContactHandler ),
    ( "/.*", Error404Handler )
], debug = True )


def formatDate( dt ):
    _dt = datetime( dt[ "year" ], dt[ "month" ], dt[ "date" ] )
    return [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ][ _dt.weekday() ] + ", " + [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ][ _dt.month - 1 ] + " " + str( _dt.day )
JINJA_ENVIRONMENT.filters[ "formatDate" ] = formatDate


logging.info( "Web server boot-up successful!" )