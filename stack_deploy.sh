export ETCD_IP=192.168.3.170
export ETCD_NODE1_IP=192.168.3.21
export ETCD_NODE2_IP=192.168.3.33
docker stack deploy -c docker-stack.yml etcd_registrator