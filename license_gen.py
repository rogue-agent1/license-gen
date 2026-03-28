#!/usr/bin/env python3
"""license_gen - Generate common open source licenses."""
import sys
from datetime import datetime
LICENSES={
"mit":"""MIT License\n\nCopyright (c) {year} {author}\n\nPermission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.""",
"apache":"""Apache License\nVersion 2.0, January 2004\n\nCopyright {year} {author}\n\nLicensed under the Apache License, Version 2.0.""",
"gpl3":"""GNU GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007\n\nCopyright (C) {year} {author}\n\nThis program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License.""",
"bsd2":"""BSD 2-Clause License\n\nCopyright (c) {year}, {author}\nAll rights reserved.\n\nRedistribution and use in source and binary forms, with or without
modification, are permitted.""",
"unlicense":"""This is free and unencumbered software released into the public domain.\n\nAnyone is free to copy, modify, publish, use, compile, sell, or
distribute this software.""",
}
if __name__=="__main__":
    if len(sys.argv)<2:print("Available: "+", ".join(sorted(LICENSES.keys())));sys.exit(1)
    lic=sys.argv[1].lower();author=sys.argv[2] if len(sys.argv)>2 else"Author"
    year=datetime.now().year
    if lic in LICENSES:print(LICENSES[lic].format(year=year,author=author))
    else:print(f"Unknown license: {lic}")
