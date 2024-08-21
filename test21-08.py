class Pessoa:

    def __init__(self, nome, idade, tamanho, peso):
        self.nome = nome
        self.idade = idade
        self.tamanho = tamanho
        self.peso = peso
    
    def informarNome(self):
        return self.nome
    
    def informarIdade(self):
        return self.idade
    
    def informarTamanho(self):
        return self.tamanho
    
    def informarPeso(self):
        return self.peso

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def completouAniversario(self):
        self.idade += 1

    def alterouDePeso(self, novoPeso):
        self.peso = self.peso + novoPeso

    def checaMaiorIdade(self, idade):
        if idade >= 18:
            return True
        elif idade < 18 and idade > 0:
            return False
        else:
            return 2
        
    def informaMaiorIdade(self):
        if self.checaMaiorIdade(self.informarIdade()) == True:
            print("Você é maior de idade.")
        elif self.checaMaiorIdade(self.informarIdade()) == False:
            print("Você é menor de idade.")
        else:
            print("Você informou uma idade inválida.")

class SuperPessoa(Pessoa):

    def __init__(self, nome, idade, tamanho, peso, superPoder, afiliacao):
        super().__init__(nome, idade, tamanho, peso)
        self.forca = peso*tamanho
        self.superPoder = superPoder
        self.afiliacao = afiliacao

    def informarFicha(self):
        print(f"Nome: {self.nome}\nAfiliação: {self.afiliacao}\nForça: {self.forca}\nSuper Poder: {self.superPoder}")

def main():

    pessoaComum1 = Pessoa("Trevor", 17, 1.80, 75.5)

    pessoaIncomum1 = SuperPessoa("Lisa", 20, 1.65, 67.4, "Super Força", "Teen Titans")

    print(pessoaComum1.informarNome())
    pessoaComum1.informaMaiorIdade()
    pessoaComum1.completouAniversario()
    pessoaComum1.informaMaiorIdade()
    print(pessoaComum1.informarPeso())
    pessoaComum1.alterouDePeso(-15.5)
    print(pessoaComum1.informarPeso())

    print("")

    pessoaIncomum1.informarNome()
    pessoaIncomum1.informaMaiorIdade()
    pessoaIncomum1.informarFicha()

main()