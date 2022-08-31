Px = 25;
Py = 248;
Gr = 4;
Pmx = 0;
Pmy = 0;

function personagem() {
  fill (255,0,0);
  rect(Px, Py += Gr, 25, 25);
  Px += Pmx;
  Py += Pmy;
  
  if (Py > 252){
   Gr = 0;
  }
  else {
   Gr = 4;
  }
  if (Px > 200){
   Gr = 4;
  }
  if (Py > 330){
   Px =25; Py = 248; 
  }
  if (Py > 130 && Py < 180 && Px > 210 && Px < 330){
   Gr = 0;
  }

 

}



function keyTyped() {
 if (key === 'd') {
   Pmx = 2;
 }
 if (key === 'w') {
   Gr = 0;Pmy -= 8;
 }
 if (key === 'a') {
   Pmx = -2;
 }
 if (key === 'a' && key === 'd'){
   Pmx = 0;
 }
}


function keyReleased(){
 if (key === 'd'){
  Pmx = 0;
 }
 if (key === 'w'){
  Pmy = 0;
 }
 if (key === 'a'){
  Pmx = 0;
 }
}
