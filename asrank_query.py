import re
import argparse
import sys
import json
import requests

URL = "https://api.asrank.caida.org/v2/graphql"
decoder = json.JSONDecoder()
encoder = json.JSONEncoder()

#method to print how to run script
def print_help():
    print (sys.argv[0],"-u as-rank.caida.org/api/v1")
    
######################################################################
## Parameters
######################################################################
parser = argparse.ArgumentParser()
parser.add_argument("asn",type=int,help="ASN we are looking up")
args = parser.parse_args()

######################################################################
## Main code
######################################################################
def main():
    if args.asn is None:
        parser.print_help()
        sys.exit()
    query = AsnQuery(args.asn)
    request = requests.post(URL,json={'query':query})
    if request.status_code == 200:
        print (request.json());
    else:
        print ("Query failed to run returned code of %d " % (request.status_code))

######################################################################
## Queries
######################################################################

def AsnQuery(asn): 
    return '''{
        asn(asn:"%i") {
            asn
            asnName
            rank
            organization {
                orgId
                orgName
            }
            cliqueMember
            seen
            longitude
            latitude
            cone {
                numberAsns
                numberPrefixes
                numberAddresses
            }
            country {
                iso
                name
            }
            asnDegree {
                provider
                peer
                customer
                total
                transit
                sibling
            }
            announcing {
                numberPrefixes
                numberAddresses
            }
        }
    } '''% (asn)
#run the main method
main()