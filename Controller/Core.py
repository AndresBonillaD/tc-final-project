from Entity.FiniteStateMachine import FiniteStateMachine
from Entity.State import State


class Core:
    # attributes
    automatas = {}

    def __init__(self):
        self.automatas = dict()

    #### MENU
    def menuLoop(self):
        case = ''

        while case != 'exit':
            case = self.switcher()
            print('Case:', case)

            if case == 'case0':
                print('futura carga de archivo .txt')
                continue
            if case == 'case1':
                print('futura carga de automata manualmente')
                continue
            if case == 'automataDemo':
                print('hardcoded fsm')

                # hardcoded dfa L = { a*b+ }
                # instance transitions
                q0Transitions = {'a': ['q0'], 'b': ['q1']}
                q1Transitions = {'b': ['q1']}
                # instance states
                q0 = State('q0', False, q0Transitions)
                q1 = State('q1', True, q1Transitions)
                # alphabet set
                a = {'a', 'b'}
                # states set
                s = {q0, q1}
                # initial state q0
                # instance dfa object
                fda0 = FiniteStateMachine(a, s, q0)

                #stores it in automatas
                self.automatas[0] = fda0
                print(self.automatas)
                # fda0.showData()
                #word = input('Compute word: ')
                #fda0.computeWord(word)
                continue
            if case == 'memoryFsm':
                id = int(input('Enter fsm id: '))
                select_fsm = self.automatas.get(id)
                print(type(select_fsm))
                # aqui debe ir el casteo de AutomataController
                continue
            if case == 'nothing':
                print('INVALID COMMAND')
                continue

    # return the specific command corresponding to the user input
    def switcher(self):

        switcher = {
            '0': 'case0',
            '1': 'case1',
            '2': 'memoryFsm',
            '3': 'automataDemo',
            'exit': 'exit'
        }

        print('-----   Menu   -----')
        print('''
        0: Case0
        1: case1
        2: fsm on memory
        3: Automata Demo
        exit: salir
            ''')

        argument = input('Ingrese comando: ')
        return switcher.get(argument, 'nothing')

    # get automata form dict that stores in core what is created
    def getAutomata(self, id):
        return self.automatas.get(id)