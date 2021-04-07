# Tema3 LFA

   Am folosit ANTLR pentru a genera parser-ul. Aceasta este gramatica pe care am folosit-o
KLEENE : '*'+;
REUNION: '|';
OPEN : '(';
CLOSED : ')';

WHITESPACE : [ \t\n]+ -> skip;
VAR : ([A-Z] | [a-z]) ;

expr : c_expr REUNION expr | c_expr;
c_expr : c_expr c_expr | k_expr | atom;
k_expr : atom KLEENE;
sub_expr: OPEN expr CLOSED;
atom : variable | sub_expr;
variable : VAR;

   In fisierul ERtoNFA am implemantat 3 functii care intorc nfa-uri echivalente cu expresia
regulata obtinuta prin aplicarea unuia din cei 3 operatori pe expresiile regulate echivalente cu nfa
-urile primite (un singur nfa primit in functia star()).

   In clasa ERVisitorToNFA care mosteneste ERVisitor trec prin arborele de parsare a expresiei
regulate si construiesc un NFA echivalent.
    In metoda visitVariable intorc un nfa cu 2 stari si cu o tranzitie din starea initiala in cea
finala pe caracterul din variabila.
    In tot restul metodelor verific ce copii mai exista pentru acel nod si ii vizitez.
    In medoata visitK_expr intorc rezultatul obtinut prin alicarea functiei star() din ERtoNFA pe
nfa-ul obtinut prin vizitarea atomului pe care se aplica operatorul kleene.
    In medoata visitC_expr verific daca exista doua noduri c_expr si intorc rezultatul obtinut din
functia concatenation cu rezultatele vizitarii nodurilor c_expr sau rezultatul vizitarii celuilalt
nod daca c_expr nu reprezinta o concatenare.
    In medoata visitExpr verific daca se face reuniunea intre dou expresii si intorc rezultatul
obtinut din functia reunion cu rezultatele vizitarii nodurilor c_expr sau rezultatul vizitarii
nodului c_expr daca expresia nu era o reuniune.

   Transformare NFA -> DFA este facuta in metoda from_nfa() din clasa DFA care explicata in
README-ul de la Tema 2.
