Criar cluster Kubenetes.

Subir o zookepper.

Selecionar "Cargas de trabalho", ir em implantar.

Em caminho da imagem informar: wurstmeister/zookeeper .
Conforme meu docker-compose não é necessário informar variável de ambiente.

Em configuração > Nome do aplicativo : zookeeper

Após criado tem que expor ele com um serviço.

O botão Expor ou no menu Ações, tem a funcionalidade.

Usar a porta > 2181:2181

E usar tipo de serviço: Balanceador de carga

