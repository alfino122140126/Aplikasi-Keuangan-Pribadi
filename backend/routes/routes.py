def includeme(config):
    config.add_route('get_transaksi', '/transaksi')
    config.add_route('post_transaksi', '/transaksi')
    
    config.add_route('get_utang', '/utang')
    config.add_route('post_utang', '/utang')
    
    config.add_route('get_pengingat', '/pengingat')
    config.add_route('post_pengingat', '/pengingat')