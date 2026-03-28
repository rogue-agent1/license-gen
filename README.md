# license_gen

Generate open source license files. 7 licenses with SPDX identifiers.

## Usage

```bash
# Generate MIT license
python3 license_gen.py mit --author "Your Name"

# Generate to specific file
python3 license_gen.py apache --author "Your Name" -o LICENSE

# List available licenses
python3 license_gen.py list

# License details
python3 license_gen.py info mit
```

## Available Licenses
MIT, Apache-2.0, GPL-3.0, BSD-2-Clause, ISC, Unlicense, CC0-1.0

## Zero dependencies. Single file. Python 3.8+.
