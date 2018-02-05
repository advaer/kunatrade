BASE_API_URL = 'https://kuna.io'
PUBLIC_KEY = '...your public key...'
SECRET_KEY = '...your secret key...'
API_SPEC = {
    'timestamp': {
        'verb': 'GET',
        'path': '/api/v2/timestamp'
    },
    'tickers': {
        'verb': 'GET',
        'path': '/api/v2/tickers',
        'market_path': True
        # market
    },
    'candles': {
        'verb': 'GET',
        'path': '/api/v2/order_book'
        # market
    },
    'trades': {
        'verb': 'GET',
        'path': '/api/v2/trades',
        # market
    },
    'get_personal_info': {
        'verb': 'GET',
        'path': '/api/v2/members/me',
        'is_private': True,
    },
    'create_order': {
        'verb': 'POST',
        'path': '/api/v2/orders',
        # side
        # volume
        # market
        # price
    },
    'cancel_order': {
        'verb': 'POST',
        'path': '/api/v2/order/delete',
        # id
    },
    'active_orders': {
        'verb': 'GET',
        'path': '/api/v2/orders',
        'is_private': True,
        # market
    },
    'my_trades': {
        'verb': 'GET',
        'path': '/api/v2/trades/my',
        'is_private': True,
        # market
    },
}
