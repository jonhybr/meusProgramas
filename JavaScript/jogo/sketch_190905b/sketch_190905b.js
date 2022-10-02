R = 255;G = 255;B = 255;

function setup() {
createCanvas(800,600);
}


function draw() {

noFill();
background(0);
portao();
botao();

print(cx,cy,bx,by,vm,vmx);


if(cx < 0){
 cx += vm;}
if(cy < 0){
 cy += vm;}
if(cx + cl > window.width){
 cx -= vm;}
if(cy + ca> window.height){
 cy -= vm;}

 if(cx + cl + 3 > pox1 && cx < pox1 + pol){
  vm = vm *-1;
 }
 else {
  vm = 3;
 }

  cx += vmx;cy += vmy;
 
 
cubo();
}
