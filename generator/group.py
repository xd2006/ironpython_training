import os
import random
import re
import string
import getopt
import sys
import clr

clr.AddReferenceByName("Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c")

from Microsoft.Office.Interop import Excel

from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.xlsx"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    str = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return clear(str.strip())


def clear(s):
    return re.sub("\s+", " ", s)


testdata = [
    Group(name=random_string("testname", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

try:
    os.remove(file)
except OSError:
    pass

excel = Excel.ApplicationClass()
excel.Visible = True

workbook = excel.Workbooks.Add()
sheet = workbook.ActiveSheet

for i in range(len(testdata)):
    sheet.Range["A%s" % (i+1)].Value2 = testdata[i].name

workbook.SaveAs(file)

excel.Quit()