from colorama import *

# paths
CONFIG_PATH = "/etc/wireguard/wg0.conf"
ASSOCIATION_CASH_PATH = "/usr/local/etc/wg-scripts/cache_associations"

# colors
colors = \
    [
        ('peer:', Fore.BLUE),
        ('interface:', Fore.GREEN),
        ('.+:', Style.BRIGHT),
    ]
