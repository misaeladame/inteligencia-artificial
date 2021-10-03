hombre(dante).
hombre(carlos).
hombre(beto).
hombre(andres).

espadre(dante, carlos).
espadre(carlos, beto).
espadre(beto, andres).

esabuelo(X, Y) :-
espadre(X, A),
espadre(A, Y).