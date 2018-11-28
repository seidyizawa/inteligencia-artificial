pertence_a(X,[X|_]).
pertence_a(X,[_|R]) :-
	pertence_a(X,R).

num_elementos([_|R],N) :-
	num_elementos(R,NC),
	N is NC + 1.

elem_repetido([],[]).
elem_repetido([X|C],L) :-
	pertence_a(X,L),
	elem_repetidos(C,L).
elem_repetido([X|C],[X|C2]) :-
	pertence_a(X,C),
	elem_repetido(C,C2).

intercalada([],[],[]).
intercalada([],L,L).
intercalada(L,[],L).
intercalada([X,R1],[Y|R2],[X,Y|R3]) :-
	intercalada(R1,R2,R3).

insere_ord(N,[],[N]).
insere_ord(N,[X|R],L) :-
	N >= X,
	insere_ord(N,R,L).


ordenada([],[]).
ordenada([X|R],L2) :-
	insere_ord(X,_,L2),
	ordenada(R,L2).

intersecao([X|C],L2) :-
	pertence_a(X,L2).
intersecao([_|C],L2) :-
	intersecao(C,L2).

concatenadas([],L,L).
concatenadas([C|R],L2,[C|R2]) :-
	concatenadas(R,L2,R2).

remove_repetidas([],[]).
remove_repetidas([X|C],[X|C1]) :-
	not(pertence_a(X,C)),
	remove_repetidas(C,C1).
remove_repetidas([_|C],L) :-
	remove_repetidas(C,L).

uniao(L1,L2,RESULTADO) :-
	concatenadas(L1,L2,R1),
	remove_repetidas(R1,RESULTADO).

busca(X,[],[X]).
busca(X,[C1|R1],RESULTADO) :-
	intersecao(X,C1),
	uniao(X,C1,COMPONENTE),
	busca(X,COMPONENTE,RESULTADO).

subculturas([],[]).
subculturas([X|C],RESULTADO) :-
	subculturas(C,COMPONENTE),
	busca(X,COMPONENTE,RESULTADO).