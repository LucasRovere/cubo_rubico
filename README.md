
#######################################################
    Cubo mágico virtual
    Modela cubos de tamanhos variáveis
    Faz os movimentos no cubo atualizando no terminal
    Sequencia de movimentos pode ser salva e repetida

    Movimentos:
    "u" => Face superior horário
    "u'" => Face superior anti horário

    "d" => Face inferior horário
    "d'" => Face inferior anti horário

    "f" => Face dianteira horário
    "f'" => Face dianteira anti horário

    "b" => Face trazeira horário
    "b'" => Face trazeira anti horário

    "r" => Face lateral direira para cima
    "r'" => Face lateral direita para baixo

    "l" => Face lateral esquerda para cima
    "l'" => Face lateral esquerda para baixo

    Camadas internas:
        Cada traço (-) depois do comando gira uma camada mais para dentro do cubo. Ex:
        > "u" => gira a face superior
        > "u-" => gira a camada abaixo da face superior (sem girar a face)

        > "d" => gira a face inferior
        > "d-" => gira a camada acima da face inferior (sem girar a face)

    Comandos:
        'restart': reinicia o cubo ao estado original e apaga o tracking
        'track': reinicia o tracking mantendo o estado do cubo e mostra as tracks salvas
        'track nome': salva o tracking atual com usando a chave 'nome' como referencia e mostra as tracks salvas
        'run nome': inicia a track salva com chave 'nome'

    Comandos track:
        'r' => desfaz o último movimento
        'q' => sai do modo run
        '' => input vazio (ou comando inexistente) roda o próximo movimento
