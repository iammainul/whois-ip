# whois-ip

whois-ip is a simple whois tool in python for whois lookup for IP Addresses. It takes advantage of the python ipwhois package.

The output is saved in a csv file named: "output.csv" 
The output currently only shows these following details:
- IP
- Name
- Country
- City
- Description

---

### Usages
```
python whosisip.py -i <single-ip>
python whosisip.py -l <ip-list.txt>
```

### Requirements
```
pip install IPWhois
```


### Modification
Will work on making it a multitrheaded program. Please feel free to contribute.