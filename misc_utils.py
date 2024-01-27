import os


def initialize_env():
    os.environ['DATA_ETL_REDSHIFT_USER_METRICS'] = 'xxxxxxx'
    os.environ['DATA_ETL_REDSHIFT_HOST_METRICS'] = 'redshift-cluster-1.xxxxxxxxxxxx.us-east-2.redshift.amazonaws.com'
    os.environ['DATA_ETL_REDSHIFT_USER_PW_METRICS'] = 'xxxxxxxxxx'
    os.environ['DATA_ETL_REDSHIFT_PORT'] = '5439'
    os.environ['DATA_ETL_AWS_ACCESS_KEY_ID'] = 'xxxxxxxxxxxxxxxx'
    os.environ['DATA_ETL_AWS_SECRET_KEY_ID'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    os.environ['DATA_ETL_SNOWFLAKE_USER'] = 'xxxx'
    os.environ['DATA_ETL_SNOWFLAKE_PW'] = 'xxxxxxx'
    os.environ['DATA_ETL_SNOWFLAKE_ACCOUNT'] = 'xxxxxxx.us-east-1'
