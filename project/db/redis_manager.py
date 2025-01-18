# /project/db/redis_manager.py
import redis

# Connexion à Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def get_redis_session(session_id: str):
    return redis_client.get(session_id)  # Récupère une session par ID

def set_redis_session(session_id: str, data: dict):
    redis_client.set(session_id, data)  # Sauvegarde une session avec un ID
