from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

def get_cache(name, data_folder):
	cache_opts = {
	    'cache.type': 'file',
	    'cache.data_dir': data_folder+'cache',
	    'cache.lock_dir': data_folder+'cache-lock'
	}

	cache_manager = CacheManager(**parse_cache_config_options(cache_opts))
	cache = cache_manager.get_cache(name, type='file', expire=30)
	return cache