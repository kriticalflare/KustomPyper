class Error(Exception):
   """Base class for other exceptions"""
   pass

class NoResultsFound(Error):
   """Raised when there are no results found for search term """
   pass
   