/*
Marissa Ginel
CSC 345 
Lab 4
This code is to recreate the tortoise and the hare
by implementing functions and processing pointers*/

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <unistd.h>

int randNum(void);
void move(unsigned int *const t, unsigned int *const h);
void displayPos(unsigned int *const t, unsigned int *const h);
//main function to display and call
int main(){
unsigned int tort = 1, hare = 1;
unsigned int *const tpoint = &tort;
unsigned int *const hpoint = &hare;
  
puts("ON YOUR MARK, GET SET");
puts("BANG            !!!!!");
puts("AND THEY'RE OFF  !!!!");

while(tort < 70 && hare < 70){
move(tpoint, hpoint);
displayPos(tpoint, hpoint);
sleep(1);
}

if(tort >= 70 && hare >= 70)
puts("IT'S A TIE!");
else if(tort >= 70)
puts("TORTOISE WINS!!! YAY!!!");
else
puts("HARE WINS. YUCH");

return 0;
}
//random number between/including 1 and 10
int randNum(void){
srand(time(NULL));
return (rand() % 10 + 1);
}

//move positions based off random move
void move(unsigned int *const t, unsigned int *const h){
// move tortoise
int move = randNum();
// fast plod 
if(move >= 1 && move <= 5)
    *t += 3;
// slow plod 
else if(move >= 6 && move <= 8)
    *t += 1;
// slip    
else{
    if(*t > 6)
        *t -= 6;
    else
        *t = 1;
}
// move hare
move = randNum();
// big hop
if(move == 1 || move == 2)
    *h += 9;
// big slip
else if( move == 3){
    if(*h > 12)
        *h -= 12;
    else
        *h = 1;
}
// small hop
else if(move >= 4 && move <=6)
    *h += 1;
// small slip
else if(move == 7 || move == 8){
    if(*h > 2)
        *h -= 2;
    else
        *h = 1;
}
}

// display the current positions
void displayPos(unsigned int *const t, unsigned int *const h){
    for(size_t i = 1; i < 71; i++){
        if(i == *t && i == *h)
            printf("%s", "OUCH!!!");
        else if(i == *t)
            printf("%s", "T");
        else if(i == *h)
            printf("%s", "H");
        else
            putchar(' ');
}putchar('\n');
}