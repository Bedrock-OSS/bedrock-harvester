'''
Usage: Run the script and optionally add commandline arguments to it. Default
configuration (no arguments) downloads the stable version packs.

--download_mode ["stable" or "beta"]
--rp_url <the url to download resourcepack>
--bp_url <the url to download behaviorpack>

rp_url and bp_url overwrites the download mode.

Examples:
    Downloading beta packs and extracting data from them:
        python main.py --download_mode beta

    Downloading packs from custom urls
        python main --bp_url example.com --rp_url example1.com

The scripts uses temporary path ".tmp". The path is not cleared after the
execution. The path is removed and added again at the start of the script.
'''
import sys
from zipfile import ZipFile
import os
import shutil


from downloader import download_file
from harvester import harvest
from sound_harvester import strip_sounds

argv = sys.argv

# Reading the commandline arguments
try:
    DOWNLOAD_MODE=argv[argv.index('--download_mode')+1]
except:
    DOWNLOAD_MODE='stable'

if DOWNLOAD_MODE=='stable':
    RP_URL='https://aka.ms/resourcepacktemplate'
    BP_URL='https://aka.ms/behaviorpacktemplate'
elif DOWNLOAD_MODE=='beta':
    RP_URL='https://aka.ms/MinecraftBetaResources'
    BP_URL='https://aka.ms/MinecraftBetaBehaviors'
else:
    raise Exception(f'Unknown download mode {DOWNLOAD_MODE}.')

try:
    RP_URL=argv[argv.index('--rp_url')+1]
except:
    pass

try:
    RP_URL=argv[argv.index('--rp_url')+1]
except:
    pass


SKIP_DOWNLOAD='--skip_download' in argv


def main():
    if not SKIP_DOWNLOAD:
        if os.path.exists('.tmp'):
            shutil.rmtree('.tmp')
        os.makedirs('.tmp', exist_ok=True)

        print("Downloading files...")
        download_file(RP_URL, '.tmp/rp.zip')
        download_file(BP_URL, '.tmp/bp.zip')

    if os.path.exists('.tmp/rp'):
        shutil.rmtree('.tmp/rp')
    print('Extracting resource pack')
    with ZipFile('.tmp/rp.zip') as zipf:
        zipf.extractall('.tmp/rp')

    if os.path.exists('.tmp/bp'):
        shutil.rmtree('.tmp/bp')
    print('Extracting behavior pack')
    with ZipFile('.tmp/bp.zip') as zipf:
        zipf.extractall('.tmp/bp')
    
    stable = DOWNLOAD_MODE == 'stable'

    harvest('.tmp/bp', stable)
    strip_sounds('.tmp/rp/sounds/sound_definitions.json')

if __name__ == "__main__":
    main()
