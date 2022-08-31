Ix = 400; Iy = 194; Ia = 25; Il = 25;Imx = 0; Imy = 0;

function inimigo() {
 fill(255, 0, 0); 
 rect(Ix += Imx, Iy += Imy, Ia, Il);

 if (Ix < 401){
   
  Imx = 2;
  
 }
 if (Ix > 475){
   
  Imx = - 2;

 }

}
