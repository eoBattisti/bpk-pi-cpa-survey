# BPK Search

1. [Características gerais da aplicação](#características-gerais-da-aplicação)
	1. [Tabela de dados](#tabela-de-dados)
	2. [Cabeçalho](#cabeçalho)
	3. [Formulários](#formulários)
2. [Área Pública](#área-pública)
	1. [Pesquisa](#pesquisa)
		1. [Nuvem de palavra](#nuvem-de-palavra)
		2. [Carrossel de eventos](#carrossel-de-eventos)
		3. [Menu de filtros](#menu-de-filtros)
		4. [Resultados](#resultados)
	2. [Pesquisa pré-configurada (Empresa, Produto, Serviço)](#pesquisa-pré-configurada)
	3. [Eventos](#eventos)
3. [Área residente](#área-residente)
	1. [Principal](#principal)
	2. [Listagem de empresas](#listagem-de-empresas)
	3. [Editor de empresa](#editor-de-empresa)
	4. [Listagem de páginas](#listagem-de-páginas)
	5. [Editor de página](#editor-de-página)
		1. [Características do editor de página](#características-do-editor-de-página)
		2. [Campos](#campos)
			1. [Títulos e Sub-títulos](#títulos-e-sub-títulos)
			2. [Endereço de página](#endereço-de-página)
			3. [Conteúdo da página](#conteúdo-da-página)
			4. [Imagem principal](#imagem-principal)
			5. [Formulário de Lead](#formulário-de-lead)
			6. [Título da pesquisa](#título-da-pesquisa)
			7. [Logos](#logos)
			8. [Tipo de visualização da busca](#tipo-de-visualização-da-busca)
			9. [Palavras-chave](#palavras-chave)
			10. [Descrição SEO](#descrição-seo)
			11. [Título da página SEO](#título-da-página-seo)
			12. [Seção de números](#seção-de-números)
			13. [Seção de destaques](#seção-de-destaques)
			14. [Seção de produtos](#seção-de-produtos)
			15. [Seção de serviços](#seção-de-serviços)
			16. [Mesclar as seções de produto e serviço](#mesclar-as-seções-de-produto-e-serviço)
			17. [Seção de mídias sociais](#seção-de-mídias-sociais)
			18. [Seção de funcionalidades](#seção-de-funcionalidades)
			19. [Seção de resultados](#seção-de-resultados)
			20. [Seção de imagens](#seção-de-imagens)
			21. [Seção de convidados](#seção-de-convidados)
	6. [Listagem de eventos](#listagem-de-eventos)
	7. [Editor de evento](#editor-de-evento)
	8. [Listagem de usuários](#listagem-de-usuários)
	9. [Editor de usuário](#editor-de-usuário)
	10. [Quadro de notificações](#quadro-de-notificações)
	11. [Editor de notificação](#editor-de-notificação)
	12. [Listagem de contatos](#listagem-de-contatos)

# Estrutura do projeto

A aplicação foi implementada através do framework django e django rest para linguagem python, utilizando o banco de dados postgreSQL.

A estrutura do projeto fica localizada dentro da pasta django contendo os principais arquivos:

- `.eslintrc.json`: arquivo designado para a configuração do ESLint, que faz análise estática do código javascript para encontrar problemas e erros.
- `.prettierrc.json`: utilizado para configurar o Prettier, responsável pela formatação do código.
- `.prospector.yaml`: configuração do Prospector, responsável pela análise do código python em busca de problemas e erros.
- `.pylintrc`: configuração do Pylint, linter de código python que assegura a qualidade do código.
- `DockerFile`: possui as instruções necessárias para a construção do container do Django.
- `Makefile`: contém as instruções da ferramenta de automação de compilação make.
- `manage.py`: arquivo destinado ao utilitário de linha de comando do django, através dele que algumas instruções são executadas para-se trabalhar com o django.

O django realiza a separação do projeto através de uma pasta raiz e outras pastas separadas por apps.

- Pasta raíz: `biopark/`;
- Apps:
    - `companies/`: Contempla as entidades de Empresa, leads e log;
    - `events/`;
    - `groups/`;
    - `notifications/`;
    - `pages/`;
    - `permissions/`;
    - `users/`;

A arquitetura do django utiliza o padrão MTV (Model, Template, View):

- Model: Entidade da aplicação.
- Template: Etapa que consiste na renderização das páginas (HTML).
- View: Contém a lógica para o processo de renderização da página.

Para o django Rest o processo é diferente, os models passam por um processo de serialização (serializers.py) e depois são manipulados através de ViewSets (viewsets.py), para que de fato os registros sejam entregados ao endpoint.

Todas as classes e funções implementadas no django foram construídas a partir do padrão que a documentação expõe:

- [Django](https://docs.djangoproject.com/en/4.1/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

Principais arquivos e diretórios do projeto Django:

- Diretórios:
    - `locale/`: registram em arquivos `.po` traduções da aplicação.
    - `public_static/`: diretório reservado aos arquivos estáticos gerados pelo django.
    - `static/`: arquivos estáticos base que serão utilizados pelo django. Os arquivos estáticos são separados em pastas:
        - `css/`: armazena todos as folhas de estilos.
        - `js/`: armazena todos os arquivos de script.
        - `json/`: armazena dados estruturados em json.
        - `media/`: armazena os arquivos de media.
        - `plugins/`: contém os plugins vendorizados que são utilizados no frontend.
    - `templates/`: mantém todos os templates principais da aplicação, algumas pastas importantes são:
        - `handler/`: contém os templates utilizados na tratativa de erros (400, 403, 404 e 500);
        - `layout/`: contém os templates utilizados para a construção do layout da aplicação;
        - `registration/`: contém os templates utilizados em autenticações e para o processo de reset de senha;
        - `form/`: contém todos os templates de formulário.
        - `list/`: contém todos os templates de datatable.
    - `templatetags/`: registram tags customizáveis para ser utilizado pelo template-engine Jinja.

- Arquivos:
    - `middleware.py`: contém os middlewares utilizados no processo de request/response.
    - `mixins.py`: contém abstração para serem reutilizadas em outras classes.
    - `serializers.py`: contém as classes utilizadas no processo de serialização dos endpoints do Django Rest.
    - `urls.py`: registra todas as rotas da aplicação. Em apps, serão registradas as rotas relacionadas ao app, já na pasta raiz será incluindo as rotas definidas no diretório raiz e também as rotas incluídas em outros apps.
    - `utils.py`: contém funções utilitárias à aplicação.
    - `views.py`: registra as views do padrão MTV.
    - `viewsets.py`: registra viewsets do DRF (Django rest framework).
    - `models.py`: registra as entidades da aplicação.
    - `forms.py`: contém a classe de configuração do formulário para ser utilizado no processo de criação/atualização da entidade no padrão MTV.

A pasta raiz fica localizada no diretório `biopark`, contendo arquivos de configuração do django e componentes da aplicação de forma global. Entre os principais arquivos/diretórios destacados na raiz, estão:

- `fixtures/`: salvam dados que são importados ao banco pelo Django de forma automática quando o servidor é iniciado.
- `media/`: diretório destinado a publicação de arquivos durante o desenvolvimento local.
- `requirements/`: organiza todos os pacotes da aplicação gerenciados pelo gerenciador de pacotes PIP em quatro arquivos (CI, Development, Main, Production)
- `settings/`: mantém as configurações do django separados por três arquivos: Main, Development, Production.
- `api_urls.py`: arquivo destinado ao cadastro de Viewsets da API Rest em rotas.
- `defaults.py`: contém listas de tuplas para serem utilizados em campos do tipo integer como choice.
- `urls.py`: registra todas as rotas da aplicação incluindo as rotas de outros módulos.

Os arquivos/diretórios característicos de um app do Django são:

- `migrations/`: salvam todas as migrações que são geradas automaticamente pelo django quando o model sofre atualização.
- `admin.py`: contém classes de configuração do django admin para cada entidade.

O frontend foi construído a partir do template metronic.

## Comandos do docker

Para buildar os containers é necessário executar o comando:

`docker-compose build`

Para iniciar os containers utiliza-se o comando:

`docker-compose up`

Para encerrar:

`docker-compose down`

Caso seja necessário apagar todos os containers:

`docker-compose down -v`

## Comandos do django

Para iniciar o servidor manualmente:

`docker-compose run django ./manage.py runserver`

Para criar as migrações manualmente:

`docker-compose run django ./manage.py makemigrations`

Para efetuar as migrações:

`docker-compose run django ./manage.py migrate`

Para acessar o shell com a aplicação em processo de execução:

`docker-compose exec django ./manage.py shell`

Para extrair termos da aplicação para tradução é necessário executar o comando:

`docker-compose exec django ./manage.py makemessages`

Após traduzir os termos é necessário aplicar a tradução:

`docker-compose exec django ./manage.py compilemessages`

# Características gerais da aplicação

## Tabela de dados

Todas as tabela de dados da aplicação possuem estruturas semelhantes, na parte superior é localizado um título com a quantidade de registros geral, ao lado direito é possível alterar o modo de visualização, normalmente entre arquivados e não arquivados, quando o registro em questão pode ser arquivado.

![](./assets/Pasted%20image%2020230109161324.png)

O cabeçalho da tabela pode conter a implementação para ordenar a tabela com base na coluna.

![](./assets/Pasted%20image%2020230109161426.png)

A tabela contém filtros localizados logo após o header. Os tipos de filtro podem variar de:
- Textual; 
- Seleção de opção;
- Seleção de data;

![](./assets/Pasted%20image%2020230109161525.png)

Em caso de resoluções menores o filtro é extraído da tabela para que fique em um local mais adequado visualmente.

![](./assets/Pasted%20image%2020230109161733.png)

Semelhante aos filtros, as linhas podem ser retraídas para adequar o conteúdo visual à resoluções menores.

![](./assets/Pasted%20image%2020230109161934.png)

Quando a linha estiver retraída, haverá um sinal de mais (+) que quando pressionado o restante da linha é apresentado alternando o ícone para um sinal de menos (-).

## Cabeçalho

O Cabeçalho pode possuir comportamentos diferentes com base no acesso do usuário, caso seja um acesso anônimo que o usuário não precisou efetuar o login, a aplicação irá mostrar apenas a barra da área pública e de forma contrária, caso o usuário esteja logado, haverá duas barras, uma para a área residente localizada na parte superior e uma para a área pública na parte inferior.

![](./assets/Pasted%20image%2020230109163107.png)

Na barra de área residente, além dos menus, também existe um sino de notificação que é mostrado apenas quando o usuário possui permissão de visualizar notificação, um ícone de sol que permite alternar o modo noturno da aplicação e a foto do usuário que pode ser expandido informando o nome e o e-mail, além da opção de desconectar.

![](./assets/Pasted%20image%2020230109163400.png)

![](./assets/Pasted%20image%2020230109163426.png)

![](./assets/Pasted%20image%2020230109163454.png)

## Formulários

Todos os formulários da aplicação possuem características semenlhantes. Os asteriscos vermelhos indicam obrigatoriedade do campo.

![](./assets/Pasted%20image%2020230110083755.png)

O ícone de exclamação é utilizado para obter mais informações sobre o campo quando o usuário posiciona o ponteiro sobre o ícone.

![](./assets/Pasted%20image%2020230110083903.png)

As caixas de entrada de texto possuem contadores de caracteres, indicando a quantidade atual e a quantidade máxima permitida pelo campo.

![](./assets/Pasted%20image%2020230110084030.png)

Toda alteração no formulário dispara eventos de validação e se caso houver algum campo incorreto, uma mensagem vermelha é posicionada abaixo mostrando o erro.

![](./assets/Pasted%20image%2020230110084300.png)

# Área pública

## Pesquisa

A tela de pesquisa pode ser acessada a partir do menu no cabeçalho da página.

![](./assets/Pasted%20image%2020230109163810.png)

A tela de pesquisa é constituída por uma barra de pesquisa, filtros avançados, nuvem de palavra e carrossel de eventos. Inicialmente, será mostrado apenas a nuvem de palavra e, quando houver eventos futuros, o carrossel de eventos.

### Nuvem de palavra

A nuvem de palavra é construída a partir das palavras-chave das páginas cadastradas na plataforma do Biopark de forma aleatória.

![](./assets/Pasted%20image%2020230105105905.png)

Caso uma destas palavra seja pressionada uma busca rápida será efetuada, mostrando as páginas que possuem relação com a palavra ou com termos semelhantes.

### Carrossel de eventos

O Carrossel de eventos lista todos os eventos a partir da data de acesso à plataforma, ou seja, sempre informando eventos futuros. Quando não houver nenhum evento, o carrossel será suprimido.

![](./assets/Pasted%20image%2020230105140734.png)

### Menu de filtros

O Menu de filtros pode ser expandido a partir do botão "Filtros" ao lado do botão de busca. Existem três filtros avançados:
- Palavras-chave: quando configurado irá buscar exatamente as palavras-chave que estão cadastradas nas páginas;
- Categorias: possui as opções: Empresa, Serviços, Produtos, Eventos e Tudo.
- Atividade: se selecionado irá buscar por páginas que sejam de empresas relacionadas a atividade marcada.

![](./assets/Pasted%20image%2020230105141401.png)

### Resultados

Após a pesquisa ser efetuada será mostrado o total de resultados, botões para alterar a visão, um seletor para ordenar a busca e um botão de cópia.

Os resultados poderão ser informados em dois estilos: em forma de card ou em forma de tabela.

![](./assets/Pasted%20image%2020230105142905.png)

![](./assets/Pasted%20image%2020230105143034.png)

A forma de visualização pode ser alterada através destes botões:

![](./assets/Pasted%20image%2020230105143119.png)

O primeiro indica a visualização em cards e o segundo em tabela.

![](./assets/Pasted%20image%2020230105143148.png)

O seletor de ordenação poderá ser configurado para ordernar por páginas atualizadas recentemente ou páginas mais antigas.

O botão de "Copiar Busca" quando selecionado irá levar para a área de transferência (ctrl + c) a configuração de filtros para que um usuário possa rapidamente compartilhar a sua busca com outro usuário.

![](./assets/Pasted%20image%2020230105143243.png)

Por exemplo, uma busca por páginas de tecnologia sobre sistemas foi feita:

![](./assets/Pasted%20image%2020230105144128.png)

Quando a busca for copiada, o usuário poderá enviar o link para outro usuário através do ctrl + v: 
`https://search.bpk.com.br/search/?search=Sistemas&type=4&activity=6375a6fd-7ada-452f-b33d-9a0400607a9a&page_size=9&status=1&archived=false`

## Pesquisa pré-configurada

Os menus "Empresa", "Produto" e "Serviço" da área pública possuem o mesmo destino que o menu de pesquisa, no entanto, a diferença é que estas páginas já vão carregar a pesquisa com o filtro de categoria pré-configurado para que a busca seja feita de forma automática.

![](./assets/Pasted%20image%2020230105144348.png)

## Eventos

A página de eventos irá levar o usuário até o calendário contendo todos os eventos registrados na plataforma e pode ser acessada a partir do menu "Eventos" no cabeçalho da área pública.

![](./assets/Pasted%20image%2020230109165656.png)

Os eventos são categorizados em dois tipos:
- Internos: Apenas usuários do BPK Search veem eventos internos;
- Externos: Qualquer usário pode visualizar, até os anônimos;

Os internos só serão mostrados no calendário em caso de acesso a aplicação (Login).

![](./assets/Pasted%20image%2020230105144554.png)

O calendário possui as opções de navegação: "Anterior", "Próximo" e "Hoje". Funcionam conforme a opção de visualização marcada: "Mês", "Semana", "Dia" e "Lista".

![](./assets/Pasted%20image%2020230105144816.png)

# Área residente

## Principal

A tela principal pode ser acessada a partir do menu no cabeçalho da página.

![](./assets/Pasted%20image%2020230110082741.png)

A tela principal contém o a tabela de controle de atividades, informando cada alteração que possuem relação com a empresa ou empresas que o usuário logado possui vínculo.

![](./assets/Pasted%20image%2020230105153342.png)

A tabela aprenseta as colunas:
- Usuário que efetuou a alteração;
- A empresa ou empresas do usuário;
- A ação;
- Data de quando ocorreu.

No caso de um multiplicador, ele poderá ver todas as alterações em objetos que possuem relação com as suas empresas, incluindo os usuários, no entanto, não será informado na tabela se outro multiplicador for alterado.

Se um usuário principal acessar a tabela, ele irá visualizar todas as alterações em objetos que possuem relação com a sua empresa, incluindo os usuários.

Se um usuário normal acessar a tabela, ele irá visualizar todas as alterações em objetos que possuem relação coma sua empresa, porém no caso de usuários, somente será mostrado se ele for o usuário alterado.

A página contém um botão "exportar", em que o usuário pode optar pela exportação em pdf ou csv e todos os registros serão baixados.

## Listagem de empresas

A tela de listagem pode ser acessada pelo menu no cabeçalho da página.

![](./assets/Pasted%20image%2020230110083125.png)

![](./assets/Pasted%20image%2020230106083331.png)

A listagem de empresa apresenta todas as empresas que o usuário possui vínculo, no caso de um multiplicador pode aparecer várias empresas, já para os demais perfis (Principal e Custom), só irá aparecer uma única empresa. A única ação disponível para usuários Principal e Custom é a opção de edição.

![](./assets/Pasted%20image%2020230106085419.png)

Para o multiplicador, além da opção de edição, existe uma ação para arquivar a empresa. E caso a opção de empresas arquivadas esteja marcada, ele conseguirá desarquivar uma empresa.

![](./assets/Pasted%20image%2020230106085448.png)

![](./assets/Pasted%20image%2020230106085514.png)

## Editor de empresa

O cadastro de nova empresa poderá ser acessado na página de listagem e através do menu no cabeçalho da página:

![](./assets/Pasted%20image%2020230106090227.png)

![](./assets/Pasted%20image%2020230106090251.png)

Para editar uma empresa já existente é necessário selecionar a action na tabela.
Os campos de criação da empresa são:
- Nome (100 caracteres máximos);
- CNPJ;
- Nome fantasia (50 caracteres máximos);
- Email (254 caracteres máximos);
- Telefone 1;
- Telefone 2;
- Site (100 caracteres máximos);
- Endereço (255 caracteres máximos);
- Atividade;

![](./assets/Pasted%20image%2020230106090629.png)

## Listagem de páginas

A tela de listagem de páginas pode ser acessada pelo menu no cabeçalho da página.

![](./assets/Pasted%20image%2020230106094820.png)

A tabela de páginas irá apresentar todas as páginas que são pertencentes a empresa do usuário ou as empresas que ele possui vínculo.
As colunas são:
- Título;
- Empresa (Vísivel apenas para o multiplicador);
- Caminho da página;
- Classificação;
- Criado por;
- Estado;
- Ações;

![](./assets/Pasted%20image%2020230106095620.png)

O multiplicador terá, além das colunas citadas, mais uma coluna para empresa, uma vez que ele também poderá manipular as páginas na aplicação, e, portanto, irá conseguir gerenciar todas as páginas das empresas que possui vínculo.

![](./assets/Pasted%20image%2020230106095753.png)

A tabela possui dois modos de visualização: "Não arquivadas" e "Arquivadas". Cada coluna possui seu filtro específico.

![](./assets/Pasted%20image%2020230106100030.png)

![](./assets/Pasted%20image%2020230106100211.png)

Como ações a tabela possui as opções:
- Editar: ao inteagir o usuário é redirecionado para o editor de página;
- Clonar: ao interagir o usuário irá clonar a página, criando uma cópia não publicada contendo o mesmo conteúdo da página original;
- Arquivar ou Desarquivar: esta opção depende do modo de visualização da tabela, caso seja "Não arquivadas" o usuário poderá arquivar e caso seja "Arquivadas" o usuário poderá desarquivar;
- Publicar ou Despublicar: esta opção depende do estado da página que pode se encontrar no estado de edição, que ainda não foi publicada e não está vísivel na área pública ou publicada que pode ser visualizada por outros usuários;

![](./assets/Pasted%20image%2020230106100315.png)

## Editor de página

O cadastro de página pode ser acesado a partir do botão de listagem ou do menu do cabeçalho e a edição de uma página já existente pode ser acessada na action de edição.

![](./assets/Pasted%20image%2020230106103452.png)

![](./assets/Pasted%20image%2020230106103518.png)

Se o usuário logado for um multiplicador, ele poderá criar páginas para várias empresas, e para isso, deve selecionar para qual empresa ele quer criar uma página:

![](./assets/Pasted%20image%2020230106121246.png)

As páginas são categorizadas em dois tipos:
- Descritiva: que inclui as páginas de produto, serviço e evento;
- Raiz: página da empresa;

![](./assets/Pasted%20image%2020230106121536.png)

A opção página piloto, quando habilita, já vai abrir o editor com alguns dados pré-prenchidos para auxiliar na edição.
Assim que a página foi criada, haverá quatro opções na parte superior do editor:

![](./assets/Pasted%20image%2020230106132347.png)

- Cancelar: Caso a página seja cancelada, ela será removida;
- Preview: Quando habilitado uma janela de preview será aberta apresentando uma demonstração de como a página será publicada;

![](./assets/Pasted%20image%2020230106135506.png)

- Ajuda: Se solicitado uma janela lateral é aberta com informativos sobre o conceito e funcionamento de cada campo;

![](./assets/Pasted%20image%2020230106135532.png)

- Salvar: Utilizado para salvar as alterações em uma página de forma rápida, para que o progresso de alteração não seja perdido;

### Características do editor de página

Um campo de texto poderá ter um indicativo da quantidade atual de caracteres e quantidade máxima permitida pelo campo.

![](./assets/Pasted%20image%2020230106140031.png)

O ícone com sinal de exclamação apresenta um descritivo sobre o campo em questão.

![](./assets/Pasted%20image%2020230106140140.png)

Algumas seções podem estar desabilitadas bloqueando a interação, porém pode ser habilitado  para que ela seja de fato inserida na página.

![](./assets/Pasted%20image%2020230106140254.png)

![](./assets/Pasted%20image%2020230106140307.png)

Existem duas maneiras de prosseguir de etapas no editor, uma delas é através do botão na parte inferior: "Continuar".

![](./assets/Pasted%20image%2020230106140411.png)

Este botão sempre fará a validação da etapa atual antes de prosseguir para próxima, isso significa que se houver um campo que não esteja preenchido o avanço de etapa será bloqueado e um alerta será emitido.
Por exemplo, se a seção de imagem principal estiver habilitada, é necessário que uma imagem seja inserida, portanto, não será possível avançar de etapa pelo botão continuar até que uma imagem seja publicada.

![](./assets/Pasted%20image%2020230106140523.png)

A outra maneira de avançar de etapas é através dos índices laterais que são clicáveis. A ideia dos índices de etapas é permitir que a navegação seja mais rápida, quando uma etapa for interagida a aplicação fará a validação desde a primeira etapa, até a etapa em questão, por exemplo, se a etapa quatro chamada "Exposições" for clicada, a validação irá ocorrer desde a etapa um até a quatro.

![](./assets/Pasted%20image%2020230106140838.png)

Em caso de erro, o índice ficará com a coloração vermelha e com ícone correspondente. Além disso, uma mensagem sempre irá aparecer no canto inferior direito.

![](./assets/Pasted%20image%2020230106141005.png)

![](./assets/Pasted%20image%2020230106141025.png)

Além do botão de prosseguir, existe também um botão para retroceder as etapas quando utilizado a aplicação fará a validação desde a primeira etapa até a etapa anterior a que o usuário retornou.

![](./assets/Pasted%20image%2020230106141303.png)

Ao final de todas as etapas, haverá um botão "Confirmar" que quando interagido irá conduzir o usuário até a listagem de páginas permitindo que ele possa "Arquivar", "Editar", "Clonar" ou "Publicar" através das ações da tabela.
As seções de conteúdo, como por exemplo, a seção de mídias sociais, funcionam de forma muito semelhante entre elas: 
- Pode possuir um habilitador de seção, que em caso negativo, bloqueia a interação de criação dos itens e em caso afirmativo, irá alocar a seção em questão para a página.

![](./assets/Pasted%20image%2020230106141638.png)

- Botão de criação, quando disparado abre uma janela com os campos de entrada para adicionar um novo item a seção. 

![](./assets/Pasted%20image%2020230106141740.png)

![](./assets/Pasted%20image%2020230106141753.png)

- Os itens são mostrado uma tabela e podem ser ordenados se um item for pressionado e arrastado.

![](./assets/Pasted%20image%2020230106141932.png)

- Cada item pode ser editado ou removido, em edição uma janela será aberta contendo os dados de cadastro e em caso de remoção um alerta irá solicitar a confirmação para que de fato o item seja removido.

![](./assets/Pasted%20image%2020230106142019.png)

![](./assets/Pasted%20image%2020230106142034.png)

Na etapa de informações gerais, há um editor de texto: "Conteúdo", através deste editor que o conteúdo da página será elaborado.

![](./assets/Pasted%20image%2020230106143706.png)

Ele implementa até três níveis de títulos e texto normal.

![](./assets/Pasted%20image%2020230106143653.png)

As opções de formatação variam entre negrito e itálico.

![](./assets/Pasted%20image%2020230106143848.png)

Possui dois tipos de listas: pontos e numerada.

![](./assets/Pasted%20image%2020230106143909.png)

Os botões de indentação permitem que um sub-lista exista dentro de uma outra lista.

![](./assets/Pasted%20image%2020230106144210.png)

Existe um botão que permite anexar endereço de página à um texto.

![](./assets/Pasted%20image%2020230106144034.png)

É possível anexar imagens no editor, atente-se para que a imagem tenha até no máximo 10MB e que ela esteja em alguns dos formatos: jpg, png e jpeg.

![](./assets/Pasted%20image%2020230106151327.png)

O editor implementa a opção de criar citações no conteúdo, através deste botão:

![](./assets/Pasted%20image%2020230106151537.png)

É possível, também, criar tabelas informando a quantidade de linhas e colunas.

![](./assets/Pasted%20image%2020230106151604.png)

Caso seja necessário anexar conteúdos de media, é possível inserir uma URL que irá embedar o conteúdo na página.

![](./assets/Pasted%20image%2020230106151642.png)

### Campos

#### Títulos e Sub-títulos

Campos de texto com 100 caracteres máximos e 3 caracterees mínimos.

#### Endereço de página

Endereço pelo qual a página será publicada. Os padrões dependem do tipo de página:
- Empresa: `/<Nome Fantasia da empresa>/<Endereço da página>/`;
- Serviço: `/<Nome Fantasia da empresa>/servicos/<Endereço da página>/`;
- Produto: `/<Nome Fantasia da empresa>/produtos/<Endereço da página>/`;
- Evento: `/<Nome Fantasia da empresa>/eventos/<Endereço da página>/`;
É recomendado que seja evitado endereços longos, com nomes genéricos, com palavras-chave em excesso ou com repetições, utilize um endereço amigável para o usuário, isso fará com que a página seja mais facilmente encontrada.

#### Conteúdo da página

Texto que irá o compor o conteúdo da página. É recomendado que seja utilizado as opções de formatação para uma leitura mais confortável. Utilize a hierarquia de títulos de maneira correta, este é um fator muito importante para mecanismos de busca.

#### Imagem principal

Esta imagem será utilizada como um banner, identificada abaixo do título e subtítulo na página principal de sua empresa.

#### Formulário de Lead

Ao habilitar o formulário de Lead será disponibilizado um formulário na parte inferior da página para que outras pessoas consigam entrar em contato com a empresa através do mensageiro whatsapp, e, portanto, é necessário que o criador da página especifique qual o número da empresa que será utilizado para o lead.

#### Título da pesquisa

Esse será o título de busca ao ser pesquisado pelo usuário na página de busca.
Utilize um título sucinto e que indique corretamenta o conteúdo da página. Crie títulos exclusivos para cada página. Use títulos breves, mas descritivos.

#### Logos

Composto por três campos de imagens que serão utilizadas nos resultados de pesquisa do usuário. Os tamanhos são:
- Grande - 160x160px; 
- Média - 65x65px;
- Pequena - 35x35px.
É possível utilizar imagens diferentes para as resoluções, mas normalmente é utilizada a mesma imagem.

#### Tipo de visualização da busca

Existem duas opções para a busca:
- Sumário: Uma breve descrição da página (de 125 a 355 caracteres);
- Destaques: São cartões de destaque que apresentam um título e valor.;

#### Palavras-chave

Serão as "tags" que facilitará o usuário a encontrar a página em ferramentas de pesquisa. É recomendado que seja colocado palavras que façam sentido com o conteúdo da página.

#### Descrição SEO

Informação descritiva que será encontrado por outros usuários que realizarem pesquisas no Google. Esta descrição fornece ao google e a outros mecanismos de pesquisa um resumo do assunto da página, e, portanto, deve ser resumido com precisão, evitando informações desconexas com o conteúdo ou trechos muito genéricos, além disso, é importante que a descrição da página não possuam trechos copiados diretamente do conteúdo da página.  

#### Título da página SEO

Este é o título da página que irá aparecer no navegador e também pode ser utilizado como título de resultado de pesquisas feito por outros mecanismos de busca.

#### Seção de números

A seção de números pode ser utilizado para adicionar estatísticas na página.

![](./assets/Pasted%20image%2020230106164030.png)

O campo de mensagem altera a informação textual abaixo dos números.
Para criar o número é necessário especificar:
- Descrição (3-35 caracteres);
- Cor (RGB);
- Ícone (Font Awesome);
- Valor (1-4 caracteres);
- Unidade (8 caracteres);
O recomendado é que se utilize 3 ou 4 números;

#### Seção de destaques

Pode ser utilizado para adicionar destaques, conquistas, benefícios ou valores, em geral, informações que devem ficar destacadas da página.

![](./assets/Pasted%20image%2020230106165014.png)

O título (3-75 caracteres) e sub-título (3-200 caracteres) pode ser alterado.
Para criar o destaque é necessário especificar:
- Ícone (Font Awesome);
- Título (3-45 caracteres);
- Sub-Título (100-225 caracteres);
- Cor (RGB);

#### Seção de produtos

Pode ser utilizado para adicionar produtos à página.

![](./assets/Pasted%20image%2020230109084111.png)

O Título "Produtos" pode ser customizado com uma descrição com até 100 caracteres.
Para criar um item de produto é necessário especificar:
- Página de produto publicada para ser vinculada;

#### Seção de serviços

Pode ser utilizado para adicionar serviços à página.

![](./assets/Pasted%20image%2020230109085215.png)

O Título "Serviços" pode ser customizado com uma descrição com até 100 caracteres.
Para criar um item de serviço é necessário especificar:
- Página de serviço publicada para ser vinculada;

#### Mesclar as seções de produto e serviço

As seções de produto e serviços podem ser mescladas e ter seu título alterado por uma mensagem com até 100 caracteres.

![](./assets/Pasted%20image%2020230109085714.png)

![](./assets/Pasted%20image%2020230109085935.png)

#### Seção de mídias sociais

Pode ser utilizado para divulgar as mídias sociais da empresa.

![](./assets/Pasted%20image%2020230109090220.png)

Para criar um item de mídia social é necessário especificar:
- O endereço completo da página;
- O ícone da logo da mídia social;

#### Seção de funcionalidades

Pode ser utilizado para divulgar as funcionalidades de um produto.

![](./assets/Pasted%20image%2020230109093621.png)

O Título pode ser customizado por uma mensagem com até 100 caracteres.
Para criar uma funcionalidade é necessário especificar:
- Título (3-35 caracteres);
- Ícone (Font Awesome);
- Descrição (120-335 caracteres);

#### Seção de resultados

Pode ser utilizado para divulgar os resultados de um serviço.

![](./assets/Pasted%20image%2020230109093719.png)

O Título pode ser customizado por uma mensagem com até 100 caracteres.
Para criar um resultado é necessário especificar:
- Mensagem descritiva do resultado (3-35 caracteres);
- Ícone (Font Awesome);
- Número (1-4 caracteres);
- Unidade (8 caracteres);

#### Seção de imagens

Pode ser utilizado para apresentar imagens referente ao conteúdo da página.

![](./assets/Pasted%20image%2020230109094631.png)

O Título pode ser customizado por uma mensagem com até 100 caracteres.
Para criar uma imagem é necessário especificar:
- Imagem (Max: 10MB, Formatos: jpeg, png, jpg);
- Título (3-40 caracteres);
- Descrição (100-200 caracteres);

#### Seção de convidados

Pode ser utilizado para apresentar os convidados de um evento.

![](./assets/Pasted%20image%2020230109095336.png)

O Título pode ser customizado por uma mensagem com até 100 caracteres.
Para criar um apresentador é necessário especificar:
- Nome (3-35 caracteres);
- Imagem (Max: 10MB, Formatos: jpeg, png, jpg);
- Cargo (3-35 caracteres);

## Listagem de eventos

A tela de listagem de eventos pode ser acessada pelo menu no cabeçalho da página.

![](./assets/Pasted%20image%2020230110093324.png)

A tela de listagem de eventos apresenta em uma tabela todos os eventos da empresa ou empresas que o usuário possui vínculo. Os campos informados são: Nome do Evento; Local; Tipo; Início e Fim.

![](./assets/Pasted%20image%2020230109100242.png)

As possíveis actions são:
- Edição: redireciona para o editor de um evento já existente;
- Arquivar ou desarquivar: alterna o estado de arquivado do evento;
- Visualizar: redireciona para o calendário de eventos;
As modos de visualização alternam entre:
- Não arquivados;
- Arquivados;

## Editor de evento

A tela de criação de eventos pode ser acessada a partir do menu no cabeçalho ou do botão "adicionar" presente na listagem.

![](./assets/Pasted%20image%2020230109122600.png)

![](./assets/Pasted%20image%2020230109122618.png)

![](./assets/Pasted%20image%2020230109130134.png)

Para criar um evento é necessário determinar: 
- Título (100 caracteres);
- Descrição (255 caracteres);
- Localização (255 caracteres);
- Data;
- Horário Inicial;
- Horário Final;
- Página de evento;
- Tipo de evento;
O tipo de evento varia entre interno e externo:
- Interno: apenas usuários do BPK Search poderão visualizar o evento;
- Externo: todos os usuários do BPK Search irão visualizar o evento;
Para publicar uma página de evento é necessário acessar o editor de evento para vincular a página à um evento.
Uma página pode conter vários eventos vinculados, no entanto, será mostrado na pesquisa o evento futuro vinculado.

## Listagem de usuários

Esta tela pode ser acessada a partir do menu no cabeçalho.

![](./assets/Pasted%20image%2020230109125450.png)

A tela de listagem de usuários apresenta em uma tabela todos os usuários que possuem relação com a empresa que o usuário tem vínculo. Contudo, a lista de usuário muda conforme o perfil do usuário logado:
- Multiplicador: para este será informado todos os usuários principais das empresas que possui vínculo.
- Principal: para este será informado todos os usuários principais e custom da empresa que possui vínculo.
- Custom: para este será informado todos os usuários principais e custom da empresa que possui vínculo.

![](./assets/Pasted%20image%2020230109125410.png)

Esta tabela possui como colunas:
- Usuário (Nome e Email);
- Empresa;
- Cargo;
- Telefone;
- Ações;
As ações são constituidas por:
- Edição;
- Arquivar e Desarquivar;
A tabela possui os modos de visualização:
- Não arquivados;
- Arquivados;

## Editor de usuário

A tela de criação de usuários pode ser acessada a partir do menu no cabeçalho ou do botão "adicionar" presenta na listagem. Também é possível acessar o editor de usuário através da action de edição de um usuário já existente.

![](./assets/Pasted%20image%2020230109130025.png)

![](./assets/Pasted%20image%2020230109130039.png)

O editor de usuários é constituído por duas etapas, a de informações gerais e a de permissões.

![](./assets/Pasted%20image%2020230109130209.png)

Na etapa de informações gerais é necessário cadastradar os campos:
- Nome (150 caracteres máximos);
- Sobrenome (150 caracteres máximos);
- Email (255 caracteres máximos);
- Celular (+00 (00) 00000-0000);
- Username (150 caracteres máximos);
- Empresa (As opções dependem da role do usuário logado);
No campo de empresa as opções serão, no caso de um multiplicador criando um usuário principal, as opções de empresas que ele possui vínculo, já para o perfil de usuário principal, irá mostrar apena a empresa que ele possui vínculo.

![](./assets/Pasted%20image%2020230109130532.png)

Na etapa de permissões será necessário cadastrar:
- O tipo de usuário;
- As permissões de usuário;
No caso de um multiplicador o tipo de usuário é restrito apenas a usuários principais, já para os usuários principais será restrito apenas a usuários custom.

## Quadro de notificações

Esta tela pode ser acessada a partir do menu ou da janela de notificação.

![](./assets/Pasted%20image%2020230109130737.png)

![](./assets/Pasted%20image%2020230109130752.png)

O quadro de notificação apresenta em uma tabela todas as notificações que o usuário possui relação, sendo este o remetente ou o destinatário.
No caso do remetente, apenas o multiplicador poderá ocupar esta posição e para este perfil a tabela terá as colunas:
- Remetente;
- Título da notificação;
- Data de envio;
- Destinatários (Empresas);
- Ações;
A única ação disponível para o remetente é ver o detalhes da notificação.

![](./assets/Pasted%20image%2020230109131902.png)

No detalhes da notificação é informado o título, a data de envio, o remetente, a mensagem e também informa quais usuários já visualizaram a notificação e quais deixaram de ver.
Para os usuários principais e custom que possuem permissão para visualizar notificação a tabela irá mostrar as colunas:
- Remetente;
- Título;
- Data de envio;
- Status (Não visualizado e visualizado);
- Ações;
A única ação disponível para o destinatário é a opção de visualizar notificação.

![](./assets/Pasted%20image%2020230109135305.png)

Assim que a notificação for aberta ela será marcada como visualizada.

## Editor de notificação

Esta tela pode ser acessada pelo menu do cabeçalho e pelo quadro de notificação quando o usuário for um multiplicador.

![](./assets/Pasted%20image%2020230109135519.png)

![](./assets/Pasted%20image%2020230109135541.png)

Para adicionar uma nova notificação, o remetente deverá especificar as empresas que são destinatárias, o título da notificação e a descrição, caso seja necessário, ele também colocar um arquivo em anexo, o tamanho deste arquivo não pode ultrapassar 10MB.

![](./assets/Pasted%20image%2020230109140516.png)

Na opção de destinatários também é possível utilizar filtros rápidos com base na atividade da empresa:
- Agro;
- Comércio;
- Edução;
- Indústria;
- Prestação de serviços;
- Saúde;
- Tecnologia;
E também poderá utilizar a opção "todos", marcando todas as empresas como destinatários.

## Listagem de contatos

Esta tela pode ser acessada a partir do menu do cabeçalho, quando o usuário não for multiplicador e quando possuir permissão para acessar os contatos.

![](./assets/Pasted%20image%2020230109142129.png)

A listagem de contatos apresenta todos os lead que entraram em contato pelas páginas da empresa que o usuário possui vínculo.
A tabela informa as colunas:
- Data de envio;
- Nome;
- Telefone;

![](./assets/Pasted%20image%2020230109144757.png)

A tabela contém uma opção de exportação para os arquivos CSV e PDF.
Qualquer usuário do BPK Search pode fazer um lead, independente do login, basta apenas que a página tenha o formulário de lead habilitado com um número de telefone marcado no editor de página.

![](./assets/Pasted%20image%2020230109152435.png)

Após ter configurado a página, o formulário de lead será renderizado e o usuário poderá inserir seu nome e telefone, após a solicitação o usuário irá ser redirecionado para o whatsapp.

![](./assets/Pasted%20image%2020230109152501.png)

![](./assets/Pasted%20image%2020230109152616.png)
