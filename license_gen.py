#!/usr/bin/env python3
"""License generator — MIT, Apache-2.0, GPL-3.0, BSD-2."""
import sys
from datetime import date
MIT="""MIT License\n\nCopyright (c) {year} {name}\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED."""
BSD="""BSD 2-Clause License\n\nCopyright (c) {year}, {name}\nAll rights reserved.\n\nRedistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:\n\n1. Redistributions of source code must retain the above copyright notice.\n2. Redistributions in binary form must reproduce the above copyright notice."""
def cli():
    if len(sys.argv)<2: print("Usage: license_gen mit|bsd|apache|gpl [name]"); sys.exit(1)
    name=sys.argv[2] if len(sys.argv)>2 else "Author"; year=date.today().year
    t=sys.argv[1].lower()
    if t=="mit": print(MIT.format(year=year,name=name))
    elif t=="bsd": print(BSD.format(year=year,name=name))
    else: print(f"# {t.upper()} License\n\nCopyright (c) {year} {name}")
if __name__=="__main__": cli()
