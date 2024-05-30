import list_EBS_snapshots,list_running_EC2_instances,boto3
ec2 = boto3.client('ec2', region_name='eu-west-3')
ec2_running_set=list_running_EC2_instances.get_all_instances_Ids()
snapshots_List=list_EBS_snapshots.get_all_snapshots()
"""# Iterate through each snapshot and 
delete if it's not attached to any volume or the volume is not attached to a running instance"""
for snapshot in snapshots_List:
    snapshot_id = snapshot['Snapshot_id']
    volumeId = snapshot['VolumeId']
    print(f'{snapshot_id} has {volumeId}')
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
            if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")