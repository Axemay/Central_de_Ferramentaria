<h1>Sistema de controle de reservas de ferramentas</h1>

<p>Projeto em grupo proposto como requisito para aquisição da certificação do Mundo 1, na graduação tecnológica de Desenvolvimento Full Stack da Universidade Estácio de Sá</p>

![image](https://user-images.githubusercontent.com/101254285/189240709-26cb29ea-613b-4297-b29b-efcd80ff3b35.png)

<h3>Link do vídeo: <a href="https://youtu.be/izh7uXpsDB4">https://youtu.be/izh7uXpsDB4<a></h3>

<p>Grupo: DevTeam13</p>
<p>Participantes:</p>
<ul>
<li><a href="https://github.com/Axemay">Maiara Accacio Machado</a> - 202204268183</li>
<li><a href="https://github.com/fneto1723">Francisco Ferreira de Queiroz Neto</a> - 202205164951</li>
<li><a href="https://github.com/dpsndroid">Daniel Portella de Souza Nepomuceno</a> - 202205063186</li>
<li><a href="https://github.com/Rafa1a">Rafael Leal Altero</a> - 202205021882</li>
</ul>

<h2>Objetivo da missão de certificação do Mundo 1</h2>
<p>Desenvolver uma aplicação para gerenciamento de equipamentos em um ambiente de preparação de conteúdo audiovisual voltado para educação.</p>

<h3>Bibliotecas e módulos utilizados</h3>
<ul>
<li>csv -> DictWriter, DictReader, writer, reader</li>
<li>datetime -> date, time, datetime, timedelta</li>
<li>openpyxl</li>
<li>os</li>
<li>pandas</li>
<li>pathlib</li>
<li>re</li>
<li>time -> strptime</li>
<li>tkcalendar -> Calendar</li>
<li>tkinter -> END, Frame, ttk, Scrollbar, messagebox -> askyesno</li>
<li>typing -> Dict</li>
<li>webbrowser</li>
</ul>

<h3>Central de Ferramentaria</h3>
<p>Na tela inicial, o usuário poderá abrir o manual de uso do sistema.</p>

![image](https://user-images.githubusercontent.com/101254285/189252464-ac454e23-ebff-4b6a-b1bc-73a34457cb11.png)


<p>No cadastro de técnico, o CPF é validado pelo dígito não aceitando números inválidos e outros caracteres.</p>

![image](https://user-images.githubusercontent.com/101254285/189253044-f5e18e66-f6eb-486e-8d7d-2ff520de62c3.png)


<p>O código da ferramenta é gerada automaticamente a cada novo cadastro. Além disso, cada ferramenta é cadasta com um tempo máximo permitido para sua reserva</p>
![image](https://user-images.githubusercontent.com/101254285/189254010-4e481dde-1ff6-4ab8-9d1d-bbb3f69dca95.png)



<p>As ferramentas precisam ser reservadas com até 24 horas de antecedência. O sistema verifica se a ferramenta estará disponível no período solicitado e apenas permitirá a reserva em caso positivo. Além disso, o sistema irá bloquear reservas por período superior ao permitido para cada ferramenta.

![image](https://user-images.githubusercontent.com/101254285/189255801-d53a3ba0-1f8d-4161-accf-db4ae656bbce.png)


<p>Técnicos, Ferramentas e reservas podem ser removidos.</p>

![image](https://user-images.githubusercontent.com/101254285/189255959-7f550536-e3fb-4e01-8d33-dbdea6e2ed35.png)




