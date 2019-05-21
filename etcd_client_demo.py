import etcd


client = etcd.Client(host='192.168.3.170', port=2379)

SERVICE_PATH = '/trunk/services/'

SERVICE_NAME = 'test_service'

try:
    client.read(SERVICE_PATH)

    req_path = SERVICE_PATH + SERVICE_NAME

    directory = client.get(req_path)
    if directory and directory.children:
        for obj in directory.children:
            print(str(obj.key) + ': ' + str(obj.value))

except etcd.EtcdKeyNotFound:
    print('SERVICE_PATH: ' + req_path + ' read error!')
