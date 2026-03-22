# RoadMap

Fleet monitoring dashboards. See every node, every service, every metric from one screen.

Built on Grafana, customized for mixed fleets of Raspberry Pis and cloud servers.

## What It Monitors

| Metric | Description |
|--------|-------------|
| **CPU temperature** | Per-node thermal readings with alert thresholds |
| **RAM usage** | Memory and swap consumption |
| **Disk I/O** | Storage capacity, read/write rates |
| **Network** | Bandwidth, latency, packet loss between nodes |
| **Agent status** | Which AI agents are running and where |
| **Service health** | Up/down for every service on every node |
| **AI metrics** | Inference latency, model load times, accelerator utilization |

## Fleet

Tracks 7 nodes:
- 5 Raspberry Pi devices (ARM, 2-8GB RAM)
- 2 cloud servers (x86)

Each node runs a lightweight collector. Dashboards update in real time.

## Dashboards

- **Fleet Overview** — all nodes at a glance, color-coded health
- **Node Detail** — deep dive into one device
- **Agent Status** — AI agent activity and health
- **Network Map** — connectivity between nodes
- **Alerts** — active warnings and history

## What Changed From Upstream Grafana

- Pre-built dashboards tuned for Pi hardware (2GB RAM thresholds, thermal limits)
- BlackRoad theme (hot pink #FF1D6C)
- Service discovery for Ollama, NATS, MinIO, Qdrant, Redis, PostgreSQL
- Alert defaults for ARM devices running at the edge

## Setup

```bash
./install.sh
docker-compose up -d
# Access at http://localhost:3000
```

## Stack

- **Base**: Grafana (forked)
- **Data**: Prometheus + node_exporter
- **Dashboards**: Pre-configured fleet panels
- **Alerts**: Threshold-based with escalation

## License

Proprietary. Copyright (c) 2024-2026 BlackRoad OS, Inc. All rights reserved.
Upstream Grafana is AGPL v3. All BlackRoad modifications are proprietary.

---

*Remember the Road. Pave Tomorrow.*
