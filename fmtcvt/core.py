import json
import os.path

import yaml


def convert(in_path: str, out_path: str):
    _, in_ext = os.path.splitext(in_path)
    _, out_ext = os.path.splitext(out_path)

    if in_ext == out_ext:
        raise ValueError(
            "in file path and out file path must have different extensions"
        )

    if in_ext == ".json":
        with open(in_path, mode="r") as f:
            data = json.load(f)
    elif in_ext in ".yaml":
        with open(in_path, mode="r") as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)

    if out_ext == ".json":
        with open(out_path, mode="w") as f:
            json.dump(data, f)
    elif out_ext in ".yaml":
        with open(out_path, mode="w") as f:
            yaml.dump(data, f)
