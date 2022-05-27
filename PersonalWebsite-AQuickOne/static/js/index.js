let particle;
let array= [];
function setup() {
    let cnv = createCanvas(1500, 900);
 		cnv.parent('myContainer');
//    frameRate(30)
    for(let lcv = 0 ; lcv < 40; lcv++){
            var randomX = random(0,1500)
            console.log(randomX)
            var randomY = random(0,900)
            array.push(new Particles(randomX,randomY))


    }

}

function draw() {
    background(0)
    for(let lcv = 0; lcv < array.length; lcv++){
        array[lcv].appear();
        array[lcv].move();
    }


}

function Particles(randomX,randomY){
    this.x = randomX;
    this.y = randomY;
    this.vx = 0.1
    this.vy = 0;

    this.move = function(){
        this.x += this.vx;
        this.y += this.vy;

    }
    this.appear = function(){
        fill(color(255, 255, 255));
        circle(this.x, this.y, 5);
    }


}