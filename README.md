# Helloworld Auth
Don't worry, even though this README is in Portuguese, the code is fully bilingual! It speaks fluent Python... and English. So, go ahead and dive in — no translation required, just your coding skills! 😎

**Helloworld Auth** é uma biblioteca poderosa para gerenciamento de autenticação e autorização, projetada para ser flexível e escalável, permitindo suporte a múltiplos métodos de login e controle avançado de permissões. Construída sobre os princípios da **Clean Architecture**, ela oferece uma implementação robusta e extensível para lidar com fluxos de autenticação e segurança em qualquer aplicação.

## Principais Funcionalidades

- **Autenticação Multi-login:** Suporte para login via email, telefone e nome de usuário.
- **Gerenciamento de Tokens JWT:** Emissão, validação e revogação de tokens JWT para garantir segurança e controle de sessões.
- **Autorização Avançada:** Controle de permissões baseado em escopos, facilmente customizável para diferentes cenários.
- **Integração com Múltiplas Fontes de Dados:** Compatível com bancos de dados SQL e NoSQL, permitindo integração fluida com diferentes tecnologias de armazenamento.
- **Suporte a Mensageria:** Integração com Kafka para notificações e envio de eventos.
- **Recuperação de Senhas:** Implementação de fluxo para recuperação e redefinição de senhas.
- **Serviço de Emails:** Suporte a templates de email para enviar notificações de login e mensagens de recuperação de senha.


## Integração com Helloworld Core
A Helloworld Auth foi projetada para se integrar perfeitamente com a [**Helloworld Core**](https://github.com/edicleoline/helloworld-core), permitindo que você tire proveito da arquitetura limpa e de funcionalidades como o Unit of Work e o Repository Pattern. Isso torna a implementação de autenticação altamente modular e escalável, além de suportar múltiplas fontes de dados em uma única unidade de trabalho.

## Recursos Avançados
1. Autenticação Baseada em Eventos: suporta uma abordagem orientada a eventos para autenticação, facilitando a integração com sistemas de mensageria como Kafka.
2. Controle de Escopos e Permissões: defina escopos customizados para gerenciar o acesso dos usuários a diferentes funcionalidades.
3. Templates de Email: notificações de login e recuperação de senha utilizando templates customizados.
4. Suporte a Login Externo: Integração com provedores de autenticação externa.

## TODO

Aqui estão algumas funcionalidades que já estamos implementando no **helloworld-auth**:

- **Autenticação utilizando login de terceiros (OAuth2)**: Suporte para autenticação via plataformas como Google, Facebook, GitHub, e outras usando o padrão OAuth2.
  
- **Autorização**: Adicionar mecanismos robustos de controle de acesso e permissões, garantindo uma gestão precisa e eficiente dos níveis de acesso dos usuários.

- **Configuração**: Alterar facilmente o comportamento da biblioteca por meio de opções de configuração personalizáveis.

Fique de olho nas próximas atualizações! 🚀

## Contribua
Gostou do projeto? Contribua com melhorias, abra issues ou envie um pull request. Toda ajuda é bem-vinda!


