/*
 * ibcfun.c
 *
 *  Created on: 17-Feb-2013
 *      Author: ajoy
 *
 *  To compile run gcc/cc ibc.c -lpbc -lgmp -lcrypto
 */
#include<stdio.h>
#include<pbc/pbc.h>
#include<pbc/pbc_test.h>
#include<openssl/sha.h>

int main(int argc, char **argv) {
  pairing_t pairing;
  pbc_demo_pairing_init(pairing, argc, argv);
  char m[80]={0};


  if (!pairing_is_symmetric(pairing)) pbc_die("pairing must be symmetric");

  printf("Enter the message to be encrypted : ");
  gets(m);
  size_t len_m = sizeof(m);

  unsigned char hash[30];
  SHA1(m, len_m, hash);
  printf("The hash is : %s", hash);

  element_t g, h;
  element_t public_key, secret_key;
  element_t sig;
  element_t temp1, temp2;

  element_init_G2(g, pairing);
  element_init_G2(public_key, pairing);
  element_init_G1(h, pairing);
  element_init_G1(sig, pairing);
  element_init_GT(temp1, pairing);
  element_init_GT(temp2, pairing);
  element_init_Zr(secret_key, pairing);

  element_random(g);
  element_random(secret_key);
  element_pow_zn(public_key, g, secret_key);
  printf("The private key is : %s while the public key is %s\n",secret_key, public_key );
  element_from_hash(h, hash, 30);
  element_pow_zn(sig, h, secret_key);

  pairing_apply(temp1, sig, g, pairing);
  pairing_apply(temp2, h, public_key, pairing);
  if(!element_cmp(temp1, temp2)){
	  printf("\nVerified\n");}
  else{
	  printf("\nNot verified\n");
  }

}
