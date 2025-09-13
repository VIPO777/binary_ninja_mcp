from importlib import import_module

_plugin_mod = None
try:
    _plugin_mod = import_module('.plugin', __name__)
except Exception:
    try:
        _plugin_mod = import_module('fosdickio_binary_ninja_mcp.plugin')
    except Exception:
        from . import plugin as _plugin_mod


BinaryNinjaMCP = getattr(_plugin_mod, 'BinaryNinjaMCP') 
plugin = getattr(_plugin_mod, 'plugin', None)

__all__ = ["BinaryNinjaMCP", "plugin"]
