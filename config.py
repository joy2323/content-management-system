import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('cmsimg') or 'ENTER_STORAGE_ACCOUNT_NAME'
    BLOB_STORAGE_KEY = os.environ.get('5B3nk/TzqEDfOCVviRN7Fl4VqgaEc2QUTdRuEf7308yg+6yY5Tlpqb0y8hBfQOSm5NJhMfaLST+sdmwC+s7n8Q==') or 'ENTER_BLOB_STORAGE_KEY'
    BLOB_CONTAINER = os.environ.get('images') or 'ENTER_IMAGES_CONTAINER_NAME'

    SQL_SERVER = os.environ.get('contentmanage') or 'ENTER_SQL_SERVER_NAME.database.windows.net'
    SQL_DATABASE = os.environ.get('cms') or 'ENTER_SQL_DB_NAME'
    SQL_USER_NAME = os.environ.get('systemadmin') or 'ENTER_SQL_SERVER_USERNAME'
    SQL_PASSWORD = os.environ.get('Content2020') or 'ENTER_SQL_SERVER_PASSWORD'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "YERvVnj1i7J-s6J_3IdS.ngyu33I._g787"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "c74e6a2d-fd48-4b68-8da2-f14ac4c05f9d"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session