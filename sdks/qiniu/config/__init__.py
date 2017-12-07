# coding: utf-8
import os

__all__ = ['QiniuConfig']

app_config_file_name = os.environ.get('QINIU_CONFIG', '')
if not app_config_file_name:
    raise Exception('No QINIU_CONFIG in os environ, should be something like: xxx_config')
app_config_module = __import__('config.{}'.format(app_config_file_name), fromlist=['Config'])

QiniuConfig = app_config_module.Config

# should set env: export QINIU_CONFIG=xxx_config
