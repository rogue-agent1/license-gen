#!/usr/bin/env python3
"""license_gen — Generate open source license files.

Usage:
    license_gen.py mit --author "Rogue"
    license_gen.py apache --author "Rogue" --year 2026
    license_gen.py list
    license_gen.py info mit
"""

import sys
import argparse
from datetime import datetime

LICENSES = {
    'mit': {
        'name': 'MIT License',
        'spdx': 'MIT',
        'osi': True,
        'copyleft': False,
        'text': '''MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
''',
    },
    'apache': {
        'name': 'Apache License 2.0',
        'spdx': 'Apache-2.0',
        'osi': True,
        'copyleft': False,
        'text': '''                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   Copyright {year} {author}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
''',
    },
    'gpl3': {
        'name': 'GNU General Public License v3.0',
        'spdx': 'GPL-3.0-only',
        'osi': True,
        'copyleft': True,
        'text': '''Copyright (C) {year} {author}

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
''',
    },
    'bsd2': {
        'name': 'BSD 2-Clause "Simplified" License',
        'spdx': 'BSD-2-Clause',
        'osi': True,
        'copyleft': False,
        'text': '''BSD 2-Clause License

Copyright (c) {year}, {author}

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
''',
    },
    'isc': {
        'name': 'ISC License',
        'spdx': 'ISC',
        'osi': True,
        'copyleft': False,
        'text': '''ISC License

Copyright (c) {year}, {author}

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
''',
    },
    'unlicense': {
        'name': 'The Unlicense',
        'spdx': 'Unlicense',
        'osi': True,
        'copyleft': False,
        'text': '''This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
''',
    },
    'cc0': {
        'name': 'Creative Commons Zero v1.0 Universal',
        'spdx': 'CC0-1.0',
        'osi': False,
        'copyleft': False,
        'text': '''CC0 1.0 Universal

To the extent possible under law, {author} has waived all copyright and
related or neighboring rights to this work.

For more information, see <https://creativecommons.org/publicdomain/zero/1.0/>
''',
    },
}


def cmd_generate(args):
    key = args.license.lower()
    if key not in LICENSES:
        print(f'Unknown license: {key}. Use "list" to see available.', file=sys.stderr)
        sys.exit(1)
    
    lic = LICENSES[key]
    year = args.year or datetime.now().year
    author = args.author or 'Your Name'
    
    text = lic['text'].format(year=year, author=author)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(text)
        print(f'Written {lic["name"]} to {args.output}')
    else:
        print(text)


def cmd_list(args):
    print(f'{"Key":<12} {"Name":<42} {"SPDX":<15} {"OSI":>4} {"Copyleft":>8}')
    print('-' * 85)
    for key, lic in LICENSES.items():
        osi = '✓' if lic['osi'] else ''
        copyleft = '✓' if lic['copyleft'] else ''
        print(f'{key:<12} {lic["name"]:<42} {lic["spdx"]:<15} {osi:>4} {copyleft:>8}')


def cmd_info(args):
    key = args.license.lower()
    if key not in LICENSES:
        print(f'Unknown: {key}')
        sys.exit(1)
    lic = LICENSES[key]
    print(f'Name:     {lic["name"]}')
    print(f'SPDX:     {lic["spdx"]}')
    print(f'OSI:      {"Yes" if lic["osi"] else "No"}')
    print(f'Copyleft: {"Yes" if lic["copyleft"] else "No"}')


def main():
    p = argparse.ArgumentParser(description='Open source license generator')
    sub = p.add_subparsers(dest='cmd', required=True)

    for key in LICENSES:
        s = sub.add_parser(key, help=f'Generate {LICENSES[key]["name"]}')
        s.add_argument('--author', '-a', default='')
        s.add_argument('--year', '-y', type=int)
        s.add_argument('--output', '-o', default='LICENSE')
        s.set_defaults(func=cmd_generate, license=key)

    sub.add_parser('list', help='List available licenses').set_defaults(func=cmd_list)

    s = sub.add_parser('info', help='Show license details')
    s.add_argument('license')
    s.set_defaults(func=cmd_info)

    args = p.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
