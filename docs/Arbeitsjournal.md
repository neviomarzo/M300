# Arbeitsjournal – M300 Cloud Modul

**Name:** Nevio
**Modul:** M300 – Cloud & Infrastruktur
**Zeitraum:** Mai – Juli 2026

- [Arbeitsjournal – M300 Cloud Modul](#arbeitsjournal--m300-cloud-modul)
  - [22.05.2026](#22052026)
    - [Tagesziele](#tagesziele)
    - [Resultate](#resultate)
    - [Probleme \& Reflexion](#probleme--reflexion)
    - [Ressourcen](#ressourcen)
    - [Praktische Übung](#praktische-übung)
  - [29.05.2026](#29052026)
    - [Tagesziele](#tagesziele-1)
    - [Resultate](#resultate-1)
    - [Probleme \& Reflexion](#probleme--reflexion-1)
    - [Ressourcen](#ressourcen-1)
    - [Praktische Übung](#praktische-übung-1)
  - [02.06.2026](#02062026)
    - [Tagesziele](#tagesziele-2)
    - [Resultate](#resultate-2)
    - [Probleme \& Reflexion](#probleme--reflexion-2)
    - [Ressourcen](#ressourcen-2)
    - [Praktische Übung](#praktische-übung-2)
  - [05.06.2026](#05062026)
    - [Tagesziele](#tagesziele-3)
    - [Resultate](#resultate-3)
    - [Probleme \& Reflexion](#probleme--reflexion-3)
    - [Ressourcen](#ressourcen-3)
    - [Praktische Übung](#praktische-übung-3)
  - [12.06.2026](#12062026)
    - [Tagesziele](#tagesziele-4)
    - [Resultate](#resultate-4)
    - [Probleme \& Reflexion](#probleme--reflexion-4)
    - [Ressourcen](#ressourcen-4)
    - [Praktische Übung](#praktische-übung-4)
  - [14.06.2026](#14062026)
    - [Tagesziele](#tagesziele-5)
    - [Resultate](#resultate-5)
    - [Probleme \& Reflexion](#probleme--reflexion-5)
    - [Ressourcen](#ressourcen-5)
    - [Praktische Übung](#praktische-übung-5)

---

## 22.05.2026

---

### Tagesziele

- [x] Eigene Lernumgebung einrichten
- [x] Link zu Repo in Link-Liste eintragen
- [x] Erste Idee für eigenes Projekt entwickeln und dokumentieren
  - [x] Pflichtaspekte gemäss Kompetenzmatrix abgedeckt
  - [x] Use-Case mit praktischem Nutzen definiert

---

### Resultate

- Lernumgebung eingerichtet (Terraform, AWS CLI installiert und konfiguriert)
- GitHub Repo `M300` erstellt und verlinkt
- Projektidee definiert: RKE2 Multi-Node Kubernetes-Cluster auf AWS mit CI/CD (GitHub Actions), Monitoring (Prometheus + Grafana) und mehreren Apps in getrennten Namespaces

---

### Probleme & Reflexion

| Problem                                     | Ursache                                    | Lösung / Reflexion                       |
| ------------------------------------------- | ------------------------------------------ | ---------------------------------------- |
| `sudo apt install terraform` fehlgeschlagen | Terraform nicht im Standard-APT Repository | HashiCorp Repository manuell hinzugefügt |

---

### Ressourcen

| Ressource                   | Link                                                                  |
| --------------------------- | --------------------------------------------------------------------- |
| Terraform Installationsdoku | <https://developer.hashicorp.com/terraform/downloads>                 |
| AWS CLI Doku                | <https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html> |
| RKE2 Doku                   | <https://docs.rke2.io>                                                |

---

### Praktische Übung

Was gemacht:
Terraform initialisiert und erste Konfiguration geschrieben (VPC, Subnetz, Internet Gateway, Route Table) — noch kein `terraform apply`, nur Struktur aufgebaut.

Was gelernt:
Terraform funktioniert mit Providern die aus der Registry geladen werden. Infrastruktur wird deklarativ beschrieben — man definiert den Zielzustand, Terraform kümmert sich ums Wie.

Hier der Eintrag für Woche 2:

---

## 29.05.2026

---

### Tagesziele

- [x] Terraform: VPC, EC2-Instanzen, Security Groups provisionieren

---

### Resultate

- VPC, Subnetz, Internet Gateway und Route Table via Terraform erstellt
- Security Groups für RKE2 Cluster konfiguriert (SSH, Kubernetes API, Ingress, etc.)
- SSH Key Pair in AWS importiert
- EC2 Instanzen provisioniert (1 Master, 2 Worker, Ubuntu 22.04, t3.medium)

---

### Probleme & Reflexion

| Problem                          | Ursache                                                           | Lösung / Reflexion                                 |
| -------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------- |
| `terraform apply` mit 403 Fehler | AWS Region falsch konfiguriert (`eu-central-1` statt `us-east-1`) | Region in `variables.tf` auf `us-east-1` angepasst |

---

### Ressourcen

| Ressource                   | Link                                                                |
| --------------------------- | ------------------------------------------------------------------- |
| Terraform AWS Provider Doku | <https://registry.terraform.io/providers/hashicorp/aws/latest/docs> |
| RKE2 Ports Doku             | <https://docs.rke2.io/install/requirements#networking>              |

---

### Praktische Übung

Was gemacht:
Vollständige AWS Infrastruktur via Terraform provisioniert — VPC, Subnetz, Internet Gateway, Route Table, Security Groups und 3 EC2 Instanzen.

Was gelernt:
Terraform erstellt Ressourcen automatisch in der richtigen Reihenfolge basierend auf Abhängigkeiten. Mit `count` können mehrere identische Ressourcen mit einer einzigen Definition erstellt werden.

---

## 02.06.2026

---

### Tagesziele

- [x] RKE2 Cluster installieren und konfigurieren
- [x] Rancher installieren

---

### Resultate

- RKE2 Multi-Node Cluster via Ansible Playbook (`ranchergovernment/rke2-ansible`) installiert
- Alle 3 Nodes als `Ready` registriert
- Rancher via Helm installiert, erreichbar unter <https://rancher.sybhad.ch>
- TLS-Zertifikat automatisch via Let's Encrypt ausgestellt

---

### Probleme & Reflexion

| Problem | Ursache | Lösung / Reflexion         |
| ------- | ------- | -------------------------- |
| –       | –       | Keine Probleme aufgetreten |

---

### Ressourcen

| Ressource                 | Link                                                                                                                       |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| RKE2 Ansible Playbook     | <https://github.com/ranchergovernment/rke2-ansible>                                                                        |
| Rancher Installationsdoku | <https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster> |

---

### Praktische Übung

Was gemacht:
RKE2 Cluster mit Ansible aufgesetzt und Rancher installiert. Alles ausserhalb der Schulzeit zuhause durchgeführt.

Was gelernt:
Ansible Playbooks ermöglichen eine automatisierte und reproduzierbare Installation auf mehreren Nodes gleichzeitig. Rancher bietet eine übersichtliche UI zur Verwaltung des Clusters und wird mit Let's Encrypt automatisch mit einem gültigen TLS-Zertifikat gesichert.

Hier der Eintrag:

---

## 05.06.2026

---

### Tagesziele

- [x] Cert-Manager und ClusterIssuer konfigurieren
- [x] Podinfo deployen und Ingress mit Let's Encrypt einrichten
- [x] Prometheus + Grafana (kube-prometheus-stack) installieren

---

### Resultate

- Cert-Manager via Helm installiert, ClusterIssuer `letsencrypt-prod` mit HTTP01-Challenge erstellt
- Podinfo via Rancher im Namespace `app-podinfo` deployed
- Ingress für Podinfo erstellt, TLS-Zertifikat automatisch via Let's Encrypt ausgestellt
- Podinfo erreichbar unter <https://podinfo.sybhad.ch>
- kube-prometheus-stack via Rancher im Namespace `monitoring` installiert

---

### Probleme & Reflexion

| Problem | Ursache | Lösung / Reflexion         |
| ------- | ------- | -------------------------- |
| –       | –       | Keine Probleme aufgetreten |

---

### Ressourcen

| Ressource             | Link                                                |
| --------------------- | --------------------------------------------------- |
| Cert-Manager Doku     | <https://cert-manager.io/docs>                        |
| Podinfo Helm Chart    | <https://stefanprodan.github.io/podinfo>              |
| kube-prometheus-stack | <https://github.com/prometheus-community/helm-charts> |

---

### Praktische Übung

Was gemacht:
Cert-Manager installiert und ClusterIssuer für Let's Encrypt konfiguriert. Podinfo via Rancher deployed und Ingress mit automatischem TLS erstellt. Monitoring-Stack via Rancher installiert.

Was gelernt:
Cert-Manager nimmt einem die manuelle Zertifikatsverwaltung komplett ab — sobald der Ingress mit der richtigen Annotation erstellt wird, läuft alles automatisch. Der kube-prometheus-stack bündelt Prometheus, Grafana und Alertmanager in einem einzigen Helm Chart.

---

## 12.06.2026

---

### Tagesziele

- [x] Flask Demo-App entwickeln und deployen
- [x] CI/CD Pipeline mit GitHub Actions aufbauen

---

### Resultate

- Flask Demo-App entwickelt — zeigt Pod-Name, Node, Namespace und Version
- Docker Image via GitHub Actions automatisch gebaut und zu GHCR gepusht
- Kubernetes Manifests erstellt (Deployment, Service, Ingress)
- CI/CD Pipeline deployed automatisch bei Push auf `main`-Branch
- Demo-App erreichbar unter <https://demo.sybhad.ch>
- Grafana Ingress erstellt, erreichbar unter <https://grafana.sybhad.ch>

---

### Probleme & Reflexion

| Problem                                          | Ursache                                  | Lösung / Reflexion                                 |
| ------------------------------------------------ | ---------------------------------------- | -------------------------------------------------- |
| Node.js 20 Deprecation Warning in GitHub Actions | Actions verwenden intern noch Node.js 20 | `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true` gesetzt |

---

### Ressourcen

| Ressource                | Link                                                                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| GitHub Actions Doku      | <https://docs.github.com/en/actions>                                                                              |
| GHCR Doku                | <https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry> |
| docker/build-push-action | <https://github.com/docker/build-push-action>                                                                     |

---

### Praktische Übung

Was gemacht:
Flask Demo-App entwickelt die Kubernetes-Laufzeitinformationen anzeigt. GitHub Actions Pipeline aufgebaut die das Docker Image automatisch baut, zu GHCR pusht und auf den Cluster deployed.

Was gelernt:
GitHub Actions ermöglicht eine vollständig automatisierte CI/CD Pipeline. Mit `GITHUB_TOKEN` kann direkt zu GHCR gepusht werden ohne zusätzliche Credentials. Kubernetes Rolling Updates laufen automatisch ohne Downtime wenn ein neues Image deployed wird.

---

## 14.06.2026

---

### Tagesziele

- [x] Konnektivitätstests durchführen und dokumentieren
- [x] Dokumentation um Technologie-Begründungen (A1) ergänzen
- [x] Rollenkonzept (I1) vorbereiten

---

### Resultate

- Cluster-Status geprüft: alle 3 Nodes `Ready` mit RKE2 `v1.35.5+rke2r2`
- HTTPS-Erreichbarkeit aller Apps via `curl -I` getestet (demo, podinfo, grafana)
- TLS-Zertifikate bei allen drei Domains aktiv (HSTS-Header gesetzt)
- Abschnitt "Technologie-Begründungen" in der Dokumentation ergänzt (Begründungen für RKE2, t3.medium, Nginx, Terraform, GHCR)
- Aktuellen Stand für Rollenkonzept analysiert: noch keine RBAC-Rollen definiert, Zugriff aktuell via `cluster-admin`

---

### Probleme & Reflexion

| Problem                                 | Ursache                                 | Lösung / Reflexion                                   |
| --------------------------------------- | --------------------------------------- | ---------------------------------------------------- |
| Podinfo antwortet mit 405 auf `curl -I` | Podinfo unterstützt keine HEAD-Requests | Kein Fehler, normales Verhalten der App dokumentiert |

---

### Ressourcen

| Ressource                     | Link                                                            |
| ----------------------------- | --------------------------------------------------------------- |
| Kubernetes RBAC Doku          | <https://kubernetes.io/docs/reference/access-authn-authz/rbac/> |
| Cert-Manager HTTP01 Challenge | <https://cert-manager.io/docs/configuration/acme/http01/>       |

---

### Praktische Übung

Was gemacht:
Konnektivitätstests für Cluster und alle drei Applikationen durchgeführt und dokumentiert. Dokumentation um Technologie-Begründungen ergänzt.
