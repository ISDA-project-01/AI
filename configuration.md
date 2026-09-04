# VAPIC System Configuration Guide

## Architecture Overview
VAPIC (VishalAI Parallel Intelligence Cluster) is designed for 5 CPU-only Windows PCs with 8 GB RAM each, plus 1 Manager Laptop and mobile devices connected via a TP-Link private LAN router.

## Network Addressing & Static Lease Allocations
- Router IP: `192.168.50.1`
- Laptop (Admin Console): `192.168.50.10`
- PC1 (Master Gateway & Gemma Synthesis): `192.168.50.11`
- PC2 (Peer AI Node 1 - Qwen): `192.168.50.12`
- PC3 (Peer AI Node 2 - Gemma): `192.168.50.13`
- PC4 (Peer AI Node 3 - Llama): `192.168.50.14`
- PC5 (Peer AI Node 4 - DeepSeek): `192.168.50.15`

## DNS & Private Domain
- Internal Domain: `vapic.local`
- Configure router local DNS hostnames mapping `vapic.local` to PC1 (`192.168.50.11`).

## Environment Variables
Configured via `.env` or system environment variables:
- `VAPIC_SECRET_KEY`: Secret token key
- `VAPIC_ADMIN_USERNAME`: Administrator account name (Default: `admin`)
- `VAPIC_ADMIN_PASSWORD`: Administrator password
- `VAPIC_SUPERVISOR_USERNAME`: Mobile supervisor account name (Default: `supervisor`)
- `VAPIC_SUPERVISOR_PASSWORD`: Mobile supervisor password
