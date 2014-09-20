function RtLineChart (element, n, width, height, margin, name){
  this.n = n;
  this.element = element;
  this.margin = margin;
  
  this.width = width - this.margin.left - this.margin.right,
  this.height = height - this.margin.top - this.margin.bottom;
  
  this.random = d3.random.normal(0, .2);
  this.data = d3.range(this.n).map(function (){return 0;});
  this.x = d3.scale.linear()
    .domain([0, this.n - 1])
    .range([0, this.width]);

var y = d3.scale.linear()
    .domain([-5, 5])
    .range([this.height, 0]);

var that = this;
this.line = d3.svg.line()
    .interpolate("basis")
    .x(function(d, i) { return that.x(i); })
    .y(function(d, i) { return y(d); });

var svg = d3.select(this.element).append("svg")
    .attr("width", this.width + this.margin.left + this.margin.right)
    .attr("height", this.height + this.margin.top + this.margin.bottom)
  .append("g")
    .attr("transform", "translate(" + this.margin.left + "," + this.margin.top + ")");

svg.append("defs").append("clipPath")
    .attr("id", "clip")
  .append("rect")
    .attr("width", this.width)
    .attr("height", this.height);

svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + y(0) + ")")
    .call(d3.svg.axis().scale(this.x).ticks(4).orient("bottom"));

svg.append("g")
    .attr("class", "y axis")
    .call(d3.svg.axis().scale(y).ticks(4).orient("left"));

this.text = svg.append("text")
               .attr("x", 10)
               .attr("y", 10)
               .attr("fill", "green")
               .text("");

this.name = svg.append("text")
               .attr("x", 100)
               .attr("y", 10)
               .attr("fill", "blue")
               .text(name);


this.path = svg.append("g")
    .attr("clip-path", "url(#clip)")
  .append("path")
    .datum(this.data)
    .attr("class", "line")
    .attr("d", this.line);
}

RtLineChart.prototype.tick = function() {
  // push a new data point onto the back
  this.data.push(this.random());

  // redraw the line, and slide it to the left
  this.path
      .attr("d", this.line)
      .attr("transform", "rotate(0)")
      .transition()
      .duration(500)
      .ease("linear")
      .attr("transform", "translate(" + this.x(-1) + ",0)");

  // pop the old data point off the front
  this.data.shift();
}

RtLineChart.prototype.insertVal = function (val){

  this.data.push(val);
  // redraw the line, and slide it to the left
  this.path
      .attr("d", this.line)
      .attr("transform", "rotate(0)")
      .transition()
      .duration(50)
      .ease("linear")
      .attr("transform", "translate(" + this.x(-1) + ",0)");

   this.text.text(Math.round(val*100)/100);

  // pop the old data point off the front
  this.data.shift();
}
