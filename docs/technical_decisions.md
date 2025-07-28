# Decisões técnicas - documentação  

## Tecnologia  

Todas as tecnologias foram escolhidas para cumprir o desafio. Porém, foram utilizadas por possuírem ferramentas que se integram bem e possibilitam a construção de uma aplicação eficiente e desenvolvida de forma rápida. As tecnologias utilizadas foram:  

- **Python**: A linguagem possui diversas bibliotecas úteis que auxiliam no desenvolvimento de sistemas que demandam múltiplos recursos, como por exemplo cálculos complexos, leitura de PDFs, leitura de imagens, inteligência artificial, entre outros. Tendo isso em vista, foram utilizados os seguintes módulos neste projeto:  
    - **ast**: Este módulo do *Python* permite criar uma árvore de sintaxe abstrata, que serve para analisar, modificar e interpretar códigos, abstraídos em uma árvore que pode ou não ter mais de um nó. Dessa forma, foi possível construir a hierarquia presente na matemática de forma rápida e prática.  
    - **operator**: Este módulo foi utilizado para complementar o módulo **ast**, pois possui funções que representam operadores matemáticos e lógicos, transformando operadores em funções.  

- **Django**: O framework oferece segurança e facilidade para o desenvolvimento. Além disso, possui diversas funcionalidades que permitem a construção de um projeto com **Front End** e **Back End**, funcionando da seguinte maneira:  
    - **MVT**: Utiliza a arquitetura *Model View Template*, que facilita a comunicação entre os componentes da aplicação, sendo esta uma aplicação *Full Stack*, contando tanto com Front End (*Templates*) quanto com Back End (*Views* e *Models*).  

    - **Templates**: Aqui foi desenvolvida toda a parte do Front End, com templates dinâmicos e devidamente organizados. O Django Template permite aplicar lógica de programação utilizando HTML, além de renderizar estilizações tanto da aplicação quanto externas. Neste projeto, foi utilizado como base um template fornecido para o desafio, além de **scripts** em **JavaScript** que auxiliaram a complementar funcionalidades que poderiam ser limitadas sem eles. Além disso, foram utilizadas estilizações pensando na praticidade, e **django messages** configuradas no próprio framework.  

    - **Views**: Nas *views* é feita a comunicação com o banco de dados (*Django ORM*), sendo responsável por toda a lógica do sistema, incluindo:  
        - **Registrar Operações**: Utiliza o *Django ORM* para registrar as operações recebidas na *Request* proveniente dos *Templates*.  
        - **Realizar Cálculo**: Na *view* é feita a comunicação com a classe **Calc**, desenvolvida com o intuito de receber uma operação e realizar o cálculo, retornando somente o *resultado* da operação.  
        - **Tratamento de erro**: Na *view* é realizado o tratamento de erros que podem ocorrer durante essas operações. Foi feito um mapeamento durante o desenvolvimento para que esses erros fossem alertados ao usuário quando ocorressem.  
        - **Class Based Views**: Foi utilizada para garantir uma estrutura mais modular, fácil de testar e manter, além de oferecer recursos que facilitam o desenvolvimento como um todo.  

    - **Tests**: Oferece um sistema de testes integrado ao framework, baseado no *Unittest*, mas com recursos adicionais. Foi utilizado *Pytest* como *Test Runner* da aplicação, e para os testes foi utilizado o **TestCase** do framework, que herda diretamente de *Unittest*, porém com funcionalidades adicionais.  

    - **Admin**: O framework inclui um painel administrativo que auxilia significativamente no desenvolvimento, permitindo interagir diretamente com os *models*. Nesta aplicação, foi utilizado tanto para acompanhar o desenvolvimento quanto para visualizar a criação dos objetos. O painel foi personalizado para ser mais intuitivo aos desenvolvedores, incluindo paginação e ordenação de campos.  

- **SQLite**: Foi utilizado para cumprir o desafio, além de possuir ótima integração com o framework **Django** e ser prático para o desenvolvimento.