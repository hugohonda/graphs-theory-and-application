/*
 * Universidade de Bras�lia
 * Departamento de Ci�ncia da Computa��o
 * Teoria e Aplica��es de Grafos
 * Prof. Dr. Vinicius Ruela Pereira Borges

 Arquivo: no.h
 
Funcao deste programa: Implementacao de um grafo utilizando representacao de lista de adjacencia
Como compilar:
                gcc *c.c -o busca
Para executar:
                ./busca < g1.in
                
*/

#include <stdio.h>
#include <stdlib.h>

// Nao remover nunca essas guards!!!
#ifndef _NOH_
#define _NOH_

typedef struct no
{
    int chave;
    float w;
    struct no *prox;
} *No;

No No_cria(int chave, float peso);

// Nao remover as guards
#endif

