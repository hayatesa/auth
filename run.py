#!/usr/bin/env python
# -*- coding: utf-8 -*-
from auth_app import app


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True, use_reloader=False)
