/*Validar que la llave esta dentro del alfabeto y en caso
de que no sea asi, mostrar el proceso de reduccion de la llave*/
#include <stdio.h>

int main() {
  char opcion;
  char archivo[50],buffer[50];
  FILE* archi;
  int bandera=1,key,i,j;
  do {
    printf("Choose an option:\n");
    printf("Push e to encrypt.\n");
    printf("Push d to decrypt.\n");
    fflush(stdin);
    scanf("%c",&opcion);
    switch (opcion) {
      case 'd':
        //system("cls");
        printf("Write the file name\n");
        scanf("%s", archivo);
        printf("Push the key\n");
        scanf("%d", &key);
        archi = fopen(archivo,"r");
        fgets(buffer,50,archi);
        fclose(archi);

        printf("%s\n",buffer);
        if(key >= 26) key = key % 26;
        if(key < 0) key = key + 26;
        for(i=0;i<50;i++){
          if(buffer[i] >= 'A' && buffer[i] <= 'Z'){
            buffer[i] = buffer[i] - 65;
            buffer[i] = (buffer[i]+(26-key)) %26;
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
        //system("cls");
        printf("Write the file name\n");
        scanf("%s", archivo);
        printf("Push the key\n");
        scanf("%d", &key);
        archi = fopen(archivo,"r");
        fgets(buffer,50,archi);
        fclose(archi);

        printf("%s\n",buffer);
        if(key >= 26) key = key % 26;
        if(key < 0) key = key + 26;
        for(i=0;i<50;i++){
          if(buffer[i] >= 'a' && buffer[i] <= 'z'){
            buffer[i] = buffer[i] - 97;
            buffer[i] = (buffer[i] + key )%26;
            if(buffer[i] < 0) buffer[i] = buffer[i] + 26;
            buffer[i] = buffer[i] + 65;
          }
        }
        printf("%s\n",buffer);

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
        //system("pause");
        //system("cls");
    }
  } while(bandera == 1);
  return 0;
}
