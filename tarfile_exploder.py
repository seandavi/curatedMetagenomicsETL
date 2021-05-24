#!/usr/bin/env python
"""Get all the legacy tar files and expand to Google Cloud Storage

Requires `gsutil` and appropropriate setup for google cloud SDK
"""
import subprocess

c = subprocess.check_output('gsutil ls gs://data-curatedmetagenomics/*.tar.gz'.split()).split(b'\n')

for tgz1 in c[:-1]:
    tgz=tgz1.decode('utf-8')
    print(tgz)
    fname = tgz.split('/')[3]
    study_id = fname.replace('.tar.gz','')
    try:
        print(f'gsutil cp {tgz} {fname}'.split())
        ret = subprocess.call(f'gsutil cp {tgz} {fname}'.split())
        print(ret)
        ret = subprocess.call(f'tar -xvzf {fname}'.split())
        print(ret)
        #ret = subprocess.call('find . -type f -name '*.tsv' -exec gzip "{}" \;'.split())
        #print(ret)
        ret = subprocess.call(f'gsutil -m cp -r {study_id} gs://cmgd-data/manual/'.split())
        print(ret)
        subprocess.call(f'rm -rf {fname} {study_id}'.split())
    except Exception as e:
        print(e)
