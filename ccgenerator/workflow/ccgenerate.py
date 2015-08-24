# encoding: utf-8

import sys
from workflow import Workflow
from random import randint
from random import choice
from re import findall


def main(wf):
    cardTypes = ["visa", "master", "amex", "diners", "jcb", "discover", "hiper"]
    le = len(wf.args)
    if not wf.args[0] in cardTypes:
        for ct in cardTypes:
            wf.add_item(title="ccg %s" % ct)
        wf.send_feedback()
        return 0

    cc = ""
    length = 0

    query = wf.args[0]

    if query == "visa":
        cc += "4"
        length = 16

    if query == "master":
        cc += str(randint(51,55))
        length = 16

    if query == "amex":
        cc += choice(["34", "37"])
        length = 15

    if query == "diners":
        cc += "54"
        length = 16

    if query == "jcb":
        cc += str(randint(3528, 3589))
        length = 16

    if query == "discover":
        cc += choice(["6011", str(randint(622126, 622925)), str(randint(644, 649)), "65"])
        length = 16

    if query == "hiper":
        cc += "384"
        length = 16

    while (len(cc) < length - 1):
        cc += str(randint(0,9))

    cc += str(luhn(cc))
    wf.add_item(title=cc,arg=cc,valid=True)
    # Send the results to Alfred as XML
    wf.send_feedback()
    return 0

def luhn(input):
    digits = [int(c) for c in input if c.isdigit()]
    digits.reverse()
    doubled = [2 * d for d in digits[0::2]]
    total = sum(d - 9 if d > 9 else d for d in doubled) + sum(digits[1::2])
    return (total * 9) % 10

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))