cx = 32;cy = 32;cl = 32;ca = 32;vmx = 0;vmy = 0;
vm = 3;


function cubo(){
  
 fill(255);
 rect(cx,cy,cl,ca);
 
}

function keyTyped(){
 if (key === 'd'){
  vmx = vm;}
 if (key === 's'){
  vmy = vm;}
 if (key === 'a'){
  vmx = -vm;}
 if (key === 'w'){
  vmy = -vm;}
}

function keyReleased(){
  if (key === 'd'||key === 'a'){
   vmx = 0;}
  if (key === 's'||key === 'w'){
   vmy = 0;}
}
