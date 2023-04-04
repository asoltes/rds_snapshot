# Creating AWS RDS Snapshots

`python3 rds_snapshot.py -db database-1,database-2 -r us-east-1` 
or
`python3 rds_snapshot.py --db_instances database-1,database-2 --region us-east-1`


# Generate Jenkinsfile

`cd generatejenkinsfile`
`python3 create_jenkinsfile_rds.py -r ap-southeast-1`