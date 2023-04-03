import boto3
import time
import argparse
import concurrent.futures


current_time_str = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

def create_rds_snapshots(instance_names):
    rds = boto3.client('rds', region_name="us-east-1")
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create RDS snapshots')
    parser.add_argument('-db','--db_instance', metavar='db-instance', type=str, nargs='+',
                        help='a list of RDS instance names')
    args = parser.parse_args()

    create_rds_snapshots(args.db_instance)
