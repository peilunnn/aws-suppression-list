https://docs.aws.amazon.com/ses/latest/dg/sending-email-suppression-list.html

From CLI,
1. If you haven't enabled the Amazon SES account-level suppression list, do so by running:
```
aws sesv2 put-account-suppression-attributes \
--suppressed-reasons BOUNCE COMPLAINT
```

2. Pipe your entire suppression list into a JSON file by running:
```
until aws sesv2 list-suppressed-destinations --output text | grep -m 1 "NextToken" 
  do aws sesv2 list-suppressed-destinations --output text >> supp_list.json && sleep 2 
  done
```

3. Do the extraction by running ```python3 extract.py```

4. Inspect the emails.csv file generated