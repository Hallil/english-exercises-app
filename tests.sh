#!/usr/bin/env bash
python3 test_authentication.py | python3 test_views.py | python3 test_level_access.py | python3 test_db_layer.py | python3 test_login.py
