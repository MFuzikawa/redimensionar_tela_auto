# Redimensionador de navegador
## Objetivo
criar um executavel que monitora meu navegador, quando a tela muda de resolução o navegador se centraliza sozinho

## Problema a resolver
quando abro um programa em tela cheia o navegador na segunda tela se evade da tela e fica cortada

## tecnologias utilizadas
Python
usei as bibliotecas pyinstaller, pyautogui, pygetwindow

## minhas solução
O script que desenvolvi age como um "vigilante" ele constantemente checa se a janela do Opera GX foi movida ou redimensionada e
 se isso acontecer, ele a força a voltar para a posição correta e a redimensiona.

 ## como o Script Funciona na Prática
Monitoramento: O script roda em segundo plano. A cada poucos segundos (time.sleep(10)), 
ele verifica a posição e o tamanho da janela do Opera GX.

Detecção de Mudança: Ele compara a posição e o tamanho atuais da janela com os que deveriam
estar na sua segunda tela (os valores de x, y, w e h que ele obteve no início).

Correção Automática: Se ele detectar que a janela não está onde deveria, ele aciona a função de reposicionamento (reposicionar_opera_segunda_tela)
para movê-la e redimensioná-la instantaneamente.

## como usá-lo em seu computador

O que você vai precisar
Dois monitores configurados no seu computador.

O Opera GX instalado.

Acesso à internet para baixar o aplicativo.

Passo 1: Baixar o Aplicativo
Copie o repositorio do github

na pasta da aplicação vc encontrará uma pasta chamada build dentro dela um arquivo chamado Application.exe 
Salve-o em uma pasta que você possa encontrar facilmente, como a sua área de trabalho ou a pasta Documentos.

Passo 2: Usar o Aplicativo
É muito simples. Basta dar um duplo clique no arquivo .exe que você baixou.

O aplicativo vai começar a rodar em segundo plano, monitorando a janela do Opera GX.

Se a janela do Opera GX for movida ou redimensionada, o aplicativo a forçará a voltar para a segunda tela.

Para verificar se o aplicativo está rodando, abra o Gerenciador de Tarefas (Ctrl + Shift + Esc) e procure por Application.exe na lista de processos.

Passo 3: Parar o Aplicativo
Para parar o monitoramento, basta fechar o processo no Gerenciador de Tarefas:

Abra o Gerenciador de Tarefas (Ctrl + Shift + Esc).

Procure por monitora_opera.exe na lista de processos.

Clique com o botão direito do mouse sobre ele e selecione Finalizar tarefa.

O aplicativo será encerrado, e a janela do Opera GX não será mais monitorada.
