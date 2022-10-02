x = 100; y = 100; cor = 255;


function setup() {
 createCanvas(800, 600);
}

function mouseClicked(){
  if (mouseIsClicked && mouseX > x && mouseX < x + 50 && mouseY > y && mouseY < y + 50){
  cor = 0;
  x += mouseX;
  y += mouseY;
  }
}

function draw() {
  fill(cor);
  rect(x, y, 50, 50);

}
