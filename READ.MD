Criar cluster Kubenetes.

Subir o zookepper.

Selecionar "Cargas de trabalho", ir em implantar.

Em caminho da imagem informar: wurstmeister/zookeeper .
Conforme meu docker-compose não é necessário informar variável de ambiente.

Em configuração > Nome do aplicativo : zookeeper

Após criado tem que expor ele com um serviço.

O botão Expor ou no menu Ações, tem a funcionalidade.

Usar a porta > 2181:2181

E usar tipo de serviço: Balanceador de carga.

Agora subir o kafka.

Vou subir o kafka via arquivo.

Ao acessar o console do google pode criar um aquivo dentro do console, ou de 
um repositorio.

kubectl create --filename kafka.yaml

Após o serviço está de pé, altera no dkafka ou no kafka.dep.yaml os ips.

KAFKA_ZOOKEEPER_CONNECT com o ip do service do zookeeper e 
KAFKA_ADVERTISED_HOST_NAME com o ip do service do kafka 

Agora ir em Cargas de trabalho para ver o deployment subir.

Alguns termos do kubernetes.
http://www.cienciaedados.com/kubernetes-pods-nodes-containers-e-clusters/


Abrir terminal e criar uma conexão via terminal.

kafka-console-consumer.sh --bootstrap-server 35.238.211.44:9092  --topic test-topic
kafka-console-producer.sh --broker-list 35.238.211.44:9092 --topic test-topic


