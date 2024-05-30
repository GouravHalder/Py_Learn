import boto3

def get_account_id():
    # Initialize a session using STS
    sts = boto3.client('sts')

    # Retrieve caller identity
    response = sts.get_caller_identity()
    # Extract account ID
    account_id = response['Account']
    for items in response['ResponseMetadata']:
        print(f"{items} ==> {response['ResponseMetadata'][items]}")
    return account_id

if __name__ == "__main__":
    account_id = get_account_id()
    print(f"AWS Account ID: {account_id}")
