import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Let's use Amazon EC2
ec2 = boto3.client('ec2')

response = ec2.describe_key_pairs()
print(response)

# Retrieves all regions/endpoints that work with EC2
response = ec2.describe_regions()
print('Regions:', response['Regions'])

# Retrieves availability zones only for region of the ec2 object
response = ec2.describe_availability_zones()
print('Availability Zones:', response['AvailabilityZones'])