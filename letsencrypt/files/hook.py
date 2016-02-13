#!/usr/bin/env python

import logging
import sys

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def create_txt_record(args):
    domain, token = args[0], args[2]
    logger.info(' + domain: {0}'.format(domain))
    logger.info(' + token: {0}'.format(token))
    return


def delete_txt_record(args):
    domain, token = args[0], args[2]
    logger.info(' + domain: {0}'.format(domain))
    logger.info(' + token: {0}'.format(token))
    return


def deploy_cert(args):
    domain, privkey_pem, cert_pem, fullchain_pem = args
    logger.info(' + ssl_certificate: {0}'.format(fullchain_pem))
    logger.info(' + ssl_certificate_key: {0}'.format(privkey_pem))
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
