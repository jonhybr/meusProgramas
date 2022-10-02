Nx = 45;
Ny = 50;
Nl = 25;
Na = 25;

function nuvem(){
 fill(255);
 ellipse(Nx ,Ny, Na, Nl);
 ellipse(Nx + 30 ,Ny, Na, Nl);
 ellipse(Nx + 15, Ny - 1, Na + 5, Nl + 5);
}


function solo() {

 fill(130, 44 ,8);
 rect(0, 280, 200, 20);
 fill(0, 255, 0);
 rect(0, 280, 200, 5);

 fill(130, 44 ,8);
 rect(230, 160, 100, 20);
 fill(0, 255, 0);
 rect(230, 160, 100, 5);

 fill(130, 44 ,8);
 rect(400, 220, 100, 20);
 fill(0, 255, 0);
 rect(400, 220, 100, 5);

}
