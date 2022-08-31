x = 49; y = 10; nl = 32; na = 32; vmx = 0; vmy = 0;


function setup() {
  createCanvas(400, 400);
}

function vitoria() {
  fill(0, 255, 0);
  rect(300 ,200 - 20, 32, 32 );
}

function barrer() {
  
 fill(255, 0, 0); 
 rect (100, 0, 32, height); 
 rect (0 , 0 , 32, height); 
  
}


function nave(){
  
  x += vmx;
  y += vmy;
  fill(0);
  rect(x, y, nl,na);
  
}




function keyTyped() {
  if (key === 'd') {
  vmx = 5;
  }
  if (key === 's') {
  vmy = 5; 
  }
  if (key === 'a') {
  vmx = - 5; 
  }
  if (key === 'w') {
  vmy = - 5; 
  }
  if (key === 'd' && x > 99 && x < 133 && y > 0 && y < height) {
  x = 10; y = 10;
  }
   if (key === 'a' && x < 1 && y < height) {
  x = 49; y = 10;
  }
}

function keyReleased() {
  if (key === 'd' && vmx > 0) {
    vmx = 0; 
  }
  if (key === 's' && vmy > 0) {
    vmy = 0; 
  }
  if (key === 'a' && vmx < 0) {
    vmx = 0; 
  }
  if (key === 'w' && vmy < 0) {
    vmy = 0; 
  } 
}


function draw() {
   background(220);
 
  barrer();
  nave();
  vitoria();
  
  if (x > 99 && x < 133 && y > 0 && y < height) {
 
    vmx -= vmx; vmy -= vmy;
    fill(0); 
    textSize(32);
    text('Game Over', 150, 32);
    }
  
  if (x < 1) {
     vmx -= vmx; vmy -= vmy;
    fill(0); 
    textSize(32);
    text('Game Over', 150, 32);
  }
  
  if (x > 134) {
   fill(255, 0 ,0) 
   textSize(32);
   text('Hacker', 150, 32)
  }
  
  if (x > 298 && x < 332 && y > 179 && y < 220) {
   stroke(0);
   fill (50 , 255, 50);
   textSize(16);
   text('Parabens você não ganhou nada', 150, 100)
  }
 
}
