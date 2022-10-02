Px = 25;Py = 248;Gr = 4;Pmx = 0;Pmy = 0;Pa = 25; Pl = 25;tiro = 1;


function personagem() {

  fill(255);
  rect(Px, Py += Gr, Pa, Pl);

  Px += Pmx; Py += Pmy;
  
  if (Py < -6){
   Py -= Pmy + 4;
  }
  if (Py == Py - 7){
   Py -= 1;
  }

  if (Py > 252){
   Gr = 0;
  }  else {
   Gr = 4;
  }

  if (Px > 200){
   Gr = 4;
  }

  if (Py > window.height){
   Px =25; Py = 248;
  }

  //Solo colisão
  if (Py > 132 && Py < 141 && Px > 206 && Px < 330 || Py > 192 && Py < 212 && Px > 375 && Px < 500 ){
   Gr = 0;
  }

  //Inimigo colisão
  if (Px - Pl == Ix && Py > 165 && Py < 230 ||
  Px + Pl == Ix && Py > 165 && Py < 230 ||
  Px == Ix && Py > 165 && Py < 230 ||
  Py + Ia > 193 && Py < Iy && Px > Ix && Px < Ix + Il ||
  Py + Ia > 193 && Py < Iy && Px + Pl > Ix && Px < Ix)
  
  {
   Px = 25; Py = 248;
  }

  if (Py == Iy - 25 && Px == Ix){

  }

  if (Py < 175 && Py > 130 && Px > 206 && Px < 330){
   Pmy = 0;
  }
}

function keyTyped() {
 if (key === 'd') {
   Pmx = 2;
 }
 else if (key === 'w') {
   Gr = 0;Pmy -= 8;
 }

 else if (key === 'a') {
   Pmx = -2;
 }
 else if (key === 'e'){
  Gr = 0; Pmy = -1;
 }
 else if (key === 's'){
  Pmy = 2;
 }
}

function keyPressed(){
 if (key == 'd' && key == 'a'){
  Pmx = 0;
 }
}


function keyReleased(){
  if (key === 'd' && Pmx > 0) {
    Pmx = 0;
  }
  if (key === 'a' && Pmx < 0) {
    Pmx = 0;
  }
  if (key === 'w' && Pmy < 0) {
    Pmy = 0;
  }
  if (key === 'e' && Pmy < 0) {
    Pmy = 0;
  }
  if (key === 's' && Pmy > 0){
    Pmy = 0;
  }
}
