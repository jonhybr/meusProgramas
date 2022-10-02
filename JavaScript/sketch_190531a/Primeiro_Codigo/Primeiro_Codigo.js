function setup() {
 createCanvas(700, 460);
 
}

let Nave = {
  
  X : 10,
  Y : 10,
  A : 32,
  L : 32,
  Cor : 255,
  
};


function draw() {
  
 clear();
 background(0);
 
 noStroke();
 
 rect(Nave.X, Nave.Y, Nave.L, Nave.A);
 
 fill(255);
 textSize(32);
 text('Hello', 350, 250);
 stroke(100);
 strokeWeight(10);
 fill(255);
 ellipse(mouseX, mouseY, 32, 32);
}

function KeyPressed() {
  if (key == 'd'){
    
  }


}
