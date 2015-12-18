#!/usr/bin/env python2.7

import os, sys, re, random

deploy_root = os.path.realpath(os.path.join(__file__, "../.."))

import argparse

from ansible.inventory import Inventory
import ansible.constants as C

environments = [
    'devops',
    'delivery',
    'uat',
    'performance',
    'production',
]

applications = [
    'aliss_worker',
    'billing_adapter',
    'billing_id_service',
    'billing_results_worker',
    'billing_worker',
    'case_worker',
    'document_generation_worker',
    'frank_cc_zappa',
    'pdf_worker',
    'product_worker',
    'quote_worker',
    'rdx_agentless',
    'realtime_new_business_worker',
    'stub_worker'
    'docker'
]

print deploy_root
default_inventory = os.path.join(deploy_root, 'inventories/ec2.py')

print os.path.join(os.path.dirname(__file__), '..')
print os.path.dirname(os.path.realpath(__file__))
print os.path.abspath(os.path.dirname(__file__))

