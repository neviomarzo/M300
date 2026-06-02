# Arbeitsjournal – M300 Cloud Modul

**Name:** Nevio
**Modul:** M300 – Cloud & Infrastruktur
**Zeitraum:** Mai – Juli 2026

---

## Woche 1 – 22.05.2026

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

## Woche 2 – 29.05.2026

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

## Arbeit Zuhause – 02.06.2026

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