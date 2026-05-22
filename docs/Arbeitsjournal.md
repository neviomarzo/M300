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

| Problem | Ursache | Lösung / Reflexion |
|---|---|---|
| `sudo apt install terraform` fehlgeschlagen | Terraform nicht im Standard-APT Repository | HashiCorp Repository manuell hinzugefügt |

---

### Ressourcen

| Ressource | Link |
|---|---|
| Terraform Installationsdoku | https://developer.hashicorp.com/terraform/downloads |
| AWS CLI Doku | https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html |
| RKE2 Doku | https://docs.rke2.io |

---

### Praktische Übung

Was gemacht:
Terraform initialisiert und erste Konfiguration geschrieben (VPC, Subnetz, Internet Gateway, Route Table) — noch kein `terraform apply`, nur Struktur aufgebaut.

Was gelernt:
Terraform funktioniert mit Providern die aus der Registry geladen werden. Infrastruktur wird deklarativ beschrieben — man definiert den Zielzustand, Terraform kümmert sich ums Wie.