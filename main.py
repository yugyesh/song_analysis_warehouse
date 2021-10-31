from src.create_tables import main, connect_aws

from src.etl import copy_to_staging, transform_log

# TODO: Refactor the method name
main()

# load data to the aws
cur, conn = connect_aws()

# copy data from s3 to staging tables in redshift
copy_to_staging(cur, conn)

# transform staging table data to dimensional table
# transform_log(cur, conn)
