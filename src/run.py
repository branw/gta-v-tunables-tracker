import requests
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import json
import pickle
from datetime import datetime
from glob import glob
import os
from pathlib import Path
import jsondiff
import pprint
import re

KEY = bytearray([
    0xf0, 0x6f, 0x12, 0xf4, 0x9b, 0x84, 0x3d, 0xad,
    0xe4, 0xa7, 0xbe, 0x05, 0x35, 0x05, 0xb1, 0x9c,
    0x9e, 0x41, 0x5c, 0x95, 0xd9, 0x37, 0x53, 0x45,
    0x0a, 0x26, 0x91, 0x44, 0xd5, 0x9a, 0x01, 0x15])

PLATFORMS = ['xbox360', 'xboxone', 'xboxsx', 'ps3', 'ps4', 'ps5', 'pcros']

failure = False

# Ensure the history directory exists
Path('history/').mkdir(parents=False, exist_ok=True)

for platform in PLATFORMS:
    try:
        url = f'http://prod.cloud.rockstargames.com/titles/gta5/{platform}/0x1a098062.json'
        response = requests.get(url)
        content = response.content
    except Exception as e:
        print(f'Failed to get {url}', e)
        failure = True
        continue

    trailer_len = len(content) % 16
    ciphertext = content[:-trailer_len] if trailer_len > 0 else content

    cipher = AES.new(KEY, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext) + (content[-trailer_len:] if trailer_len > 0 else b'')

    try:
        payload = json.loads(plaintext)
    except Exception as e:
        print('Failed to parse JSON:', e)
        failure = True

    last_modified = datetime.strptime(response.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z').isoformat().replace(':', '-')

    entry = {
        'last_modified': last_modified,
        'ciphertext': ciphertext.hex(),
        'payload': payload,
    }

    previous_entry_paths = sorted(glob(f'history/*-{platform}-*.json'))

    previous_entry = None
    previous_entry_path = None
    if previous_entry_paths:
        previous_entry_path = previous_entry_paths[-1]
        with open(previous_entry_path, 'r') as f:
            previous_entry = json.loads(f.read())

    hasher = SHA256.new()
    hasher.update(ciphertext)
    ciphertext_hash = hasher.hexdigest()

    entry_path = f'history/{last_modified}-{platform}-{ciphertext_hash}.json'

    no_changes = previous_entry and Path(previous_entry_path) == Path(entry_path)
    num_previous_entries = len(previous_entry_paths)
    if no_changes:
        num_previous_entries -= 1

    # Update dates in the README
    with open('README.md', 'r') as f:
        readme = f.read()
    with open('README.md', 'w') as f:
        f.write(re.sub(
            fr'\[`tunables-{platform}.json`\](.*)\|`(.*)`\|(\[?)(\d+)',
            f'[`tunables-{platform}.json`]\\1|`{last_modified}`|\\g<3>{num_previous_entries}',
            readme))   

    if no_changes:
        print(f'No changes for {platform} - matches {previous_entry_path}')
        continue

    # Write the historical entry
    with open(entry_path, 'w') as f:
        f.write(json.dumps(entry, indent=4))

    # We still want to log the entry when payload parsing fail so that we can
    # backfill existing entries after fixing the script. However, we cannot
    # update the current entry or changelog.
    if payload:
        # Update the current entry
        with open(f'tunables-{platform}.json', 'w') as f:
            f.write(json.dumps(payload, indent=4))

        # Update the changelog
        if previous_entry:
            print(f'Diffing payloads of {entry_path} and {previous_entry_path}')

            diff = jsondiff.diff(previous_entry['payload'], entry['payload'], syntax='explicit')
            with open(f'changelog-{platform}.md', 'a') as f:
                if f.tell() == 0:
                    f.write(f'# Changelog for `{platform}`\n\n')
                
                f.write(f'## `{previous_entry["last_modified"]}` to `{last_modified}`\n\n```\n')
                pprint.pprint(diff, f)
                f.write('```\n')     

# Fail this GitHub Actions step so we get a notification when something went
# wrong while grabbing the file or parsing it
if failure:
    exit(1)
