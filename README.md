<h1>Sistema de controle de reservas de ferramentas</h1>

<p>Projeto em grupo proposto como requisito para aquisição da certificação do Mundo 1, na graduação tecnológica de Desenvolvimento Full Stack da Universidade Estácio de Sá</p>
<hr>
<p>Grupo: DevTeam13</p>
<p>Participantes:</p>
<ul>
<li>Maiara Accacio Machado</li>
<li>Francisco Ferreira de Queiroz Neto</li>
<li>Daniel</li>
<li>Paulo</li>
<li>Rafael</li>
</ul>

<h2>Objetivo da missão de certificação do Mundo 1</h2>
<p>Desenvolver uma aplicação para gerenciamento de equipamentos em um ambiente de preparação de conteúdo audiovisual voltado para educação.</p>

<h3>Regras de negócio</h3>

<p>As ferramentas precisam ser reservadas com até 24 horas de antecedência. Reservas de emergência são também possíveis e, para isso, a central de ferramentaria não pode ficar sem algumas ferramentas mais críticas no estoque. Ferramentas críticas são ferramentas necessárias para manutenção de equipamentos e/ou instalações que possam apresentar algum risco de segurança para os trabalhadores em caso de problema. Em uma planta industrial a segurança é sempre a maior prioridade.</p>

<p>As solicitações de reserva precisam ser enviadas por email para o responsável pela Central de Ferramentaria, indicando o código da ferramenta (código interno e que identifica de forma única a ferramenta), sua descrição, data e hora da retirada, data e hora prevista de devolução e o técnico responsável (nome completo do técnico) pela retirada.</p>

<p>O uso das ferramentas precisa ser otimizado ao máximo, pois estoque em excesso representa custo para a empresa. Desta forma, é muito importante que os técnicos sempre informem a data e hora prevista da devolução, para que ela possa ficar à disposição para uso por um outro técnico.</p>

<p>Cada ferramenta precisa ter um tempo máximo permitido para sua reserva (horas, dias, ...) auxiliando o responsável pela Central de Ferramentaria no combate ao uso inadequado das ferramentas e na otimização do seu estoque. Cada ferramenta deve ter as seguintes informações associadas:

<ul>
<li>Código sequencial interno da ferramenta (código gerado de forma automática pelo sistema)</li>
<li>Descrição da Ferramenta. Texto livre contendo as principais informações de identificação</li>
<li>Fabricante (texto livre)</li>
<li>Voltagem de uso (texto livre)</li>
<li>Part Number (número que identifica a ferramenta no fabricante)</li>
<li>Tamanho</li>
<li>Unidade de Medida (cm, polegadas, metros, ...)</li>
<li>Tipo da Ferramenta (elétrica, mecânica, segurança, ...)</li>
<li>Material da ferramenta (ferro, madeira, plástico, borracha, ...)</li>
<li>Tempo máximo de reserva (horas)</li>
</ul>


<p>Todos os técnicos precisam estar cadastrados no sistema pois eles precisarão ser facilmente identificados e contatados em caso de atraso na devolução da ferramenta. Cada técnico deve ter as seguintes informações associadas:

<ul>
<li>CPF (deve ter o digito verificador validado)</li>
<li>Nome (texto livre)</li>
<li>Telefone celular ou rádio (9 dígitos para celular ou até 8 dígitos para rádio)</li>
<li>Turno (manhã, tarde ou noite)</li>
<li>Nome da esquipe (texto livre)</li>
</ul>

<p>Tanto técnico como ferramenta podem ser excluídos do cadastro quando necessário.</p>

<hr>
<h3>Reserva de ferramentas - Entrega bônus</h3>
<p>Ao reservar uma ferramenta, ela deve ficar associada ao técnico responsável pela sua retirada e devolução.</p>
<p>O responsável pela Central de Ferramentaria deve poder consultar com quem as ferramentas estão (após a sua retirada) e qual a previsão de devolução para que possa controlar algum eventual atraso. </p>
<p>Uma ferramenta só pode ser reservada se ela estiver disponível na data e hora prevista para a retirada. </p>



