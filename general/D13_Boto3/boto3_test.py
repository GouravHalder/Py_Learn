import boto3
import pprint, json
client = boto3.client('s3')
#response = client.create_bucket(
 #   Bucket='pritidhua-demo-boto3-yt-786',
#)
response = client.get_bucket_acl(
    Bucket='pritidhua-demo-boto3-yt-786',
)
owner = response['Owner']
for items in response:
    if (items=='Owner'):
        owner = response['Owner']
        print(owner['DisplayName'])
    elif (items=='Grants'):
        grants= response['Grants']
        for item in grants:
            my_Grantee=item['Grantee']
            my_Perm=item['Permission']
            print(my_Grantee)
            print(my_Perm)
            if (my_Perm=='Permission'):
                print (item['Permission'])
            else:
                for Grantee_items in my_Grantee:
                    print(item['Grantee'][Grantee_items])
    else:
        pass
