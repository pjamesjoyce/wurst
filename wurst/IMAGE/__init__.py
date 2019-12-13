import json
import os
import io as py_io
import base64

from .io import load_image_data_file

from .metadata import region_topology


def _to_filelike(bytestring):
    return py_io.BytesIO(base64.b64decode(bytestring))


IMAGE_TOPOLOGY = json.load(
    _to_filelike(region_topology)
)
