import copy
import datetime
import tdxlib.tdx_integration
import tdxlib.tdx_api_exceptions

class TDXKnowledgebaseIntegration(tdxlix.tdx_integration.TDXIntegration):
     '''
     TDX Provided API methods
        1. POST
            Create a KB article
            Add attachement to an article
            Add relationship btween two KB articles
            Create a KB Category
            Get a list of KB articles
        2. GET
            Gets a KB article
            Gets a list of assets and config items assiocaited with a specific article
            Gets a list of KB articles associated with a specific article
            Gets the categories for the service context
            Gets the specified category
        3. PUT
            Edits an existing article
            Edits a specific category
        4. DELETE
            Deletes a KB article
            Removes a relationship between two KB articles
            Deltes a specific category
    '''

    def __init__(self): 