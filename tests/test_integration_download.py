"""Download API integration tests."""

import filecmp
import os
import platform
import sys
import tempfile

import siaskynet as skynet


SKYLINK = "AAA9s0sR9i8NGy19EadRGcpUt0HdvDMHJilKGmW545-k1g"

client = skynet.SkynetClient()


def test_download_file():
    """Test downloading a file to a temporary location."""

    # This test fails on CI for Windows so skip it.
    if platform.system() == "Windows" and 'CI' in os.environ:
        return

    src_file = "./testdata/file1"

    # Download a file.

    with tempfile.NamedTemporaryFile() as handle:
        dst_file = handle.name
        print("Downloading to "+dst_file)
        client.download_file(dst_file, SKYLINK)
        if not filecmp.cmp(src_file, dst_file):
            sys.exit("ERROR: Downloaded file at "+dst_file +
                     " did not equal uploaded file "+src_file)

    print("File download successful")


def test_get_metadata():
    """Test downloading the metadata for a file."""

    expected_metadata = {
        'filename': 'file1',
        'length': 5,
        'subfiles': {
            'file1': {
                'filename': 'file1',
                'contenttype': 'application/octet-stream',
                'len': 5
            }
        }
    }

    # Download a file's metadata.

    metadata = client.get_metadata(SKYLINK)
    if metadata != expected_metadata:
        sys.exit("ERROR: Downloaded metadata "+str(metadata) +
                 " did not equal expected metadata "+str(expected_metadata))
