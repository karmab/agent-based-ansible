# Deploying with agent based workflow through a playbook

This directory contains a playbook that can be used to deploy an Openshift Cluster using agent based workflow

Code to boot the nodes using redfish is also available.

## Requisites

- Valid pull secret
- Ansible installed
- Bmc urls details of your target nodes
- Nmstatectl and python3-netaddr installed

## How to use

1. Prepare a valid inventory file (check the [sample one](inventory.yml.sample) for reference). Give it a yml suffix
2. Run `ansible-playbook -i inventory.yml run.yml`

## Relevant variables

|Parameter           |Default Value       |
|--------------------|------------------  |
|pull_secret         |openshift_pull.json |
|disconnected_url    |None                |
|disconnected_prefix |ocp4                |
|ca                  |None                |
|ipv6                |False               |
|sno                 |False               |
|sno_cpuset          |None                |
|api_vip             |None                |
|ingress_vip         |None                |
|machine_networks    |[]                  |
|version             |stable              |
|tag                 |4.12                |
|operators           |[]                  |
|manifests           |manifests           |
|extra_manifests     |extra_manifests     |

## Emulating baremetal hosts with kcli

A [kcli plan](kcli_plan.yml) is provided to create 3 vms with specific macaddresses on a non dhcp libvirt network

The plan can be run with

```
kcli create plan agent-based
```
