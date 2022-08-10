# Git

Para mostrar a branch que você esta no terminal do linux/wsl precisa fazer uma alteração no arquivo .bashrc

```bash
# Show git branch name
force_color_prompt=yes
color_prompt=yes
parse_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
if [ "$color_prompt" = yes ]; then
 PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;31m\]$(parse_git_branch)\[\033[00m\]\$ '
else
 PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w$(parse_git_branch)\$ '
fi
unset color_prompt force_color_prompt
```

O primeiro comando a ser executado para inicializar o git no diretório atual

```
git init
```

Um dos comandos mais utilizados é o 

```
git status
```

Com esse comando podemos ver em qual branch estamos e se tem alguma arquivo para ser adicionado ao stage ou commitado

Para configurar o nome do usuário e o email que irá aparecer no git é só usar os seguintes comandos

```
git config --local user.name "Guilherme"
git config --local user.email "guifl_pereira@hotmail.com"
```

Pode usar tanto a flag —local para definir as configurações apenas para aquele diretório, ou a flag —global, para definir de forma global para seu git. Para verificar as informações o comando é bem similar

```
git config user.name
git config user.email
```

Para commitar as mudanças adicionadas no stage usamos o seguinte comando

```
git commit -m "Mensagem descritiva do commit aqui"
```

Para verificar o histórico de commits é só usar o comando

```
git log   # essa forma mostra quem fez os commits, as hashs, data e hora do commit e o mensagem
git log --oneline   # forma mais simples, mostra apenas o começo da hash e a mensagem de commit
git log -p    # forma mais completa, apresenta também as alteração no arquivo
```

Existem várias formas de usar o git log, o site [git log cheatsheet (devhints.io)](https://devhints.io/git-log) contém algumas opções para personalizar a exibição do log

Caso existam arquivos/pastas que não queremos que o git monitore podemos adicionar o nome desses arquivos/pastas em um arquivo chamado .gitignore

Podemos criar um repositório servir de servidor local/offline para cirar esse diretório que irá conter apenas as alterações dos arquivos usamos

```
git init --bare
```

Precisamos avisar nosso repositório local da existência desse servido, para isso vamos utilizar

```
git remote add apelido_que_eu_quero_escolher_para_o_servidor caminho_para_o_servidor
git remote add local /mnt/e/OneDrive/Alura/git/servidor   # exemplo
git remote   # lista os repositórios remotos que nosso repositório atual conhece
git remote -v  # lista o caminho para os repositório remotos que nosso repositório atual conhece
```

Para copiar os arquivos de um repositório que queremos trabalhar precisamos clonar esse repositório

```
git clone caminho_para_o_repositório nome_que_eu_quero_que_o_clone_tenha_na_minha_maquina
git clone /mnt/e/OneDrive/Alura/git/servidor projeto    # exemplo
```

Caso o servidor estiver vazio, o novo diretório será criado vazio também. Isso também adiciona o caminho que utilizamos como repositório remoto, esse repositório tem o nome de origin. Para alterar o nome do repositório remoto utilizamos

```
git remote rename nome_já_existente novo_nome
git remote rename origin local   # exemplo
```

Para enviar os arquivos para o servidor basta digitar

```
git push nome_do_repositório_remoto nome_da_branch_que_quero_enviar
git push local master   # exemplo
```

Caso já clonamos um repositório e queremos buscar as atualização precisamos usar

```
git pull nome_do_repositório_remoto nome_da_branch_que_quero_buscar
git pull local master
```

Para usar o GitHub basta entrar no site do GitHub, criar um novo repositório, colocar o nome, a descrição, e se ele vai ser publico ou privado e então criar. Já para adicionar esse repositório como nosso servidor precisamos fazer o seguinte

```
git remote add apelido_que_eu_quero_escolher_para_o_servidor caminho_para_o_servidor
git remote add origin git@github.com:GuiFerreira11/alura.git  # exemplo de adição usando o ssh
git remote add origin https://github.com/GuiFerreira11/alura.git # exemplo de adição usando o https
git branch -M main   # atualmente é mais comum utilizar o nome main do que master para a branch principal, mas isso é opcional
git push origin main    # fazendo o push da branch local para o github
```

Existe uma diferença entre os métodos ssh e https. Para utilizar o método ssh precisa criar uma chave SSH

```
$ ssh-keygen -t ed25519 -C "your_email@example.com"
$ ssh-keygen -t ed25519 -C "guifl_pereira@hotmail.com"
> Generating public/private algorithm key pair.
> Enter a file in which to save the key (/c/Users/you/.ssh/id_algorithm):[Press enter]
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
$ eval "$(ssh-agent -s)"
> Agent pid 59566
$ ssh-add ~/.ssh/id_ed25519

Depois precisa entrar no site do GitHub, ir em configurações SSH Keys e adicionar o conteúdo da chave publica 
```

Quando for fazer o push com esse método precisar digitar a senha do GitHub toda vez. Para utilizar o métodos HTTPS não precisa gerar a SSH Key, basta digitar o usuário e a senha, porém o GitHub agora pede para usar um PAT (personal acess tokens) como senha. Esse PAT é gerado na parte de configurações do GitHub/developer settings/Persnoal acess tokens

Para verificar a existências da branches e cricar novas usamos

```
git branch   # lista as branchs existentes atualmente
git branch nome_da_branch  # cria uma nova branch com o nome escolhido
git branch titulo   # exemplo
```

Agora se quisermos trocar de branch utilizamos

```
git checkout nome_da_branch
git checkout titulo    # exemplo
```

Há uma forma mais fácil de já criar uma nova branch e fazer o checkout para ela

```
git branch -b nome_da_branch
git branch -b lista    # exemplo
```

Para unir duas branches, depois que o trabalho em uma delas já finalizou precisamos usar o merge, com esse comando geramos um commit de merge

```
git merge nome_da_branch_que_queremos_puxar
git merge titulo   # usando esse comando na master, vamos trazer as alterações da branch titulo para a master
```

Precisei adicionar duas opções no .bashrc para que o Git utilizasse o neovim como editor padrão, pois ele não estava conseguindo utilizar o neovim.

```bash
export EDITOR='/usr/local/bin/nvim'
export GIT_EDITOR='/usr/local/bin/nvim'
```

Exige outra forma de unir duas branches. Além do merge podemos utilizar o rebase, nesse caso o Git vai pegar todos os commits realizados na branch que estamos puxando e colocar “na frente” dos commits realizados na master e não gera um commit de merge

```
git rebase nome_da_branch_que_queremos_puxar
git rebase titulo   # usando esse comando na master, vamos trazer as alterações da branch titulo para a master e colocar como ultimo commit o realizado na branch master
```

Pela leitura inicial que eu fiz, utilizar merge é melhor do que rebase, pois com o merge mantemos a timeline de commits intacta, e podemos remover os commits de merge depois. O comando merge também apresenta todos os possíveis conflitos de uma vez, enquanto que o rebase vai mostrando um por um, além de ser mais fácil de reverter um merge do que um rebase. O rebase parece ser bem útil quando trabalhamos sozinho.

Quando vamos realizar um merge e há um conflito nos arquivos que queremos unir o git não realiza o merge e apresenta um erro. Quando abrimos o arquivo que gerou o conflito podemos verificar qual foi o conflito, ele vai estar sinalizado da seguinte maneira

```
<<<<<<<<< HEAD
linhas do arquivo que você esta
========
linhas do arquivo da branch
>>>>>>>> nome da branch que tem o arquivo em conflito
```

O comando git checkout também serve para desfazer mudança que não foram adicionadas ao stage ainda, então se modificamos um arquivo, mas não usamo o git add, podemos desfazer a alteração com o git checkout

```
git checkout -- nome_do_arquivo
git checkout -- index.html   # exemplo
```

Caso eu já tenha adicionado o arquivo no stage, mas não tenha commitado ainda, para desfazer eu preciso primeiro remover o arquivo do stage e depois usar o checkout para desfazer

```
git reset HEAD nome_do_arquivo
git reset HEAD index.html
git checkout -- index.html
```

Agora caso já tenha commitado as alterações precisamos reverter o commit

```
git revert hash_do_commit
git revert 43bb0171ac44f52966a51976df29dcdf9ad93ca2   # exemplo. Isso irá gerar um novo commit para reverter as mudanças
```

Caso eu faça alguma mudança no código, mas finalize e queira guardar para continuar trabalhando mais tarde, porém sem fazer um commit eu preciso fazer um stash

 

```
git stash
git stash list  # exibe a lista de stash salvos para continuar em trabalho WIP
```

Depois de realizar as novas modificações no arquivo eu preciso puxar as modificações que estão em stash para continuar trabalhando

```
git stash apply numero_da_stash_obtido_com_o_git_stash_list
git stash apply 0
git stash drop  # remove os stash

ou

git stash pop # já aplica e as modifcações da stash e remove ela
```

O comando checkout também permite que você navegue para branchs antigas

```
git checkout 7_primeiros_caracteres_da_hash_do_commit_desejado
git checkout 9d592b3 
```

Podemos fazer alterações, testes e até commits nesse momento sem afetar o código principal, pois estamos desacoplados da timeline. Contudo, se precisar salvar as modificações realizadas é preciso criar uma nova branch

```
git branch -b nome_da_branch
```

Para voltar para a branch principal basta usar o checkout novamente

```
git checkout master
```

Com o git log -p podemos ver as alterações commit por commit realizadas no código, mas caso seja necessário verificar todas as alterações de uma vez entre dois commits diferente precisamos usar o diff. Esse comando também mostra a diferença entre um arquivo que estamos editando, mas não adicionamos no stage.

```
git diff 7_digitos_da_hash_mais_antiga..7_digitos_da_hash_mais_recente
git diff 9d592b3..dfeb810   # exemplo, mostra todas as diferentea entre (..) o commit com a hash 9d592b3 e o commit com a hash dfeb810
git diff  # mostra a diferença entre o arquivo que modificamos, mas não evniamos para o stage e o arquivo já commitado
```

Depois de já ter editado o código o suficiente para lançar uma release podemos marcar o estado do código como uma tag para poder marcar aquela versão como finalizada e que não poderá mais ser alterada, assim podemos continuar editando o nosso código, porém as novas modificações entrarão na versão seguinte.

```
git tag -a nome_da_versão -m "mensagem para a versão"
git tag -a v0.1.0 -m "Lançando a primeira versão (BETA) da aplicação de cursos"
git tag   # exibe a lista de tag que minha aplicação tem
```