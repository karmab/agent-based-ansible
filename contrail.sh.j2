#!/usr/bin/env bash

MANIFESTS=$(readlink -f {{ manifests }})
VERSION={{ contrail_version|default("23.1") }}
CTL_CIDR={{ contrail_ctl_cidr|default("10.40.1.0/24") }}
CTL_GATEWAY={{ contrail_ctl_gateway|default("10.40.1.1") }}
PULL_SECRET="{{ pull_secret|default('openshift_pull.json') }}"
export AUTH=$(cat $PULL_SECRET | jq '.auths["enterprise-hub.juniper.net"].auth')
PULLSECRET_ENCODED=$(envsubst < contrail.auth | base64 -w0)
[ -d contrail-networking ] && rm -rf contrail-networking
git clone https://github.com/Juniper/contrail-networking
cd contrail-networking/releases/$VERSION/ocp
sed -i "s@10.40.1.0/24@$CTL_CIDR@" vrrp/*99-network-configmap.yaml
sed -i "s@10.40.1.1@$CTL_GATEWAY@" vrrp/*99-network-configmap.yaml

FIRST_NIC={{ contrail_data_nic|default("enp1s0") }}
SECOND_NIC={{ contrail_ctl_nic|default("enp2s0") }}
sed -i "s@ens3@$FIRST_NIC@" *99-disable-offload-master.yaml *99-disable-offload-worker.yaml
sed -i "s@ens4@$SECOND_NIC@" vrrp/*99-disable-offload-master-ens4.yaml vrrp/*99-disable-offload-worker-ens4.yaml

rm -rf auth-registry/103-contrail-analytics-imagepullsecret.yaml
sed -i "s@<base64-encoded-credential>@$PULLSECRET_ENCODED@" auth-registry/*pullsecret.yaml

find . -name "*yaml" -exec cp {} $MANIFESTS \;
