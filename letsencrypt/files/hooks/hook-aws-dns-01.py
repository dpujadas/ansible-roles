#!/usr/bin/env python

import logging
import sys
import boto3
import time

DNS_TTL = 300

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

session = boto3.Session()
route53_client = session.client("route53")
iam_client = session.client("iam")


def find_zone_id_for_domain(domain):
    for page in route53_client.get_paginator("list_hosted_zones").paginate():
        for zone in page["HostedZones"]:
            if (
                domain.endswith(zone["Name"]) or
                (domain + ".").endswith(zone["Name"])
            ):
                return zone["Id"]


def wait_for_route53_change(change_id):
    while True:
        response = route53_client.get_change(Id=change_id)
        if response["ChangeInfo"]["Status"] == "INSYNC":
            return
        time.sleep(5)


def change_txt_record(action, domain, value):
    zone_id = find_zone_id_for_domain(domain)
    record = "{0}.{1}".format('_acme-challenge', domain)
    response = route53_client.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            "Changes": [
                {
                    "Action": action,
                    "ResourceRecordSet": {
                        "Name": record,
                        "Type": "TXT",
                        "TTL": DNS_TTL,
                        "ResourceRecords": [
                            {"Value": '"{}"'.format(value)}
                        ],
                    }
                }
            ]
        }
    )
    wait_for_route53_change(response["ChangeInfo"]["Id"])
    return


def create_txt_record(args):
    domain, token = args[0], args[2]

    change_txt_record("UPSERT", domain, token)
    return


def delete_txt_record(args):
    domain, token = args[0], args[2]

    change_txt_record("DELETE", domain, token)
    return


def file_get_contents(filename):
    with open(filename) as f:
        return f.read()


def deploy_cert(args):
    domain, privkey_pem, cert_pem, fullchain_pem, time_stamp = args

    privkey = file_get_contents(privkey_pem)
    cert = file_get_contents(cert_pem)
    fullchain = file_get_contents(fullchain_pem)
    chain = fullchain.replace(cert, '')
    cert_name = '{0}-{1}'.format(domain, time.strftime("%Y%m%d%H%M%S"))

    response = iam_client.upload_server_certificate(
        Path='/cloudfront/',
        ServerCertificateName=cert_name,
        PrivateKey=privkey,
        CertificateBody=cert,
        CertificateChain=chain,
    )
    new_cert_arn = response["ServerCertificateMetadata"]["Arn"]

    logger.info(" + Cert ARN: {0}".format(new_cert_arn))
    return


def main(argv):
    ops = {
        'deploy_challenge': create_txt_record,
        'clean_challenge': delete_txt_record,
        'deploy_cert': deploy_cert,
    }
    logger.info(" + Route53 hook executing: {0}".format(argv[0]))
    ops[argv[0]](argv[1:])


if __name__ == '__main__':
    main(sys.argv[1:])
