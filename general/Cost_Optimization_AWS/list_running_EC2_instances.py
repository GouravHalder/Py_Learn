import boto3,pprint
def get_all_instances_Ids():
    # Initialize a session using Amazon EC2
    active_instance_ids=set()
    ec2 = boto3.client('ec2', region_name='eu-west-3')
    # Get all active EC2 instance IDs
    active_instances=ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for reservation in active_instances['Reservations']:
       for instance in reservation['Instances']:
            if __name__ == "__main__":
                print("Instance ID:", instance['InstanceId'])
                print("Instance Type:", instance['InstanceType'])
                print("Launch Time:", instance['LaunchTime'])
                print("Public DNS Name:", instance.get('PublicDnsName', 'N/A'))
                print("Public IP Address:", instance.get('PublicIpAddress', 'N/A'))
                print("Private IP Address:", instance.get('PrivateIpAddress', 'N/A'))
                print("State:", instance['State']['Name'])
                print("Tags:", instance.get('Tags', 'None'))
                print("-" * 50)
            active_instance_ids.add(instance['InstanceId'])
    return active_instance_ids
if __name__ == "__main__":
    print(get_all_instances_Ids())