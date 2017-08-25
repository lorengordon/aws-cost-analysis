from __future__ import print_function
import json
import logging
import os
import sys

import boto3

__location__ = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(__location__, "../"))
sys.path.append(os.path.join(__location__, "../vendored"))

import awscostusageprocessor.processor as cur
import awscostusageprocessor.consts as consts

log = logging.getLogger()
log.setLevel(logging.INFO)
ddbclient = boto3.client('dynamodb')

"""
This function starts the process that copies and prepares incoming AWS Cost and Usage reports.
"""

def handler(event, context):

    log.info("Received event {}".format(json.dumps(event)))

    curprocessor = cur.CostUsageProcessor(**event)
    #This function only supports processing files for Athena (for now).
    curprocessor.process_latest_aws_cur(consts.ACTION_PREPARE_ATHENA)
    log.info("Return object:[{}]".format(event))
    return event
