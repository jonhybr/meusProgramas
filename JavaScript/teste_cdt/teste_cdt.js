var personage;

function setup() {
createCanvas(600, 400);
personagem = new Personagem();
}


function draw() {
 background(100);
 personagem.show();
}

function keyPressed(){
 if (key === 'd'){
  personagem.move(5);
 }
 else if (key === 'a'){
  personagem.move(-5);
 }
}
