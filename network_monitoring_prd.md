# Product Requirements Document (PRD)

---

## **Project Title:**

**Docker-Based Network Monitoring System**

---

## **1. Purpose and Objectives**

The purpose of this system is to monitor the network infrastructure at Merry Acres Inn, providing detailed metrics on device uptime, bandwidth utilization, error rates, and temperature while also enabling proactive alerts for critical thresholds.

**Objectives:**

- Centralize metrics from all network devices.
- Visualize data using Grafana dashboards.
- Send alerts for high usage, downtime, and packet drops.
- Maintain historical logs for 6 months for trend analysis.

---

## **2. Scope**

**Key Features:**

1. Monitor **routers**, **switches**, **access points**, **VoIP phones**, **streaming devices**, **computers**, and all SNMP-enabled devices.
2. Visualize:
   - Bandwidth utilization per VLAN and device.
   - Online/offline status of devices.
   - Guest network IP address utilization.
3. Alerts:
   - Bandwidth > 80% on guest network.
   - Packet drops exceeding thresholds.
   - Device disconnections or downtime.
4. Store data locally for 6 months using InfluxDB.
5. Enable real-time and historical dashboards via Grafana.
6. Provide a daily summary and weekly email reports.
7. Automate recovery of Docker containers if a service fails.

---

## **3. Users and Personas**

**Primary User:**  
Andy and his team, who will use the system to monitor the Merry Acres Inn's network infrastructure. They require:

- Easy-to-read dashboards.
- Alerts via Discord for real-time notifications.
- Simple maintenance and minimal manual intervention.

---

## **4. Functional Requirements**

1. **Data Collection:**

   - SNMP Exporter scrapes metrics from network devices using community strings.
   - Prometheus scrapes metrics from the SNMP Exporter.

2. **Metrics to Monitor:**

   - **Device Metrics:** CPU, memory, bandwidth, error rates, temperature.
   - **Events:** Device uptime/downtime, port/AP usage.
   - **Aggregated Metrics:** Total VLAN bandwidth, IP address utilization.

3. **Data Storage:**

   - Use InfluxDB with a retention period of 6 months.
   - Ensure a daily backup to an FTP server or Google Drive.

4. **Visualization:**

   - Grafana dashboards with panels for:
     - Bandwidth (current and historical).
     - Device status (online/offline).
     - Guest IP utilization.
   - Include drill-down capabilities for granular details.

5. **Alerts:**

   - Threshold-based alerts:
     - Bandwidth usage > 80%.
     - High packet drops.
   - Send real-time alerts to Discord and daily summaries.

6. **Recovery Logic:**

   - Automate Docker container restarts for `snmp_exporter`, `prometheus`, and `grafana`.
   - Check ISP uptime before restarting services.

7. **Data Export:**

   - Daily summary sent to Discord.
   - Weekly email reports with trends.

8. **Security:**
   - Encrypted credentials for SNMP devices.
   - Secure API tokens for InfluxDB and Prometheus.

---

## **5. Non-Functional Requirements**

- **Scalability:**  
  Capable of monitoring up to 100 devices without performance degradation.
- **Portability:**  
  Deployable as a Docker Compose stack on Windows 10/11 with Docker Desktop.
- **Resilience:**  
  Automatic recovery from service or network interruptions.
- **Retention:**  
  Logs and metrics retained for 6 months within 200 GB storage.

---

## **6. Technical Stack**

1. **Docker Services:**

   - `snmp_exporter`: Collect SNMP metrics.
   - `prometheus`: Scrape SNMP metrics and forward them to InfluxDB.
   - `influxdb`: Store metrics with a 6-month retention period.
   - `grafana`: Visualize metrics and configure alerts.

2. **Configuration Files:**

   - `snmp.yml`: Define SNMP targets and community strings.
   - `prometheus.yml`: Configure Prometheus scraping and remote write to InfluxDB.
   - `telegraf.conf` (if needed): Alternative forwarder for InfluxDB metrics.

3. **Endpoints:**
   - Grafana: [http://localhost:3000](http://localhost:3000)
   - Prometheus: [http://localhost:9090](http://localhost:9090)
   - InfluxDB: [http://localhost:8086](http://localhost:8086)
   - SNMP Exporter: [http://localhost:9116](http://localhost:9116)

---

## **7. Implementation Steps**

1. **Set Up Infrastructure:**

   - Create Docker Compose file to spin up services.
   - Configure SNMP Exporter, Prometheus, and InfluxDB.

2. **Integrate SNMP Devices:**

   - Add devices (router, switches, APs) to `snmp.yml`.

3. **Configure Alerts:**

   - Set thresholds for bandwidth, downtime, and packet loss.

4. **Build Dashboards:**

   - Create Grafana panels for key metrics.

5. **Testing:**

   - Verify data collection.
   - Test alerts for failure scenarios.

6. **Documentation:**
   - Provide setup instructions for future maintenance.

---

## **8. Potential Challenges**

1. **SNMP Access:**
   - Ensure all devices have SNMP enabled with correct community strings.
2. **Network Stability:**
   - Account for potential downtime in scraping schedules.
3. **Disk Usage:**
   - Monitor InfluxDB storage and configure automatic backups.

---

## **9. Timeline**

| **Task**                   | **Estimated Time** |
| -------------------------- | ------------------ |
| Docker environment setup   | 1 day              |
| Configure SNMP Exporter    | 1 day              |
| Prometheus integration     | 1 day              |
| Grafana dashboard creation | 2 days             |
| Alerts and notifications   | 1 day              |
| Testing and optimization   | 2 days             |

---
