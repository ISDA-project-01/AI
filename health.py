import time
import os
import requests
from logger import logger

nodes_status = {}

def update_node_heartbeat(node_id, info):
    info["last_seen"] = time.time()
    info["status"] = "ONLINE"
    nodes_status[node_id] = info
    logger.info(f"Heartbeat received from {node_id}")

def get_cluster_health(timeout=15):
    now = time.time()
    health_report = {}
    for node_id, data in nodes_status.items():
        is_healthy = (now - data.get("last_seen", 0)) < timeout
        status = "ONLINE" if is_healthy else "UNHEALTHY"
        health_report[node_id] = {
            **data,
            "status": status,
            "seconds_since_heartbeat": round(now - data.get("last_seen", 0), 2)
        }
    return health_report

def check_remote_node(ip, port):
    url = f"http://{ip}:{port}/health"
    try:
        resp = requests.get(url, timeout=3)
        if resp.status_code == 200:
            return resp.json()
    except Exception as e:
        logger.warning(f"Failed to reach node at {ip}:{port} - {str(e)}")
    return None
