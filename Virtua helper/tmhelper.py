import logging

FORMATTER = """%(asctime)4s - %(levelname)-1s %(message)s"""

logging.basicConfig(
    filename='E:\Code\Outros\Virtua Helper\\tmhelper.log', level=logging.INFO, format = FORMATTER) 

def main():
    service = raw_input("Type the service\n")
    message = raw_input("Explain the problem\n")
    protocol = raw_input("Type the protocol\n")
    solution = raw_input("Explain the solution\n")
    formatted_protocol = ' '.join(
        [protocol[i:i + 3] for i in range(0, len(protocol), 3)])
    logging.info(
        '\n Service: {} \n Info: {} \n Protocol: {} \n Solution: {}'.format(service, message, formatted_protocol, solution))

if __name__ == '__main__':
    main()