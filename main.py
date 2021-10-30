from src.create_tables import main, connect_aws

from src.etl import copy_to_staging

main()

# load data to the aws
cur, conn = connect_aws()
copy_to_staging(cur, conn)
