import boto3
def get_all_snapshots():
    # Initialize a session using Amazon EC2
    snapshot_list = []
    ec2 = boto3.client('ec2', region_name='eu-west-3')
    snapshots=ec2.describe_snapshots(OwnerIds=['self'])
    for snapshot in snapshots['Snapshots']:
        snapshot_dict=dict()
        snapshot_dict['Snapshot_id']=snapshot['SnapshotId']
        snapshot_dict['VolumeId']=snapshot['VolumeId']
        snapshot_list.append(snapshot_dict)
    return(snapshot_list)
if __name__ == "__main__":
    print(get_all_snapshots())
   




