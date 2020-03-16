from ipwhois import IPWhois
import csv
import sys


#Usages
if len(sys.argv)!= 3:
	print ("usages:")
	print ("python whosisip.py -i <single-ip>")
	print ("python whosisip.py -l <list-of-ip>")
	sys.exit(1)

#Output File
outfile = csv.writer(open("output.csv", "wb"))
outfile.writerow(['IP', 'Name', 'Country', 'City', 'Description'])

#Single IP
if (sys.argv[1] == '-i'):
	ip = sys.argv[2]
	obj = IPWhois(ip)
	out = obj.lookup_whois()
	print (out)
#Multiple IP
elif (sys.argv[1] == '-l'):
	fp = sys.argv[2]
	ip_list = open(fp, "r")
	for ip in ip_list:
		ip = ip.strip('\n') #Removing any new line character from the end of line
		ip = ip.strip('\r')
		obj = IPWhois(ip)
		out = obj.lookup_whois()

		#writing the output into a csv-file
		ip = bytes(ip)
		name = out["nets"][0]['name']
		name = bytes(name)
		country = out["nets"][0]['country']
		country = bytes(country)
		city = out["nets"][0]['city']
		city = bytes(city)
		description = out["nets"][0]['description']
		description = bytes(description)

		outfile.writerow([ip, name, country, city, description]) 

print ("Done!")
