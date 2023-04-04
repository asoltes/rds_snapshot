import boto3
import time
import argparse
import sys
import concurrent.futures


current_time_str = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

def create_rds_snapshots(instance_names):
    rds = boto3.client('rds', region_name=args.region)
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(instance_names)) as executor:
        for instance_name in instance_names:
            snapshot_id = instance_name + f'-snapshot-{current_time_str}'
            future = executor.submit(rds.create_db_snapshot, DBInstanceIdentifier=instance_name, DBSnapshotIdentifier=snapshot_id)
            futures.append(future)
            print(f"Snapshot creation started for {instance_name}: {snapshot_id}")
        for future in concurrent.futures.as_completed(futures):
            try:
                response = future.result()
                snapshot_id = response['DBSnapshot']['DBSnapshotIdentifier']
                waiter = rds.get_waiter('db_snapshot_completed')
                waiter.wait(DBSnapshotIdentifier=snapshot_id)
                print(f"Snapshot {snapshot_id} is now available")
            except Exception as e:
                print(f"Error occurred while creating snapshot: {e}")
                sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create RDS snapshots')
    parser.add_argument('-db','--db_instances', metavar='db-instances', type=str,
                        help='a comma-separated list of RDS instance names')
    parser.add_argument('-r', '--region', metavar='region', type=str, help='specify the rds region')
    args = parser.parse_args()

    instance_names = [name.strip() for name in args.db_instances.split(',')]
    create_rds_snapshots(instance_names)
