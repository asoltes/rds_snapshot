import boto3
from jinja2 import Environment, FileSystemLoader
import os
import argparse

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    else:
        print(f"Directory already exists: {directory}")

def get_aws_account_number():
    sts_client = boto3.client('sts')
    account_id = sts_client.get_caller_identity()['Account']
    return account_id

def get_rds_instance_names():
    rds_client = boto3.client('rds', region_name=args.region)
    response = rds_client.describe_db_instances()
    instance_names = [instance['DBInstanceIdentifier'] for instance in response['DBInstances']]
    return instance_names


def render_groovy_template(instance_names, aws_account_number):
    env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))
    template = env.get_template('groovy_template.j2')
    output = template.render(instance_names=instance_names, aws_account_number=aws_account_number)
    return output

def save_groovy_script(output):
    with open(f'{aws_account_id}/Jenkinsfile', 'w') as file:
        file.write(output)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate RDS snapshot Jenkinsfile')
    parser.add_argument('-r', '--region', metavar='region', type=str, help='specify the rds region')
    args = parser.parse_args()
    aws_account_id = get_aws_account_number()
    create_directory_if_not_exists(aws_account_id)
    instance_names = get_rds_instance_names()
    groovy_script = render_groovy_template(instance_names, aws_account_id)
    save_groovy_script(groovy_script)
    print(f"Generated Jenkinsfile is now on {aws_account_id}")
