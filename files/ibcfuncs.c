/*
  cc ibcfuncts.c -lpbc -lgmp -lcrytpo
  '-lcrypto' used for SHA1
  ./a.out pairing
*/

#include<stdio.h>
#include<pbc/pbc.h>
#include<pbc/pbc_test.h>
#include<openssl/sha.h>
#include<string.h>

char ident[100], param[1024];
int nm, dm;
char hash[20];
unsigned char hid[130];
element_t h, g, share, pks, pk ,pk_temp;
int sys_n = 0, sys_t = 0, sys_f = 0, ct = 0, q;
pairing_t pairing;

int init_pairing(int n, int t, int f){
  /*This function will open the pairing file and initialize the pairing.*/
  FILE *fp;
  int k, lk;
  sys_n = n;
  sys_t = t;
  sys_f = f;
  q = 2 * sys_t + 1;
  fp = fopen("files/pairing", "r");
  size_t count = fread(param, 1, 1024, fp);
  fclose(fp);
  if(!count){
    pbc_die("input error\n");
    return -1;
  }
  pairing_init_set_buf(pairing, param, count);
  printf("Initialized pairing in ibc.c\n");
  return 0;
}

int read_share(){
  /*This function will open secrets and read the binary data into unsigned char
  and store it in element share*/
  FILE *fp;
  unsigned char str[20];
  fp = fopen("files/secrets","rb");
  if(!fp)
    return -1;
  printf("About to read from secrets\n");
  size_t count = fread(str, 20, 1, fp);
  fclose(fp);
  if(!count)
    printf("Could not read from secrets\n");
  element_init_Zr(share, pairing);
  element_from_bytes(share, str);
}

void hash_id_s(char *str){
  /*This function will read the string, hash it and then map to an element in G2.
  It will then compute hash^share*/
  element_init_G2(h, pairing);
  element_init_G2(pks, pairing);
  SHA1(str, strlen(str), hash);
  element_from_hash(h , hash, 20);
  element_pow_zn(pks, h, share);
  element_to_bytes(hid, pks);
}

void gen_privatekey(unsigned char *str, int nodeID, int senderID){
  /*This will compute the private key from all the IBC_REPLY's received
  */
  int i, j;
  float l;
  if(ct > sys_t){
    printf("Done\n");
    element_printf("The key is %B\n", pk);
    return;
  }
  else if(ct <= sys_t)
    ct++;
  printf("Value of sys_t and ct is %d and %d\n", sys_t, ct);
  i = nodeID;
  j = senderID;
  lambdal(i, q);
  element_t b, c, ci, keyshare;
  
  element_init_G2(keyshare, pairing);
  element_init_G2(pk_temp, pairing);
  element_init_G2(pk, pairing);
  element_init_Zr(b, pairing);
  element_init_Zr(c, pairing);
  element_init_Zr(ci, pairing);

  element_set_si(b, nm);
  element_set_si(c, dm);
  printf("nm is %d\ndm is %d\n", nm, dm);
  element_from_bytes(keyshare, str);
  element_pow_zn(pk_temp, keyshare, b);
  element_invert(ci, c);
  element_pow_zn(pk_temp, pk_temp, ci);
  element_mul(pk, pk, pk_temp);
}

int lambdal(int i, int ei){
  /*
  */
  int j;
  nm = 1;
  dm = 1;
  for(j = 1; j <= ei; j++){
    if(j==i)
      continue;
    nm *= j;
    dm *= j - i;
  }
  return 1;
}

int main(){
  char asd[20];
  unsigned char key[100];
  if(init_pairing(1, 1, 1) == -1){
    printf("Error");
    return -1; 
  }
  read_share();
  printf("Give a string to encrypt : ");
  scanf("%s", asd);
  hash_id_s(asd);
  element_printf("The string has been hashed, it is : %B\n", pks);
  element_to_bytes(key, pks);
  gen_privatekey(key, 1, 2);
  return 0;
}