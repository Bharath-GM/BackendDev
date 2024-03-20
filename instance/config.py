from urllib.parse import quote

class DevConfig:
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = ''
    # Database configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    user = 'BHARATH2308'
    password = quote('Zywa@2024')
    account = 'TRPCXKB-PNB53946'
    database = 'ZYWA'
    schema = 'PUBLIC'
    role ='ACCOUNTADMIN'
    warehouse= 'COMPUTE_WH'
    SQLALCHEMY_DATABASE_URI = f'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}&role={role}'

# Additional configuration can go here
# e.g., API keys for third-party services, configuration for mail server
