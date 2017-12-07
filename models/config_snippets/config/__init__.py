# coding: utf-8
import os

__all__ = ['CSConfig']

app_config_file_name = os.environ.get('CS_CONFIG', '')
if not app_config_file_name:
    raise Exception('No CS_CONFIG in os environ, should be something like: xxx_config')
app_config_module = __import__('config.{}'.format(app_config_file_name), fromlist=['Config'])

CSConfig = app_config_module.Config

# should set env: export CS_CONFIG=xxx_config
# in gitignore:
# #/models/config_snippets/config/*_config.py
# !/models/config_snippets/config/sample_config.py
