# Apollo Book Generation

Aplicação web em Python com front-end HTML e microserviços em Flask. Permite cadastro e login de usuários, upload de arquivos CSV e geração de dashboards com gráficos e tabelas. Cada dashboard salvo aparece no painel lateral esquerdo para rápido acesso.

## Estrutura

```
Apollo-Book-Generation/
├── app.py
├── extensions.py
├── auth_service/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── dashboard_service/
│   ├── __init__.py
│   ├── analytics.py
│   ├── models.py
│   └── routes.py
├── templates/
├── static/
└── requirements.txt
```

## Execução local

1. Instale as dependências com `pip install -r requirements.txt`.
2. Inicie o aplicativo executando `python app.py`.
3. Acesse `http://localhost:5000` no navegador.

Os dados são armazenados em um banco SQLite (`app.db`) criado automaticamente.
