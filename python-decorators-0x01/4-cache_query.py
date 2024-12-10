#!/usr/bin/python3
import time
import sqlite3 
import functools


query_cache = {}

def with_db_connection(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        result = func(conn, *args, **kwargs)
        conn.close()
        return result
    return wrapper

def cache_query(func):
    def wrapper(*args, **kwargs):
        query = args[1] if len(args) > 1 else kwargs['query']
        if query in query_cache.keys():
            print('Get result from cache')
            return query_cache[query]
        else:
            print('Execute the command')
            result = func(*args, **kwargs)
            query_cache[query] = result
            return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")