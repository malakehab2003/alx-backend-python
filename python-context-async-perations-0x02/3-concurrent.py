#!/usr/bin/python3
import asyncio
import aiosqlite

async def async_fetch_users():
  db = await aiosqlite.connect('users.db')
  cursor = await db.execute("SELECT * FROM users")
  result = await  cursor.fetchall()
  await db.close()
  return result

async def async_fetch_older_users():
  db = await aiosqlite.connect('users.db')
  cursor = await db.execute("SELECT * FROM users WHERE age > 40")
  result = await  cursor.fetchall()
  await db.close()
  return result


async def fetch_concurrently():
    all_users, older_users = await asyncio.gather(
        async_fetch_users(), 
        async_fetch_older_users()
    )
    
    print("All Users:")
    for user in all_users:
        print(user)
    
    print("\nUsers older than 40:")
    for user in older_users:
        print(user)

asyncio.run(fetch_concurrently())
