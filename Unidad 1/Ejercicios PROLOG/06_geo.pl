localizado_en(atlanta, georgia). % Cláusula 1
localizado_en(houston, texas). % Cláusula 2
localizado_en(austin, texas). % Cláusula 3
localizado_en(toronto, ontario). % Cláusula 4
localizado_en(X, usa) :- localizado_en(X, georgia). % Cláusula 5
localizado_en(X, usa) :- localizado_en(X, texas). % Cláusula 6
localizado_en(X, canada) :- localizado_en(X, ontario). % Cláusula 7
localizado_en(X, norteamerica) :- localizado_en(X, usa). % Cláusula 8
localizado_en(X, norteamerica) :- localizado_en(X, canada). % Cláusula 9