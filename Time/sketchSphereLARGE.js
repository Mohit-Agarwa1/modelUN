let sketch = function(p) {
  let rows = Math.trunc( (window.innerHeight*window.innerWidth)/35000 );;
  let radius = Math.trunc( (window.innerHeight*window.innerWidth)/3500);
  let min_length = 45;
  let max_length = 105;
  let space = 15;
  let stripes = [];
  let colors;
  console.log(rows,radius,min_length,max_length,space);
  p.setup = function() {

    let WIN_HEIHGT_SET_MOHIT = window.innerHeight *0.85
    let WIN_WIDTHH_SET_MOHIT = window.innerWidth *0.85
    p.createCanvas(WIN_WIDTHH_SET_MOHIT,WIN_HEIHGT_SET_MOHIT);
    p.canvas.style = "position: absolute; top: 0px; left: 0px; right: 0px; bottom: 0px";
    p.stroke(255);
    p.strokeWeight(14);
    //p.noLoop();

    colors = [
      p.color(142,192,124),
      p.color(250,189,47),
      p.color(251,71,44),
      p.color(211,134,147),
      p.color(49,69,80),
      p.color(054, 057, 059),
      p.color(202, 207, 214),
      p.color(081, 118, 100),
      p.color(053, 079, 082),
      p.color(219, 138, 135)
    ];

    for (var i = 0; i < rows; i++) {
      let ypos = ((i + .5)/rows) * (radius * 2) - radius;
      let row_length = get_row_length(ypos);
      add_stripe_row(ypos, row_length);
    }
  }

  p.draw = function() {
    p.clear();
    p.translate(p.width / 2, p.height / 2);
    for (var row in stripes) {
      for(var s in stripes[row]){
        var stripe = stripes[row][s];
        let length = get_row_length(stripe.y);
        if(!is_outside_circle(stripe, length)){
          p.stroke(stripe.color);
          p.line(p.max((stripe.start+space), -length), stripe.y, p.min((stripe.end-space), length), stripe.y);
        } else if (stripe.start > length){
            stripes[row].splice(s,1);
            let s_length = p.random(min_length,max_length);
            let end = stripes[row][0].start;
            let start = end - s_length;
            stripes[row].unshift({y:stripe.y, start:start, end:end, color:colors[p.floor(p.random(10))]});
        }
          let startx = p.constrain(stripe.start, -length, length);
          let endx = p.constrain(stripe.end, -length, length);
          let startspeed = p.sqrt(2) - p.sqrt(stripe.y * stripe.y + startx * startx) / radius;
          let endspeed = p.sqrt(2) - p.sqrt(stripe.y * stripe.y + endx * endx) / radius;
          stripe.start += startspeed;
          stripe.end += endspeed;

      }
    }
  }

  function get_row_length(ypos) {
    if ((radius * radius) < (ypos * ypos)) return 0;
    return p.sqrt((radius * radius) - (ypos * ypos));
  }

  function is_outside_circle(stripe, length) {
    return stripe.end-space < -length || stripe.start+space > length;
  }

  function add_stripe_row (ypos, row_length) {
    let row = [];
    let length = p.random(min_length,max_length);
    let start = -1000 + p.random(min_length,max_length);
    let end = start + length;
    while (end < -row_length) {
      row.push({y:ypos, start:start, end:end, color:colors[p.floor(p.random(10))]});
      length = p.random(min_length,max_length);
      start = end;
      end = start + length;
    }
    stripes.push(row);
  }

}

new p5(sketch);
