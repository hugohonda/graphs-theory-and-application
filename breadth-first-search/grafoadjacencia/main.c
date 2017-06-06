/*
 * Universidade de Bras�lia
 * Departamento de Ci�ncia da Computa��o
 * Teoria e Aplica��es de Grafos
 * Prof. Dr. Vinicius Ruela Pereira Borges

 Arquivo: main.c
 
Funcao deste programa: Implementacao de um grafo utilizando representacao de lista de adjacencia
Como compilar:
                gcc *c.c -o busca
Para executar:
                ./busca < g1.in
                
*/

#include <stdio.h>
#include <stdlib.h>
#include "grafo.h"
#include "fila.h"

main()
{
    int i,j,r,nroVertices;
    float aresta;
    Grafo *g = NULL;
    No Q = NULL;
    No des,no_u,no_v;

    // Leitura I/O padrao do numero de vertices do Grafo G
    scanf("%d\n",&nroVertices);
    g = Grafo_cria (nroVertices);    
    
    // Como a matriz eh simetrica, 
    for(i = 0; i < nroVertices;i++)
    {
	for(j = 0; j < nroVertices;j++)
	{
	    scanf("%f",&aresta);
	    if(aresta > 0.0 && i < j)
	    {
		
		no_u = No_cria(i,aresta);
		no_v = No_cria(j,aresta);
		
	        r = Grafo_insereAresta(g,no_u,no_v);
		if(!r)
		{
		    fprintf(stderr,"ERRO ao inserir aresta!\n");
		}
	    }
	}
	scanf("\n");
    }
    
    /* Como usar as funcoes da fila
     * 
    novo = No_cria(4,0.5);
    r=Fila_enfileira(&Q,novo);
    des=Fila_desenfileira(&Q);
    Fila_imprime(Q);
    free(Q);  
    */
    
    imprimeGrafo(g);
    
    // Libera o espaco em memoria
    free(g->Adj);
    free(g);
    free(no_u);
    free(no_v);
    
    // Indica ao SO que a execucao deste programa foi bem-sucedida
    return 0;
}