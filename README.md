# **PROJETO-Hamburgueria**  

[![Django Version](https://img.shields.io/badge/Django-5.1.4-green)](https://www.djangoproject.com/) [![Python Version](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)  

Uma plataforma completa para pedidos online em uma hamburgueria, desenvolvida em **Python** com o framework **Django**.  
O projeto oferece:  
- Uma **landing page** intuitiva para apresentar o cardápio e atrair clientes.  
- Funcionalidade para **realizar pedidos online** diretamente no site.  
- **Pagamento online** integrado para facilitar a transação.  
- **Acompanhamento de pedidos** em tempo real para os clientes.  

---

## **Tabela de Conteúdo**

1. [Recursos](#recursos)  
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)  
3. [Instalação](#instalação)  
4. [Uso](#uso)  
5. [Contribuição](#contribuição)  
6. [Licença](#licença)  

---

## **Recursos**  

### **Landing Page**  
- Apresentação do cardápio da hamburgueria de forma atraente e interativa.  
- Design focado na experiência do usuário e na conversão de visitantes em clientes.  

### **Pedidos Online**  
- **Escolha de produtos**: O cliente pode adicionar itens ao carrinho e personalizar o pedido.  
- **Pagamento Online**: Integração com sistemas de pagamento para realizar transações de forma segura.  

### **Acompanhamento de Pedido**  
- Os clientes podem visualizar o status do pedido em tempo real, garantindo transparência e confiança.  

---

## **Tecnologias Utilizadas**  

- **Frontend:** HTML, CSS, JavaScript.  
- **Backend:** Django 5.1.4, Python 3.11.  
- **Banco de Dados:** SQLite (configuração padrão, personalizável).  
- **Bibliotecas e Dependências:**  
  - [asgiref](https://pypi.org/project/asgiref/) para compatibilidade assíncrona.  
  - [sqlparse](https://buildmedia.readthedocs.org/media/pdf/sqlparse/latest/sqlparse.pdf) para análise e formatação de SQL.  

---

## **Instalação**  

### **Pré-requisitos**  
- Python 3.11 ou superior.  
- Pip instalado.  

### **Passos para Instalação**  
1. Clone o repositório:  
   ```bash
   git clone https://github.com/Marcos-VRS/PROJETO-Hamburgueria.git
   cd PROJETO-Hamburgueria
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv  
   source venv/bin/activate  # Linux/Mac  
   venv\Scripts\activate     # Windows
3. Instal as dependências:
   ```bash
   pip install -r requirements.txt  
4. Execute as migrações:
   ```bash
   python manage.py migrate  
5. Inicie o servidor:
   ```bash
   python manage.py runserver

---

## **Uso**
-Acesse a plataforma na URL: http://127.0.0.1:8000/.
-Navegue pelo cardápio e adicione produtos ao carrinho.
-Realize o pagamento através do sistema integrado.
-Acompanhe o status do seu pedido em tempo real.

---

## **Contribuição**
Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do repositório.
2. Crie uma branch com sua funcionalidade ou correção:
   ```bash
   git checkout -b minha-contribuicao  
3. Envie um Pull Request para revisão

---

## **Licença**
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


---

## **Contato**
•Desenvolvedor: Marcos-VRS
•Email: marcosvrsdevmail@gmail.com
•LinkedIn: https://www.linkedin.com/in/marcos-vin%C3%ADcius-ramos-da-silva-557b18a5/

