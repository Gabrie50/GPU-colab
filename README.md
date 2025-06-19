# GPU-colab

Projeto para criar um cluster híbrido usando Binder como frontend e Google Colab como backend com GPU grátis.

## Como usar

### No Google Colab

1. Abra o notebook `scripts/colab_setup.ipynb` no Google Colab.
2. Execute todas as células para instalar JupyterLab e abrir o túnel via Cloudflared.
3. Copie o link gerado (exemplo: `https://trycloudflare.com/abc123`).

### No Binder

1. Abra o Binder apontando para este repositório.
2. Abra o notebook `notebooks/controle_remoto.ipynb`.
3. Altere o hostname para o link copiado do Colab (sem o `https://`).
4. Ajuste username e password conforme sua configuração no Colab.
5. Rode as células para conectar e executar comandos remotamente na GPU do Colab.

## Arquivos

- `/binder` : configurações do ambiente Binder.
- `/scripts` : scripts para rodar no Colab.
- `/notebooks` : notebook para controle remoto.