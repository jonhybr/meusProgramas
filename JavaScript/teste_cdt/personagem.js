function Personagem(){
 this.x = width/2;
 
  this.show = function(){
   fill(255,0,0);
   rect(this.x, height-20, 20, 20);
  }
  
  this.move = function(dir){
   this.x += dir;
  }
}
