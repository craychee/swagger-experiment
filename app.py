#!/usr/bin/env python3

import connexion

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.json', arguments={'title': ''})
    app.run(server='tornado', port=8080)
