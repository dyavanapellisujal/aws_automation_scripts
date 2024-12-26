import boto3 , sys , csv 
import pandas as pd


if len(sys.argv) >= 2:
    

    iam = boto3.client('iam')

    response = iam.get_paginator('list_users')
    data_list=[]

    for user in response.paginate():
        
        for j in range (0,len(user['Users'])):
            
            

            a= dict((user['Users'])[j])
            
            
            get_mfa=iam.list_mfa_devices(UserName=a['UserName'])
            
            if len(get_mfa['MFADevices']) > 0:
                
                data={'IAM_USER':a['UserName'],'UserId':a['UserId'],'ARN':a['Arn'],'CreateDate':a['CreateDate'],'MFA_STATUS':'Enabled'}
            else:
                
            
                data={'IAM_USER':a['UserName'],'UserId':a['UserId'],'ARN':a['Arn'],'CreateDate':a['CreateDate'],'MFA_STATUS':'Disabled'}
            
            data_list.append(data)
    
        try:
            with open(sys.argv[1],'w',newline="") as csvfile:
                fieldnames = ['IAM_USER', 'UserId', 'ARN', 'CreateDate','MFA_STATUS']
                write_csv = csv.DictWriter(csvfile,fieldnames=fieldnames)
                write_csv.writeheader()
                write_csv.writerows(data_list)
        

            ask_for_excel=input("Do you want a excel file for the same?: Y/N")
            if (ask_for_excel.strip(" ")).lower()=="y":
                df = pd.read_csv("./"+sys.argv[1])
                df.to_excel(sys.argv[1][:-4]+".xlsx", sheet_name="Testing", index=False)
    

            
 
        except Exception as e:
            print(e)
            
            
            

     
        
        

    
    
    
else:
    print("Please provide a name for the csv file to be created")
