from NFA import NFA


def concatenation(nfa1: NFA, nfa2: NFA) -> NFA:
    state_number = nfa1.states + nfa2.states - 1
    transitions = nfa1.transitions.copy()

    # unim starea finala a automatului 1 cu starea initiala a automatului 2
    for (state, ch), next_states in nfa2.transitions.items():
        new_next_states = {state + nfa1.states - 1 for state in next_states}
        if state == 0:  # adaugam la tranzitiile starii finale din automatul 1 tranzitiile starii
            # initiale din automatul 2
            transitions[(nfa1.states - 1, ch)] = \
                transitions.get((nfa1.states - 1, ch), set()).union(new_next_states)
        else:
            transitions[(state + nfa1.states - 1, ch)] = new_next_states

    return NFA(state_number, 0, {state_number - 1}, transitions)


def reunion(nfa1: NFA, nfa2: NFA) -> NFA:
    state_number = nfa1.states + nfa2.states + 2
    transitions = dict()
    # adaugam starea 0 din care pleaca doua tranzitii pe epsilon catre starile initaile ale
    # automatelor initiale
    transitions[(0, 'eps')] = {1, nfa1.states + 1}

    # adaugam 1 la toate starile intiale din automatul 1 pentru a acomoda noua stare initiala
    for (state, ch), next_states in nfa1.transitions.items():
        new_next_states = {state + 1 for state in next_states}
        transitions[(state + 1, ch)] = new_next_states

    # aduagam tranzitia de la starea finala a adutomatului 1 in starea finala a automatului rezultat
    if transitions.get((nfa1.states, 'eps')):
        transitions[(nfa1.states, 'eps')] = \
            transitions.get((nfa1.states, 'eps')).union({state_number - 1})
    else:
        transitions[(nfa1.states, 'eps')] = {state_number - 1}

    # adaugam 1 la toate starile intiale din automatul (numarul de stari din automatul 1 + 1)
    # pentru a acomoda noua stare initiala si starile din automatul 1
    for (state, ch), next_states in nfa2.transitions.items():
        new_next_states = {state + nfa1.states + 1 for state in next_states}
        transitions[(state + nfa1.states + 1, ch)] = new_next_states

    # aduagam tranzitia de la starea finala a adutomatului 2 in starea finala a automatului rezultat
    if transitions.get((state_number - 2, 'eps')):
        transitions[(nfa1.states, 'eps')] = \
            transitions.get((state_number - 2, 'eps')).union({state_number - 1})
    else:
        transitions[(state_number - 2, 'eps')] = {state_number - 1}

    return NFA(state_number, 0, {state_number - 1}, transitions)


def star(nfa: NFA) -> NFA:
    state_number = nfa.states + 2
    transitions = dict()
    # adugam o noua stare initiala care are tranzitii pe epsilon catre vechea stare initiala si nou
    # stare finala
    transitions[(0, 'eps')] = {1, state_number - 1}

    # adaugam 1 la toate starile intiale din automatul 1 pentru a acomoda noua stare initiala
    for (state, ch), next_states in nfa.transitions.items():
        new_next_states = {state + 1 for state in next_states}
        transitions[(state + 1, ch)] = new_next_states

    # adugam la vechea stare finala doua tranzitii pe epsilon catre vechea stare initiala si nou
    # stare finala
    if transitions.get((state_number - 2, 'eps')):
        transitions[(state_number - 2, 'eps')] = \
            transitions.get((state_number - 2, 'eps')).union({1, state_number - 1})
    else:
        transitions[(state_number - 2, 'eps')] = {1, state_number - 1}

    return NFA(state_number, 0, {state_number - 1}, transitions)
