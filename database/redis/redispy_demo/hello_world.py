import redis

if __name__ == "__main__":
    # know more about redis connection: https://redis.readthedocs.io/en/stable/examples/connection_examples.html
    r = redis.Redis(host="localhost", port=6379, db=0)
    # all available command:https://redis.readthedocs.io/en/stable/commands.html
    print(r.set("foo", "bar"))
    print(r.get("foo"))
