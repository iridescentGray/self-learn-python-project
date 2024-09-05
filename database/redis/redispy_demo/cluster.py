from redis.cluster import ClusterNode
from redis.cluster import RedisCluster as Redis

CACHE_REDIS = [
    {"host": "10.150.30.214", "port": 6383},
    {"host": "10.150.30.215", "port": 6383},
    {"host": "10.150.30.216", "port": 6383},
    {"host": "10.150.30.217", "port": 6383},
    {"host": "10.150.30.218", "port": 6383},
    {"host": "10.150.30.219", "port": 6383},
]
if __name__ == "__main__":
    startup_nodes = [ClusterNode(node["host"], node["port"]) for node in CACHE_REDIS]
    r = Redis(startup_nodes=startup_nodes, password="")
    print(r.set("foo", "bar"))
    print(r.get("foo"))
    print(r.delete("foo"))
