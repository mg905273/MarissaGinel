/*Marissa Ginel
CSC345
Dr. Ajaj

Objective: To design and implement functions to process 2DArrays.*/

#include<stdio.h>

//find max value in array
int max(int array[][100],int rows,int cols){
   int i,j;
   int max = array[0][0];//set the first element as max
   //loop through array and find max
   for(i = 1; i < rows; i++){
       for(j = 1; j < cols; j++){
           if(max < array[i][j]){//assign max if greater than current max
               max = array[i][j];
           }
       }
   }
   return max;
   //returns max
}
int rowSum(int array[][100],int start,int cols){
   int sum = 0,i,j;
   //lopp through 
   for(i = 0; i < cols; i++){
       //sum of rows
       sum += array[start][i];
   }
   //return sum
   return sum;
}
int columnSum(int array[][100],int start,int rows){
   int sum = 0,i;
   //loop thorugh
   for(i = 0; i < rows; i++){ 
       //sum of columns 
       sum += array[i][start];
   }
   //returns sum
   return sum;
}

int isSquare(int rows,int cols){
    //determine if its square
   if(rows==cols)return 1;
   return 0;
}
void displayOutputs(int array[][100],int rows,int cols){
   int i,j;
   //loop through rows
   for(i = 0; i < rows; i++){
       printf("[");
       //loop through cols
       for(j = 0; j < cols; j++){
           //prints value
           printf("%d",array[i][j]);
           //commas
           if(j <= cols-2){
               printf(", ");
           }
       }
       printf("]\n");
   }
}
int main(){
   // declaration
   int rows,cols,i,j;
   //declare arrray
   int array[100][100];
   //welcome message
   printf("Let\'s create a 2Dim array!\n");
   //ask for rows
   printf("\t How many rows? ");
   //scan input
   scanf("%d",&rows);
   //ask for cols
   printf("\t How many columns? ");
   //scan input
   scanf("%d",&cols);
   //new line
   printf("\n");
   //2D array
   for(i = 0; i < rows; i++){
       for(j = 0; j < cols; j++){
           printf("\t enter [%d][%d]: ",i,j);
           scanf("%d",&array[i][j]);
       }
   }
   printf("\n");
   //output displays and calling functions
   printf("\nMaximum value in array: %d \n\n",max(array,rows,cols));
   for(i = 0; i < rows; i++){
       printf("Sum of row %d = %d\n",i+1,rowSum(array,i,cols));
   }
   printf("\n");
   for(i = 0; i < cols; i++){
       printf("Sum of column %d = %d\n",i+1,columnSum(array,i,rows));
   }
   printf("\n");
   if(isSquare(rows,cols)){
       printf("This is a square array.");
   }else{
       printf("This is not a square array.");
   }
   printf("\n\nHere is your 2Dim array:\n");
   displayOutputs(array,rows,cols);
}