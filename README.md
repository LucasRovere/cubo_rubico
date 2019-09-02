
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

    Comandos:
        'restart [size]': reinicia o cubo com tamanho 'size' e apaga o tracking

        'track': reinicia o tracking mantendo o estado do cubo e mostra as tracks salvas

        'track [nome]': salva o tracking atual com usando a chave 'nome'
        'state [nome]': salva o estado atual do cubo com a chave 'nome'

        'load track [nome]': inicia a track salva com chave 'nome'
        'load state [nome]': atualiza o cubo com o estado 'nome'

        'run [nome]': Executa todos os movimentos da track salva com chave 'nome'
        'run [nome] -': Executa o inverso da track salva com chave 'nome'
        
        'move [face] [camadas interiores]': Faz o movimento

        'undo': desfaz o último movimento

        'spin [axis]': gira o cubo inteiro no eixo escolhido

    Comandos move:
        'move' => pode ser omitido
        'face => Descrito abaixo
        'q' => sai do modo run
        '' => input vazio (ou comando inexistente) roda o próximo movimento

    Faces move:
        u => Face superior sentido horário
        u' => Face superior sentido anti horário

        d => Face inferior sentido horário
        d' => Face inferior sentido anti horário

        f => Face dianteira sentido horário
        f' => Face dianteira sentido anti horário

        b => Face traseira sentido horário
        b' => Face traseira sentido anti horário

        r => Face direita sentido horário
        r' => Face direita sentido anti horário

        l => Face esquerda sentido horário
        l' => Face esquerda sentido anti horário