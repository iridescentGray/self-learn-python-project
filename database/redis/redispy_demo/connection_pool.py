import redis

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    print(r.set('foo', 'bar'))
    print(r.get('foo'))