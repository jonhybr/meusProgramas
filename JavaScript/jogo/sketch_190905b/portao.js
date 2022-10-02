pox1 = 500;poy1 = 0;pol = 50;poa1 = 300;
pox2 = 500;poy2 = 300;poa2 = 300;




function portao(){
  
 fill(255);
 rect(pox1,poy1,pol,poa1);
 rect(pox2,poy2,pol,poa2);
 
 if (cx + cl > bx && cx < bx + bl && cy + cl > by && cy < by + bl){
  poy1 = -100; poy2 = 400;
 }
 

}
