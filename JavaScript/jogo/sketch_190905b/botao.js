 let bx = 100;let by = 100;let ba = 32;bl = 32;
 R = 255;G = 0;B = 0;
function botao(){
  
 fill(R,G,B);
 rect(bx,by,bl,ba);
 
if (cx + cl > 100 && cx < bx + bl && cy + cl > by && cy < by + bl){
 R = 0; G = 255;B = 0;
 }
 else{
  R = 255; G = 0; B = 0;
 }
}
