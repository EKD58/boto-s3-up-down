#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
boto sample code.
S3 uppload download test
main function
"""

import sys
import boto3


AWS_ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxx'
AWS_SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
REGION_NAME = 'ap-northeast-1'



# -----------------------------------------------------------------------------
def upload_func(in_bucket, in_key, in_up_file):
	"""
	upload test
	"""

	s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=REGION_NAME)

	bucket = s3.Bucket(in_bucket)
	bucket.upload_file(in_up_file, in_key)

	return



# -----------------------------------------------------------------------------
def download_func(in_bucket, in_key, in_out_file):
	"""
	download test
	"""

	s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=REGION_NAME)

	bucket = s3.Bucket(in_bucket)
	bucket.download_file(in_key, in_out_file)

	return



# -----------------------------------------------------------------------------
def main():
	"""
	main function
	"""

#	upload_func('bucketname', 'key/key.html', '/tmp/key_local.html')

#	download_func('bucketname', 'key/key.sh', '/tmp/key_local.sh')

	argvLen = len(sys.argv)
	if(argvLen != 4):
		print("[ERROR] please input (s3 bucket name) (s3 key name) (output path)")
		sys.exit(0)

	download_func(sys.argv[1], sys.argv[2], sys.argv[3])

	return
