import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='eu-west-3')
    """# Iterate through each snapshot and 
    delete if it's not attached to any volume or the volume is not attached to a running instance"""
    snapshots=ec2.describe_snapshots(OwnerIds=['self'])
    for snapshot in snapshots['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volumeId = snapshot['VolumeId']
        print(f'{snapshot_id} has a {volumeId}')
        if not volumeId:
            response = ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as there is no volume attached ")
        else:
            # Double check if the volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volumeId])
                if not volume_response:
                    response = ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as there is no volume attached double cheked ")
            except ec2.exceptions.ClientError as e:
                print("-" * 50)
                print(e.response['Error']['Code'])
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                        # The volume associated with the snapshot is not found (it might have been deleted)
                        ec2.delete_snapshot(SnapshotId=snapshot_id)
                        print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")