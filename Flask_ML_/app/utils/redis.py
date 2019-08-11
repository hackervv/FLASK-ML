from flask import current_app
import redis

class Redis(object):
    '''
    redis操作工具类
    created by: Exception
    created date: 2019-08-08
    '''
    @staticmethod
    def _get_r():
        host = current_app.config['REDIS_HOST']
        port = current_app.config['REDIS_PORT']
        db = current_app.config['REDIS_DB']
        r = redis.StrictRedis(host,port,db)
        return r

    @classmethod
    def write(cls, key, value, expire=None):
        '''
        写入键值对
        '''
        if expire:
            expire_in_second = expire
        else:
            expire_in_second = current_app.config['REDIS_EXPIRE']
        r = cls._get_r()
        r.set(key, value, ex=expire_in_second)

    @classmethod
    def read(cls, key):
        '''
        读取键值对
        '''
        r = cls._get_r()
        value = r.get(key)
        #return value.decode('utf-8') if value else value
        return value

    @classmethod
    def hset(cls, name, key, value):
        '''
        写入hash表
        '''
        r = cls._get_r()
        r.hset(name, key, value)

    @classmethod
    def hmset(cls, key, *value):
        '''
        写入指定hash表指定的key
        '''
        r = cls._get_r()
        r.hmset(key, *value)

    @classmethod
    def hset(cls, key):
        '''
        读取指定hash表的键值
        '''
        r = cls._get_r()
        value = r.hget(key)
        return value

    @classmethod
    def hgetall(cls, name):
        '''
        获取指定hash的所有键值对
        '''
        r = cls._get_r()
        return r.hgetall(name)

    @classmethod
    def delete(cls, *names):
        '''
        删除一个或者多个键值
        '''
        r = cls._get_r()
        r.delete(*names)

    @classmethod
    def hdel(cls, name, *keys):
        '''
        删除指定hash的一个或者多个键值
        '''
        r = cls._get_r()
        r.hdel(name, *keys)

    @classmethod
    def expire(cls, name, expire=None):
        '''
        设置缓存过期时间
        '''
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = current_app.config['REDIS_EXPIRE']
        r = cls._get_r()
        r.expire(name, expire_in_seconds)




