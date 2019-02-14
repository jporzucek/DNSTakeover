# dnsTakeover
## About
Simple but effective bash script to check a domain if it's vulnerable to subdomain takeover. It uses [Amass](https://github.com/OWASP/Amass) and [MassDNS](https://github.com/blechschmidt/massdns) tools for fast domain information gathering and records resolution. List of supported cloud providers vulnerable to takeover*:
	
* cloudapp.net
* azurewebsites.net
* s3.amazonaws.com
* cargocollective.com
* desk.com
* redirect.feedpress.me
* ghost.io
* github.com
* helpscoutdocs.com
* herokuapp.com
* herokuspace.com
* hs-sites.com
* myjetbrains.com
* myshopify.com
* statuspage.io
* surge.sh
* uservoice.com
* wordpress.com
* zendesk.com

*List may be not 100% accurate and needs a review.

## Usage
*./dnsTakeover.sh example.com*
