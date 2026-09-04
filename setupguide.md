# VAPIC Step-by-Step Setup Guide

## Step 1 — Prepare Router & Network
1. Connect TP-Link Wi-Fi router to wall outlet.
2. Connect PC1 through PC5 to router LAN Ethernet ports.
3. Connect Laptop via Wi-Fi or Ethernet.
4. Reserve static DHCP IP addresses in router admin (`192.168.50.10` to `.15`).

## Step 2 — Run Setup Batch Scripts
1. On PC1, run `PC1/setup.bat`.
2. On PC2, run `PC2/setup.bat`.
3. On PC3, run `PC3/setup.bat`.
4. On PC4, run `PC4/setup.bat`.
5. On PC5, run `PC5/setup.bat`.

## Step 3 — Verify Cluster & Access Dashboards
1. Open Admin Dashboard on Laptop: `http://192.168.50.11:8000/admin`
2. Open Supervisor Mobile Control on Supervisor Phone: `http://192.168.50.11:8000/supervisor`
3. Open Normal User Chat Interface on User Phone: `http://192.168.50.11:8000/`

## Step 4 — Run Test Suite
Run `test_cluster.bat` on PC1 to confirm all unit and integration tests pass.
