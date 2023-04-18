from GenerateESI import GenerateAPI
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='EVECeleryCodegen',
        description='Generates EVECelery code from Swagger spec.',
        epilog='This is the command-line interface for generating EVECelery code from Swagger spec.')

    parser.add_argument('--local', dest='local', action='store_true', required=False,
                        help='Use the local swagger.json file instead of pulling the latest Swagger spec from ESI.')
    args = parser.parse_args()

    GenerateAPI.run(args.local)
