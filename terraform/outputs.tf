output "master_ip" {
  description = "Public IP Master Node"
  value       = aws_instance.master.public_ip
}

output "worker_ips" {
  description = "Public IPs Worker Nodes"
  value       = aws_instance.worker[*].public_ip
}
