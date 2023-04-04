import argparse
import boto3
import concurrent.futures

def start_rds_instances(instance_ids):
    """
    Starts stopped Amazon RDS instances and waits for them to be available.
    
    :param instance_ids: A list of RDS instance IDs to start.
    """
    rds_client = boto3.client('rds')
    
    # Start the RDS instances
    for instance_id in instance_ids:
        response = rds_client.start_db_instance(DBInstanceIdentifier=instance_id)
        
        # Get the status of the instance
        instance_status = response['DBInstance']['DBInstanceStatus']
        
        # If the instance is already available, skip it
        if instance_status == 'available':
            continue
        
        # Define a function to wait for the instance to be available
        def wait_for_instance():
            waiter = rds_client.get_waiter('db_instance_available')
            waiter.wait(DBInstanceIdentifier=instance_id)
        
        # Use concurrent.futures to wait for the instance to be available concurrently
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(wait_for_instance)
            future.result()

if __name__ == '__main__':
    # Set up argparse to accept a comma-separated string of instance IDs as a command-line argument
    parser = argparse.ArgumentParser(description='Start stopped Amazon RDS instances.')
    parser.add_argument('instance_ids', metavar='INSTANCE_IDS', help='A comma-separated list of RDS instance IDs to start.')
    args = parser.parse_args()
    
    # Split the comma-separated string into a list of instance IDs
    instance_ids = args.instance_ids.split(',')
    
    # Call the start_rds_instances function with the provided instance IDs
    start_rds_instances(instance_ids)
