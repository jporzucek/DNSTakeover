#!/usr/bin/python3
import subprocess
import dns.resolver
import requests
import sys

# Disable 'Unverified HTTPS request' warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

### Let's make color!
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

### Cloud Provider Checking Functions ###

def cloudapp(primaryName, cname):
    try:
        dns.resolver.query(cname)
    except:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def azurewebsites(primaryName, cname):
    try:
        dns.resolver.query(cname)
    except:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def amazonaws(primaryName, cname):
    r = requests.get('https://{}'.format(cname), verify=False)
    if '404 Not Found' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def cargocollective(primaryName, cname):
    r = requests.get('https://{}'.format(cname), verify=False)
    if '404 Not Found' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def desk(primaryName, cname):
    r = requests.get('https://{}'.format(cname), verify=False)
    if 'site_not_found' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def feedpress(primaryName, cname):
    r = requests.get('https://redirect.feedpress.me', headers={'Host': cname }, verify=False)
    if 'The feed has not been found' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)
    
def ghost(primaryName, cname):
    r = requests.get('https://ghost.io', headers={'Host': cname }, verify=False)
    if '404: Page Not Found' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def github(primaryName, cname):
    r = requests.get('https://github.com', headers={'Host': cname }, verify=False)
    if 'There isn\'t a GitHub Pages site here' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def helpscoutdocs(primaryName, cname):
    r = requests.get('https://helpscoutdocs.com', headers={'Host': cname }, verify=False)
    if 'Page Not Found' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def heroku(primaryName, cname):
    r = requests.get('https://herokuapp.com', headers={'Host': cname }, verify=False)
    if 'no-such-app' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def hssites(primaryName, cname):
    r = requests.get('https://hs-sites.com', headers={'Host': cname }, verify=False)
    if 'No portal was specified for this request' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def jetbrains(primaryName, cname):
    r = requests.get('https://{}'.format(cname), headers={'Host': cname }, verify=False)
    if 'is not a registered InCloud YouTrack' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def shopify(primaryName, cname):
    r = requests.get('https://myshopify.com', headers={'Host': cname }, verify=False)
    if 'Sorry, this shop is currently unavailable' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def statuspage(primaryName, cname):
    r = requests.get('https://{}'.format(cname), headers={'Host': cname }, verify=False)
    if 'Hosted Status Pages for Your Company' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def surge(primaryName, cname):
    r = requests.get('https://surge.sh', headers={'Host': cname }, verify=False)
    if 'project not found' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def uservoice(primaryName, cname):
    r = requests.get('https://uservoice.com', headers={'Host': cname }, verify=False)
    if 'This UserVoice instance does not exist' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def wordpress(primaryName, cname):
    r = requests.get('https://wordpress.com', headers={'Host': cname }, verify=False)
    if 'doesn&#8217;t&nbsp;exist' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)

def zendesk(primaryName, cname):
    r = requests.get('https://zendesk.com', headers={'Host': cname }, verify=False)
    if 'Oops, this help center no longer exists' in r.text:
        print(bcolors.FAIL + "Possble takeover of {} with CNAME {}".format(primaryName, cname) + bcolors.ENDC)


# Domains list
domains= {
	cloudapp : 'cloudapp.net',
	azurewebsites : 'azurewebsites.net',
	amazonaws : 's3.amazonaws.com',
	cargocollective : 'cargocollective.com',
	desk : 'desk.com',
	feedpress : 'redirect.feedpress.me',
	ghost : 'ghost.io',
	github : 'github.com',
	helpscoutdocs : 'helpscoutdocs.com',
	heroku : 'herokuapp.com',
	heroku : 'herokuspace.com',
	hssites : 'hs-sites.com',
	jetbrains : 'myjetbrains.com',
	shopify : 'myshopify.com',
	statuspage : 'statuspage.io',
	surge : 'surge.sh',
	uservoice : 'uservoice.com',
	wordpress : 'wordpress.com',
	zendesk : 'zendesk.com'
}

if len(sys.argv) != 2:
    print('Usage: python3 dnsTakeover.py <targetDomain>')
    sys.exit()

domainName = sys.argv[1]
print(bcolors.OKGREEN + "--- Checking {} for Subdomain Takeover ---".format(domainName) + bcolors.ENDC)


# Running Amass
print(bcolors.OKBLUE + "[Running Amass...]" + bcolors.ENDC)
subprocess.run(['amass', '-passive', '-d', domainName, '-o', 'tmp/amass.out'], stdout=subprocess.PIPE)

amassResults = ''
with open('tmp/amass.out', 'r') as f:
    amassResults = f.read().splitlines()

# Running MassDNS
print(bcolors.OKBLUE + "[Running MassDNS...]" + bcolors.ENDC)
massDnsResults = subprocess.run(['massdns', '-q', '-r', '/root/Bugbounty/_tools/massdns/lists/resolvers.txt', '-t', 'CNAME', 'tmp/amass.out', '-o', 'S'], stdout=subprocess.PIPE)
massDnsResults = massDnsResults.stdout.decode('utf-8').split('\n')[:-1]


massDnsDict = {}

for record in massDnsResults:   
    record = record.split()
    name = record[0]
    cname = record[2]
    primaryName = name
    
    isCloud = False
    while not isCloud:
        for name, domain in domains.items():
            if domain in cname:
                massDnsDict[primaryName] = (name, cname)
                isCloud = True
                break
        if not isCloud:
            try:
                newCname = dns.resolver.query(cname, 'CNAME')
                cname = newCname[0].to_text()
                name = cname
            except:
                break

print(bcolors.OKBLUE + "[Checking Cloud Providers...]" + bcolors.ENDC)

for k,v in massDnsDict.items():
    print(bcolors.WARNING + "Checking {}..".format(v[1]) + bcolors.ENDC)
    primaryName = k
    domain = v[0]
    cname = v[1]
    domain(primaryName, cname)