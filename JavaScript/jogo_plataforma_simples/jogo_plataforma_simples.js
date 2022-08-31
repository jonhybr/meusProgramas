

function setup() {
createCanvas(1500, 300);
frameRate(60);
}

function draw() {

  print(Py,Px,Imx);

  noFill();
  background(0, 80, 150);

  personagem();
  inimigo();
  nuvem();
  solo();
  
  if (Px < 0){Px -= Pmx;}
  if (Py < -10){Py -= Pmy;}
  if (Px + Pl > window.width){Px += Pmx;}
  if (Py + Pa > window.height){Py += Pmy;}
}
