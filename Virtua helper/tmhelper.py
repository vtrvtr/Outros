import logging
import argparse
from tinydb import TinyDB as tdb, where
from pprint import pprint

FORMATTER = """%(asctime)4s - %(levelname)-1s %(message)s"""

logging.basicConfig(
    filename='E:\Code\Outros\Virtua Helper\\tmhelper.log', level=logging.INFO, format=FORMATTER)

db = tdb("E:\\Code\Outros\Virtua helper\complain_db.json")


def add_complain():
    service = raw_input("Type the service\n")
    message = raw_input("Explain the problem\n")
    protocol = raw_input("Type the protocol\n")
    solution = raw_input("Explain the solution\n")
    formatted_protocol = ' '.join(
        [protocol[i:i + 3] for i in range(0, len(protocol), 3)])
    logging.info(
        'ADDED: \n Service: {} \n Info: {} \n Protocol: {} \n Solution: {}'.format(service, message, formatted_protocol, solution)) 
    db.insert({'service': service.lower(), 'protocol': protocol, 'message': message.lower(), 'solution': solution.lower()})


def search(query):
    category, query = query.split()
    if category == 'message':
        results = db.search(where(category.lower()) == query.lower())
    else:
        for result in results:
            print ' Service: {r[service]} \n Protocol: {r[protocol]} \n Message: {r[message]} \n Solution: {r[solution]}'.format(r=result)

if __name__ == '__main__':
    parse = argparse.ArgumentParser(
        description="Choose the option, search or add")
    parse.add_argument('-a', help="Adds a new complain", action="store_true")
    parse.add_argument('-s', help="Read and search log files")
    args = parse.parse_args()
    if args.a:
        add_complain()
    elif args.s:
        search = raw_input('Search what dude')


