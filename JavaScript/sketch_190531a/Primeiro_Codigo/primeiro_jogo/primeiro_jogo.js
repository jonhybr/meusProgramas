var x = 50; var y = 50; var vx = 0; var vy = 0;


function setup() {
 createCanvas(800,600);
 background(200);
 
}

x = 0;

function draw() {
  

  
 fill(personagem.cor);
 rect(personagem.x,personagem.y, personagem.l, personagem.a);
  
  
 fill(inimigo.R, 0, 0);
 rect(inimigo.x, inimigo.y, inimigo.l, inimigo.a);
 
 fill(0, 50, 0);
 for (var y = 0; y <= height; y += 33){
  ellipse(x, y, 32, 32);
 }

}
