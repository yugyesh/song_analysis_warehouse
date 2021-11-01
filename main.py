from src.create_tables import main, connect_aws, create_tables, drop_tables

from src.etl import copy_to_staging, transform_staging

# load data to the aws
cur, conn = connect_aws()

# drop_tables
drop_tables(cur, conn)

# create_tables
create_tables(cur, conn)

# copy data from s3 to staging tables in redshift
copy_to_staging(cur, conn)

# transform staging table data to dimensional table
transform_staging(cur, conn)
