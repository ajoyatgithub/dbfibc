/*
  cc simplepbc.c -lpbc -lgmp -lcrytpo
  '-lcrypto' used for SHA1
  ./a.out pairing
*/


#include<stdio.h>
#include<pbc/pbc.h>
#include<pbc/pbc_test.h>
#include<openssl/sha.h>
#include<string.h>

char ident[100], param[1024];
int a = 4;
char hash[20];
unsigned char hid[130], share[150];
element_t h, g;
pairing_t pairing;

int init_pairing(){
  FILE *fp;
  int k, lk;
  fp = fopen("pairing", "r");
  size_t count = fread(param, 1, 1024, fp);
  fclose(fp);
  if(!count){
    pbc_die("input error\n");
    return -1;
  }
  pairing_init_set_buf(pairing, param, count);
  return 0;
}

void hash_id_G1(char *str){
  element_init_G2(h, pairing);
  SHA1(str, sizeof(str), hash);
  element_from_hash(h , hash, 20);
  FILE *fp;
  fp = fopen("secrets", "r");
  size_t count = fread(share, 1, 1024, fp);
  fclose(fp);
  element_from_bytes()
}

int add(){
  int b, c;
  b = 2;
  a = a + b;
  return a;
}

int main(){
  char strin[100];
  char *hash;
  printf("Enter some string to hash : ");
  scanf("%s", strin);
  hash = hash_id_G1(strin);
  printf("sds : %s : \n", hash);
}

/*
int main(int argc, char **argv){
  pairing_t pairing;
  pbc_demo_pairing_init(pairing, argc, argv);
  if(!pairing_is_symmetric(pairing)) pbc_die("Pairing must be symmetric\n");
//gen_IBC_key 

  char m[80] = {0};
  printf("Enter the message to be encrypted : ");
  gets(m);

  size_t msglen = sizeof(m);

  unsigned char hash[30];
  SHA1(m, msglen, hash);

  element_t g, h;
  element_t public_key, private_key;
  element_t sig;
  element_t temp1, temp2;

  element_init_G2(g, pairing);
  element_init_G2(public_key, pairing);
  element_init_G1(h, pairing);
  element_init_G1(sig, pairing);
  element_init_GT(temp1, pairing);
  element_init_GT(temp2, pairing);
  element_init_Zr(private_key, pairing);

  element_random(g);
  element_random(private_key);

  element_pow_zn(public_key, g, private_key);
  element_from_hash(h, hash, 30);
  element_pow_zn(sig, h, private_key);

  pairing_apply(temp1, h, public_key, pairing);
  pairing_apply(temp2, g, sig, pairing);
  if(!element_cmp(temp1, temp2))
    printf("Successfully verified\n");
  else
    printf("Verification failed\n");
}*/
