#include <stdio.h>
#include <stdlib.h>

int MCD(int a, int b);
int MCD_R(int a, int b);
int Add_Inv(int a);
void AEE(int a, int b, int *d, int *x, int *y);

int main() {
  int d,x,y;
  char opcion;
  char buffer[50];
  FILE* archi;
  int bandera=1, alpha, betha, i, j, flag=1;
  //printf("%d\t%d\t%d\n",x,y,d);
  do{
    printf("Push e to encrypt.\n");
    printf("Push d to decrypt.\n");
    fflush(stdin);
    scanf("%c",&opcion);
    switch (opcion) {
      case 'd':
        system("clear");
        //printf("Write the file name\n");
        //scanf("%s", archivo);
        printf("Write alpha\n");
        do {
          scanf("%d", &alpha);
          if(MCD_R(alpha,26) == 1)  flag = 0;
          else{
            printf("Wrong alpha, please insert a different number\n");
          }
        } while(flag==1);
        printf("Write betha\n");
        scanf("%d", &betha);
        archi = fopen("e.txt","r");
        fgets(buffer,50,archi);
        fclose(archi);

        printf("%s",buffer);
        if(betha >= 26) betha = betha % 26;
        if(betha < 0) betha = betha + 26;
        AEE(alpha,26,&d,&x,&y);
        printf("\nMult_inv = %d\t Add_Inv = %d\n",x,Add_Inv(betha));
        for(i=0;i<50;i++){
          if(buffer[i] >= 'A' && buffer[i] <= 'Z'){
            buffer[i] = buffer[i] - 65;
            //codigo para descifrar
            buffer[i] = (x*(buffer[i] + Add_Inv(betha)))%26;
            if(buffer[i] < 0) buffer[i] = buffer[i] + 26;
            buffer[i] = buffer[i] + 97;
          }
        }
        printf("%s\n",buffer);
        archi = fopen("d.txt","w");
        fputs(buffer,archi);
        fclose(archi);
        bandera = 0;
        break;
      case 'e':
        system("clear");
        //printf("Write the file name\n");
        //scanf("%s", archivo);

        printf("Write alpha\n");
        do {
          scanf("%d", &alpha);
          if(MCD_R(alpha,26) == 1)  flag = 0;
          else{
            printf("Wrong alpha, please insert a different number\n");
          }
        } while(flag==1);

        printf("Write betha\n");
        scanf("%d", &betha);
        archi = fopen("m.txt","r");
        fgets(buffer,50,archi);
        fclose(archi);

        printf("%s",buffer);
        if(betha >= 26) betha = betha % 26;
        if(betha < 0) betha = betha + 26;
        for(i=0;i<50;i++){
          if(buffer[i] >= 'a' && buffer[i] <= 'z'){
            buffer[i] = buffer[i] - 97;
            buffer[i] = (alpha*(buffer[i]) + betha)%26;
            if(buffer[i] < 0) buffer[i] = buffer[i] + 26;
            buffer[i] = buffer[i] + 65;
          }
        }
        printf("%s",buffer);

        for(i=0;i<50;i++){
          if(buffer[i] < 'A' || buffer[i] > 'Z'){
            for(j=0;i+j<50;j++){
              buffer[i+j] = buffer[i+j+1];
            }
          }
        }

        printf("%s\n",buffer);
        archi = fopen("e.txt","w");
        fputs(buffer,archi);
        fclose(archi);
        bandera = 0;
        break;
      default:
        printf("Wrong option\n");
        system("clear");
    }
  } while(bandera == 1);
  return 0;
}

int MCD_R(int a, int b){
  if(b==0)   return a;
  else      return MCD_R(b,a%b);
}

int MCD(int a, int b){
  int r;
  if (a>b){
    r = a;
    a = b;
    b = r;
  }
  r=a%b;
  while(r > 0){
    a = b;
    b = r;
    r = a%b;
  }
  return b;
}

int Add_Inv(int a){
  return (26-a);
}

void AEE(int a, int b, int *d, int *x, int *y){
  int x1,y1;
  if(b==0){
    *d = a;
    *x = 1;
    *y = 0;
  }
  else{
    AEE(b,a%b,d,x,y);
    x1 = *x;
    y1 = *y;
    *x = y1;
    *y = x1 - (a/b)*y1;
  }
}
