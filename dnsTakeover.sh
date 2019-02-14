#!/bin/bash
#title			:dnsTakeover.sh
#description	:Bash script to check a domain for subdomain takeover vulnerability
#author			:Jaroslaw Porzucek
#date			:20190214
#version		:1.0
#usage			:./dnsTakeover.sh example.com
#requirements	:Amass, MassDNS
#==============================================================================

# Let's colour
RED='\033[0;31m'
NC='\033[0m'
YEL='\033[1;33m'

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function join_by { local IFS="$1"; shift; echo "$*"; }

# Vulnerable domains that are checked
domains=(
	cloudapp.net
	azurewebsites.net
	s3.amazonaws.com
	cargocollective.com
	desk.com
	redirect.feedpress.me
	ghost.io
	github.com
	helpscoutdocs.com
	herokuapp.com
	herokuspace.com
	hs-sites.com
	myjetbrains.com
	myshopify.com
	statuspage.io
	surge.sh
	uservoice.com
	wordpress.com
	zendesk.com
)

domains="(`join_by '|' "${domains[@]}"`)"

# Check if site hosted on specific provider is vulnerable

function cloudapp {
	if ! host $2 > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function azurewebsites {
	if ! host $2 > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function amazonaws {
	if curl -sI $2 | grep "404 Not Found" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function cargocollective {
	if curl -sI https://$2 | grep "404 Not Found" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function desk {
	if curl -s https://$2 | grep "site_not_found" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function feedpress {
	if curl -s -H "Host: $1" redirect.feedpress.me | grep "The feed has not been found" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function ghost {
	if curl -sL -H "Host: $2" ghost.io | grep "404: Page Not Found" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function github {
	if curl -sL -H "Host: $2" github.com | grep "There isn't a GitHub Pages site here" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function helpscoutdocs {
	if curl -sL -H "Host: $2" helpscoutdocs.com | grep "Page Not Found" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function herokuapp {
	if curl -sL -H "Host: $2" herokuapp.com | grep "no-such-app" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function hs-sites {
	if curl -sL -H "Host: $2" hs-sites.com | grep "No portal was specified for this request" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function myjetbrains {
	if curl -sL -H "Host: $2" $2 | grep "is not a registered InCloud YouTrack" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function myshopify {
	if curl -sL -H "Host: $2" myshopify.com | grep "Sorry, this shop is currently unavailable" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function statuspage {
	if curl -sL -H "Host: $2" $2 | grep "Hosted Status Pages for Your Company" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function surge {
	if curl -sL -H "Host: $2" surge.sh | grep "project not found" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function uservoice {
	if curl -sL -H "Host: $2" uservoice.com | grep "This UserVoice instance does not exist" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function wordpress {
	if curl -sL -H "Host: $2" wordpress.com | grep "doesn&#8217;t&nbsp;exist" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function zendesk {
	if curl -sL -H "Host: $2" zendesk.com | grep "Oops, this help center no longer exists" > /dev/null; then
		echo -e "${RED}Possible takeover: $1"
	fi
}

function ctrl_c() {
	rm $tmpFile1 $tmpFile2
	exit
}


echo -e "${YEL}[Running Amass...]"
tmpFile1=`pwgen 20 1`.txt
amass -passive -d $1 -o $tmpFile1

echo -e "${YEL}[Running MassDNS...]"
tmpFile2=`pwgen 20 1`.txt
massdns -q -l amass_err.log -r \/root\/Bugbounty\/_tools\/massdns\/lists\/resolvers.txt -t A $tmpFile1 -o S -w $tmpFile2

grep -E $domains $tmpFile2 > dnsTakeover.out
tmpFile3=`pwgen 20 1`.txt
grep -v $domains $tmpFile2 | cut -d" " -f3 > $tmpFile3 


echo -e "${YEL}[Checking cloud providers...]"
while read -r IN; do
	arrIN=(${IN//CNAME/ })
	
	provider=${arrIN[1]}
	provider=(${provider//./ })
	provider=${provider[-2]}

	website=${arrIN[0]::-1}
	cname=${arrIN[1]::-1}

	echo -e "${YEL}Checking $cname..."
	$provider $website $cname
done < dnsTakeover.out

# Cleaning up...
rm $tmpFile1
rm $tmpFile2
rm $tmpFile3
