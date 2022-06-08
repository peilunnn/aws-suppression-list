import csv
import json
from typing import List

from constants import EMAIL_ADDRESS, EMAILS, SUPP_LIST


def extract_emails() -> List[str]:
    res = []
    with open(SUPP_LIST) as json_file:
        emails = json.load(json_file)
        for _, summaries in emails.items():
            for summary in summaries:
                res.append(summary[EMAIL_ADDRESS])
    return res

def save_emails() -> None:
    with open(EMAILS, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(extract_emails())

if __name__ == "__main__":
    save_emails()
