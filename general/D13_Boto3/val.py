x= [{'Grantee': {'DisplayName': 'dhuapriti02', 'ID': 'a834408a3ebeecec34b0d1661ebab424047c924910f227d774b84c93570cf846', 'Type': 'CanonicalUser'}, 'Permission': 'FULL_CONTROL'}]
for item in x:
    my_d=item['Grantee']
    print (my_d)
    for ii in my_d.items():
        print (ii)