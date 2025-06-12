import importlib
import os

class PluginManager:
    def __init__(self, plugins_folder='orion/plugins'):
        self.plugins_folder = plugins_folder
        self.plugins = {}

    def load_plugin(self, name):
        module_path = f'orion.plugins.{name}'
        module = importlib.import_module(module_path)
        self.plugins[name] = module
        return module

    def unload_plugin(self, name):
        if name in self.plugins:
            del self.plugins[name]

    def list_plugins(self):
        return os.listdir(self.plugins_folder)
