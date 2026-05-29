# M300 Dokumentation

## Projektkonzept – Kubernetes-Cluster mit CI/CD auf AWS

**Modul:** Cloud & Infrastruktur (V2)
**Autor:** Nevio
**Datum:** Mai 2026

---

### 1. Projektbeschreibung

Ziel dieses Projekts ist der Aufbau eines produktionsnahen Kubernetes-Clusters auf AWS EC2 mit RKE2, inklusive automatisierter Deployment-Pipeline (CI/CD via GitHub Actions), Monitoring-Stack sowie mehreren deployte Applikationen in getrennten Namespaces.

Die gesamte Infrastruktur wird mittels **Terraform** provisioniert. Änderungen an Applikationen werden automatisch über **GitHub Actions** auf den Cluster deployed.

---

### 2. Technologien & Tools

| Bereich                       | Technologie                      |
| ----------------------------- | -------------------------------- |
| Cloud-Plattform               | AWS (EC2, VPC, EBS, ALB)         |
| Infrastruktur-Provisionierung | Terraform                        |
| Kubernetes-Distribution       | RKE2 (Multi-Node)                |
| CI/CD                         | GitHub Actions                   |
| Container Registry            | GitHub Container Registry (GHCR) |
| Ingress                       | Nginx Ingress Controller         |
| Monitoring                    | Prometheus + Grafana             |
| Secrets-Management            | Kubernetes Secrets               |
| Versionskontrolle             | GitHub                           |

---

### 3. Architektur

#### 3.1 Cluster-Aufbau

- **1x Master-Node** (t3.medium) – RKE2 Control Plane
- **2x Worker-Node** (t3.medium) – Workload-Ausführung
- Alle Nodes in einer AWS VPC mit privaten/öffentlichen Subnetzen
- Load Balancer (ALB) für externen Zugriff

#### 3.2 Applikationen

| App        | Typ                     | Namespace     | Beschreibung                               |
| ---------- | ----------------------- | ------------- | ------------------------------------------ |
| Demo-App   | Eigene Python Flask App | `app-demo`    | Zeigt Versionsnummer, CI/CD Rolling Update |
| Podinfo    | Open Source             | `app-podinfo` | Visualisiert Cluster-Infos, schönes UI     |
| Monitoring | Prometheus + Grafana    | `monitoring`  | Überwachung des gesamten Clusters          |

Jede Applikation läuft in einem **eigenen Namespace** und ist über eine eigene Route via Nginx Ingress erreichbar.

#### 3.3 CI/CD-Pipeline (GitHub Actions)

```
Code Push → GitHub Actions → Docker Image Build → Push zu GHCR → kubectl apply auf RKE2-Cluster → Rolling Update
```

---

### 4. Anforderungen

#### 4.1 Funktionale Anforderungen

- RKE2 Multi-Node Cluster läuft stabil auf AWS EC2
- Alle drei Applikationen sind extern erreichbar (via Ingress)
- CI/CD-Pipeline deployed automatisch bei Push auf `main`-Branch
- Rolling Updates funktionieren ohne Downtime
- Monitoring zeigt Cluster-Metriken in Grafana Dashboard

#### 4.2 Nicht-funktionale Anforderungen

- **Sicherheit:** Secrets werden nicht im Code gespeichert (Kubernetes Secrets / GitHub Secrets)
- **Kosten:** AWS-Budget unter 50 USD gehalten
- **Skalierbarkeit:** Architektur erlaubt späteres Hinzufügen von Worker-Nodes
- **Nachvollziehbarkeit:** Alle Konfigurationen sind versioniert in GitHub

---

### 5. Bezug zur Kompetenzmatrix

| Kriterium                                                   | Umsetzung im Projekt                                                                                                                                        |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A1** – Ermittlung erforderlicher Services                 | Bedarfserhebung: EC2, VPC, RKE2, Ingress, Monitoring, CI/CD. Begründung warum welcher Service gewählt wird.                                                 |
| **B1** – Entwicklung eines Integrationskonzepts             | Architekturplanung: Netzwerkdesign (VPC, Subnetze, Security Groups), Tool-Auswahl (Terraform, RKE2, GitHub Actions), Testfälle für Pipeline und Deployments |
| **C1** – Konfiguration, Funktionsprüfung und Monitoring     | Konfigurationsmanagement via Terraform & Kubernetes Manifests, Secrets-Verwaltung, Performance-Optimierung der Nodes                                        |
| **D1** – Netzwerkverbindungen konfigurieren und testen      | VPC, Subnetze, Security Groups, Ingress-Routing konfigurieren und Konnektivität dokumentiert testen                                                         |
| **E1** – Integration verschiedener Services und Plattformen | Mehrere Applikationen in getrennten Namespaces, API-Kapselung via Ingress, vollautomatisierte CI/CD-Pipeline                                                |
| **E2** – Betrieb und Überwachung von Services               | Prometheus + Grafana Monitoring, Alerting, Rolling Updates, Backup-Konzept für persistente Daten                                                            |
| **F1** – Fehleranalyse und Protokollierung                  | Systematische Fehleranalyse via `kubectl logs`, Events, Grafana-Metriken. Dokumentation aller aufgetretenen Fehler                                          |
| **I1** – Dokumentation des Gesamtsystems                    | Netzwerkdiagramm, Architekturübersicht, Datenfluss CI/CD, Rollenkonzept (AWS IAM + Kubernetes RBAC)                                                         |

---

### 6. Grober Zeitplan (10 × 4 Lektionen)

| Woche | Thema                                                              |
| ----- | ------------------------------------------------------------------ |
| 1     | Projektplanung, Architektur definieren, AWS-Umgebung einrichten    |
| 2     | Terraform: VPC, EC2-Instanzen, Security Groups provisionieren      |
| 3     | RKE2 Master-Node installieren und konfigurieren                    |
| 4     | RKE2 Worker-Nodes hinzufügen, Cluster testen                       |
| 5     | Nginx Ingress Controller, Demo-App deployen                        |
| 6     | GitHub Actions CI/CD Pipeline aufbauen, Rolling Updates testen     |
| 7     | Podinfo deployen, Namespaces und RBAC konfigurieren                |
| 8     | Prometheus + Grafana installieren, Dashboards einrichten, Alerting |
| 9     | Fehleranalyse, Optimierungen, Kostenkontrolle AWS                  |
| 10    | Dokumentation finalisieren, Präsentation vorbereiten               |

---

### 7. Kostenkalkulation AWS

| Ressource           | Typ         | Kosten/h | ~100h Laufzeit |
| ------------------- | ----------- | -------- | -------------- |
| Master-Node         | t3.medium   | $0.04    | ~$4            |
| Worker-Node 1       | t3.medium   | $0.04    | ~$4            |
| Worker-Node 2       | t3.medium   | $0.04    | ~$4            |
| Load Balancer (ALB) | –           | pauschal | ~$8            |
| EBS Storage         | 3x 20GB gp3 | –        | ~$5            |
| Datenübertragung    | –           | –        | ~$3            |
| **Total geschätzt** |             |          | **~$28**       |

Budget verbleibt: ~$22 Puffer für unvorhergesehene Kosten.

---

### 8. Risiken

| Risiko                       | Wahrscheinlichkeit | Massnahme                                                      |
| ---------------------------- | ------------------ | -------------------------------------------------------------- |
| AWS-Kosten überschreiten 50$ | Mittel             | AWS Billing Alerts einrichten, Nodes bei Nichtgebrauch stoppen |
| RKE2 Cluster-Probleme        | Mittel             | Dokumentation, Community-Ressourcen, ggf. auf K3s fallback     |
| CI/CD Pipeline-Fehler        | Niedrig            | Testumgebung (separater Branch) vor Merge auf main             |
| Zeitknappheit                | Mittel             | Monitoring optional (Woche 8) kann vereinfacht werden          |

---

### 9. Arbeitstechnik

- **Wöchentliches Lernjournal:** Jede Woche wird dokumentiert was gelernt, was funktioniert hat und was nicht
- **Outcome-Dokumentation:** Laufend in GitHub Repository (`/docs`-Ordner)
- **Reflexion:** Am Ende jeder Woche kurze Reflexion zum eigenen Vorgehen

## Terraform – Infrastructure as code (IaC)

Terraform wird verwendet um die gesamte AWS-Infrastruktur automatisiert und reproduzierbar zu provisionieren. Anstatt Ressourcen manuell in der AWS Console zu erstellen, wird die Infrastruktur deklarativ im Code beschrieben.

### Dateistruktur

| Datei                 | Beschreibung                                      |
| --------------------- | ------------------------------------------------- |
| `main.tf`             | Hauptkonfiguration, definiert alle AWS-Ressourcen |
| `variables.tf`        | Variablen (Region, Projektname, etc.)             |
| `outputs.tf`          | Ausgaben nach dem Apply (VPC-ID, Subnet-ID, etc.) |
| `.terraform.lock.hcl` | Lockfile, fixiert die Provider-Version            |

### Netzwerk (VPC)

Folgende Ressourcen wurden mit Terraform in AWS erstellt:

- **VPC** (`10.0.0.0/16`) – privates Netzwerk für den gesamten Cluster
- **Public Subnet** (`10.0.1.0/24`) – Subnetz für die EC2 Nodes
- **Internet Gateway** – verbindet die VPC mit dem Internet
- **Route Table** – leitet Traffic vom Subnetz zum Internet Gateway

Hier sieht man den Output des Terraform apply:

![terraform_apply](media/terraform_apply.png)

und hier noch in AWS die der erstellte VPC

![VPC](media/VPC.png)

### Wichtige Befehle

| Befehl              | Beschreibung                                   |
| ------------------- | ---------------------------------------------- |
| `terraform init`    | Provider herunterladen, Projekt initialisieren |
| `terraform plan`    | Vorschau anzeigen was erstellt/geändert wird   |
| `terraform apply`   | Infrastruktur in AWS erstellen                 |
| `terraform destroy` | Alle erstellten Ressourcen löschen             |