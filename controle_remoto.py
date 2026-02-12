from rich import print
from rich.panel import Panel
from time import sleep
import os

def resfresh():
    sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')


class ControleRemoto:
    """
    Classe Que simula o controle remoto de uma televisão
    """

    def __init__(self): # Metódo construtor
        # Metódo de instância
        self.desligada = True
        self.volume = 1
        self.canal = 1


    def __str__(self):
        return f'Canal: {self.canal}, Volume: {self.volume}'


    def __getstate__(self):
        return f'Estado: Desligada: {self.desligada}; Volume: {self.volume}; Canal: {self.canal}'


    def ligar(self):
        """
        Função para ligar a televisão
        :return: vazio
        """
        self.desligada = False


    def desligar(self):
        """
        Função para desligar a televisão
        :return: vazio
        """
        self.desligada = True


    def aumentar_volume(self):
        """
        Função para aumentar o volume da televisão
        :return: vazio
        """

        # Verifica se a tv está ligada, e se o volume é menor que 5.
        if not self.desligada and self.volume < 5:
            self.volume += 1


    def diminuir_volume(self):
        """
        Função para diminuir o volume da televisão
        :return: vazio
        """

        # Verifica se a tv está ligada, e se o volume é maior que 0.
        if not self.desligada and self.volume > 0:
            self.volume -= 1


    def proximao_canal(self):
        """
        Função para ir para o proximo canal
        :return: vazio
        """

        # Verifica se a tv está ligada
        if not self.desligada:
            self.canal += 1

            # Verifica se o canal é menor que 5, se for maior volta para o canal 1
            if self.canal > 5:
                self.canal = 1


    def canal_anterior(self):
        """
        Função para voltar para o canal anterior
        :return: vazio
        """

        # Verifica se a tv está ligada
        if not self.desligada:
            self.canal -= 1
            if self.canal < 1:
                self.canal = 5


    def tela(self):
        """
        Função de simular a tela da televisão
        :return: vazio
        """

        # Verifica se a tv está ligada ou desligada
        if self.desligada:
            tv = Panel(renderable='[red]:prohibited: A tv está desligada[/]', title='[ TV ]', width=30)
            print(tv)
        else:
            # Barra de volume da tv
            barra = '█' * self.volume
            vazio = ' ' * (5 - self.volume)

            # Canais que irá ser mostrado na tv
            canais_lista = ['Globo', 'SBT', 'Tribuna', 'Bandeirantes', 'Record']
            canais = ''

            # Percorre a lista do canais
            for i, nome in enumerate(canais_lista):
                # Se o índice for igual ao canal atual. O canal fica preto com fundo amarelo
                if i == self.canal - 1:
                    canais += f"[black on yellow]{nome}[/] "

                else:
                    # Mostar todos os canais
                    canais += f"{nome} "

            tv = Panel(renderable=f'[green]:television:A tv está ligada![/] \nCanal: {canais} \nVolume: [[green on white]{barra}{vazio}[/]]', title='[ TV ]', width=60)
            print(tv)

def main():

    televisao = ControleRemoto()

    while True:
        try:
            resfresh()
            televisao.tela()
            simb = ''

            while simb not in '<>+-@' or not simb:
                simb = input(f'\n<Canal {televisao.canal}> +Volume {televisao.volume}- ').strip()
                if simb:
                    simb = simb[0]


            if simb == '@':
                if televisao.desligada:
                    televisao.ligar()
                else:
                    televisao.desligar()

            elif simb == '<':
                televisao.canal_anterior()

            elif simb == '>':
                televisao.proximao_canal()

            elif simb == '+':
                televisao.aumentar_volume()

            elif simb == '-':
                televisao.diminuir_volume()


        except KeyboardInterrupt:
            resfresh()
            print('[green]Volte sempre![/]')
            break

if __name__ == '__main__':
    main()
