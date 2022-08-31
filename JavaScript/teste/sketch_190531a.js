function setup() {
  createCanvas(600, 400);
  background(255);
}


function draw() {
 rect (100,100,100,100);
 var CorA1 = random (0, 255); 
 var CorA2 = random (0, 255); 
 var CorA3 = random (0, 255); 
 fill(CorA1,CorA2,CorA3);
 ellipse(mouseX, mouseY, 32, 32);
}
