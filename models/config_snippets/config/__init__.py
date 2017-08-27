# coding: utf-8
import os

__all__ = ['CSConfig']

app_config_module_path = os.environ.get('CS_CONFIG', '')
if not app_config_module_path:
    raise Exception('No CS_CONFIG in os environ, should be something like: config_snippets.config.xxx_config')
app_config_module = __import__(app_config_module_path, fromlist=['Config'])

CSConfig = app_config_module.Config

# should export in shell: export CS_CONFIG=config.xxx_config
# in gitignore:
# #/models/config_snippets/config/*_config.py
# !/models/config_snippets/config/sample_config.py
