:- set_prolog_flag(unknown,fail).

es_cebra :- es_ungulado, tiene_rayas_negras. % Regla 1
es_ungulado :- rumia, es_mamifero. % Regla 2
es_ungulado :- es_mamifero, tiene_pezunas. % Regla 3

es_mamifero. % Hecho 1
tiene_pezunas. % Hecho 2
tiene_rayas_negras. % Hecho 3 