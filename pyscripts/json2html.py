# -*- coding: utf-8 -*-

import json
import sys

"""python解析json文件:
https://blog.csdn.net/u010895119/article/details/77377413"""

def wrapDiv(string):
    return """<div id="ordersuitetable">
        {}
        </div>""".format(string)

def wrapTable(string):
    return """<table class="testTable">
        {}
        </table>""".format(string)

def writeTableTr(testnumber, testcase, cmd, description, passed):
    return """<tr>
            <td>{no}</td>
            <td>{case}</td>
            <td>{cmd}</td>
            <td>{desc}</td>
            <td style="color: {color}">{passed}</td>
            </tr>""".format(no=testnumber, case=testcase, cmd=cmd, desc=description, color="green" if passed=="passed" else "red", passed=passed)

def writeTabHeader():
    return """<tr>
            <th style="width: 3%">Test Number</th>
            <th style="width: 8%">Test Case</th>
            <th style="width: 3%">Number of Checks</th>
            <th style="width: 10%">Description</th>
            <th style="width: 3%">Pass</th>
            </tr>"""

def writeTabTitle(title):
    return """<p class="tabletitle">{}</p>""".format(title)

def writeSummary(text):
    return """<p class="summary">{}</p>""".format(text)

def writeHtmlHeader():
    return """
    <head>
    <style type="text/css">
    .testTable { 
        border-collapse:collapse;
        color:#000;
        font-size:18px; 
        }
    .testTable td, .testTable th { 
        padding:5px;
        border:1px solid rgb(188, 188, 188);
        text-align: center; 
        vertical-align: middle; 
        }
    .testTable td { 
        font-family:Georgia, Garamond, serif; 
        }
    .tabletitle{
        font: bold 24px/1 arial, sans-serif;
        text-align: left; 
        margin-bottom: 9px;
        margin-top: 30px;
    }
    .summary{
        font: normal 20px/1 "Times New Roman", Times, serif;
        text-align: left; 
        margin-bottom: 3px;
        margin-top: 30px;
        margin-left: 30px;
    }
    div#ordersuitetable {
        width: 70%;
        padding-top: 1%;
        margin-left: 30px;
        }
    </style>
    </head>
    """

if __name__=="__main__":
    jsonpath = sys.argv[1]
    with open(jsonpath, "r") as jsfile:
        joutput = json.load(jsfile)
    assert joutput is not None
    title = joutput["name"]
    status = joutput["status"]
    suites = joutput["entries"][0]["entries"]
    contents = ""
    numpass = 0
    numfail = 0

    for suite in suites:
        suitename = suite["name"]
        testcases = suite["entries"]
        number = 1
        table = writeTabHeader()
        for case in testcases:
            casenumber = number
            number += 1
            casename = case["name"]
            casedesp = case["description"]
            casepass = case["status"]
            entries = case["entries"]
            caseexec = len(entries)
            table += writeTableTr(casenumber, casename, caseexec, casedesp, casepass)
            if casepass == "passed":
                numpass += 1
            elif casepass == "failed":
                numfail += 1
        div = wrapDiv(wrapTable(writeTabTitle("Test Suite: {}".format(suitename)) + table))
        contents += div

    summary = writeSummary("Total Cases: {} <br>Passed Cases: {} <br> Failed Cases: {}".format(numpass+numfail, numpass, numfail))
    bodytitle = writeSummary(title)
    notes = writeSummary("Notes: check the attached pdf file for details.")
    contents += notes
    html = "<html>{}<body>{}\n{}\n</body>\n</html>".format(writeHtmlHeader(), bodytitle + summary, contents)
    with open("mailcontent.html", "w") as wfile:
        wfile.write(html)
        print html
