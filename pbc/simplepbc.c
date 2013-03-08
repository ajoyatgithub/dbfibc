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
int nm, dm;
char hash[20];
unsigned char hid[130];
element_t h, g, share, pks, pk ,pk_temp;
int n, t, f, ct = 0;
pairing_t pairing;

int init_pairing(){
/*This function will open the pairing file and initialize the pairing.*/
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

int read_share(){
/*This function will open secrets and read the binary data into unsigned char
and store it in element share*/
  FILE *fp;
  unsigned char str[20];
  fp = fopen("../secrets","rb");
  if(!fp)
    return -1;
  fread(str, 20, 1, fp);
  fclose(fp);
  element_init_Zr(share, pairing);
  element_from_bytes(share, str);
}

void hash_id_s(char *str){
/*This function will read the string, hash it and then map to an element in G2.
It will then compute hash^share*/
  element_init_G2(h, pairing);
  element_init_G2(pks, pairing);
  SHA1(str, sizeof(str), hash);
  element_from_hash(h , hash, 20);
  element_pow_zn(pks, h, share);
}

void gen_privatekey(unsigned char *str, int nodeID, int senderID){
/*This will compute the private key from all the IBC_REPLY's received
*/
  int i, j;
  float l;
  signed long int num, dnum;
  
  num = nm;
  dnum = dm;
  i = nodeID;
  j = senderID;
  lambda(i, 1, 10);
  element_t b, c, ci, keyshare;
  
  element_init_G2(keyshare, pairing);
  
  element_init_Zr(b, pairing);
  element_init_Zr(c, pairing);
  element_init_Zr(ci, pairing);

  element_set_si(b, num);
  element_set_si(c, dnum);
  element_from_bytes(keyshare, str);
  //TODO: Need to correct the pow_zn function, might not work.....
  element_pow_zn(pk_temp, keyshare, b);
  element_invert(ci, c);
  element_pow_zn(pk_temp, pk_temp, ci);
  element_mul(pk, pk, pk_temp);
  if(ct = t)
    printf("Done\n");
  else if(ct < t)
    ct = ct + 1;
}

int lambda(int nodeID, int si, int ei){
/*
*/
  int i, j;
  nm = 1;
  dm = 1;
  float l = 1, r = 1;
  i = nodeID;
  for(j = si; j <= ei; j++){
    if(j==i)
      continue;
    nm *= j;
    dm *= j - i;
  }
  return 1;
}
