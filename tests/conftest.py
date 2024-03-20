from urllib.parse import quote

class TestConfig:
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    user = 'BHARATH2308'
    password = quote('Zywa@2024')
    account = 'TRPCXKB-PNB53946'
    database = 'ZYWA_TEST'
    schema = 'PUBLIC'
    role ='ACCOUNTADMIN'
    warehouse= 'COMPUTE_WH'
    SQLALCHEMY_DATABASE_URI = f'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}&role={role}'
