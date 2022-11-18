// create navigation map canvas
const map = document.getElementById('navmap'); 
const myContext = map.getContext('2d');
var imageObj = new Image();
const width_map  = 950
const height_map = 788.3
const YARD_WIDTH_M = 39
const YARD_LENGTH_M = 47
// starting points in pixels on the nav map
const X_START_PX = 324
const Y_START_PX = 711 
const map_path = document.getElementById('navmap_path'); 
const pathContext = map_path.getContext('2d');
const map_pos = document.getElementById('navmap_position'); 
const posContext = map_pos.getContext('2d');
console.log("canvas width " + map.width)
console.log("canvas height " + map.height)
imageObj.src = image_url;
imageObj.onload = function() {
    // nav map background 
    myContext.drawImage(imageObj, 0, 0, width_map, height_map);
    // starting point (light green rectangle)
    myContext.fillStyle = 'rgba(0, 255, 0, 0.5)'; 
    myContext.fillRect(X_START_PX, Y_START_PX, 10, 10);  // x, y, width, height
    // AR tag
    const Wt_X = X_START_PX + 0*width_map/YARD_WIDTH_M;
    const Wt_Y = Y_START_PX - 9*height_map/YARD_LENGTH_M;
    myContext.fillStyle = 'rgba(0, 0, 255, 0.5)'; 
    myContext.fillRect(Wt_X, Wt_Y, 10, 10);  
    // way points for NAV task 
    // #1
    const WH_X = X_START_PX + 14.56*width_map/YARD_WIDTH_M;
    const WH_Y = Y_START_PX - 16.58*height_map/YARD_LENGTH_M;
    myContext.fillStyle = 'rgba(255, 0, 0, 0.5)'; 
    myContext.fillRect(WH_X, WH_Y, 10, 10);  
    //let x_px = X_START_PX - y_next*width_map/YARD_WIDTH_M;
    //let y_px = START_Y_PX - x_next*height_map/YARD_LENGTH_M;
    // #2
    const WG_X = X_START_PX + 10.63*width_map/YARD_WIDTH_M; 
    const WG_Y = Y_START_PX - 5.54*height_map/YARD_LENGTH_M; 
    myContext.fillStyle = 'rgba(255, 0, 0, 0.5)'; 
    myContext.fillRect(WG_X, WG_Y, 10, 10);
    // #3
    const WQ_X = X_START_PX + (-3.12)*width_map/YARD_WIDTH_M; 
    const WQ_Y = Y_START_PX - 12.75*height_map/YARD_LENGTH_M; 
    myContext.fillStyle = 'rgba(255, 0, 0, 0.5)'; 
    myContext.fillRect(WQ_X, WQ_Y, 10, 10);
    // #4
    const WC_X = X_START_PX + 3.67*width_map/YARD_WIDTH_M; 
    const WC_Y = Y_START_PX - 19.00*height_map/YARD_LENGTH_M;  
    myContext.fillStyle = 'rgba(255, 0, 0, 0.5)'; 
    myContext.fillRect(WC_X, WC_Y, 10, 10); 
    //myContext.fillStyle = 'rgba(0, 255, 0, 0.5)'; 
    myContext.fillStyle = 'rgba(247, 202, 24, 1)'; 
    /* ===== DRAWING THE GRID + AXES ON THE NAV MAP ===== */
    // https://usefulangle.com/post/19/html5-canvas-tutorial-how-to-draw-graphical-coordinate-system-with-grids-and-axis 
    
    myContext.fillStyle = 'rgba(247, 202, 24, 1)'; 
    // move cursor to the starting point, to begin drawing line 
    pathContext.beginPath(); 
    pathContext.moveTo(X_START_PX, Y_START_PX); // first line => moveTo()
    var grid_size = 21.27;
    var x_axis_distance_grid_lines = 33;
    var y_axis_distance_grid_lines = 15;
    var x_axis_starting_point = { number: 1, suffix: '' };
    var y_axis_starting_point = { number: 1, suffix: '' };
    // canvas width
    var canvas_width = map.width-440;
    // canvas height
    var canvas_height = map.height-30;
    // no of vertical grid lines
    var num_lines_x = Math.floor(canvas_height/grid_size);
    // no of horizontal grid lines
    var num_lines_y = Math.floor(canvas_width/grid_size);
    // Draw grid lines along X-axis
    for(var i=0; i<=num_lines_x; i++) {
        myContext.beginPath();
        myContext.lineWidth = 1;
        
        // If line represents X-axis draw in different color
        if(i == x_axis_distance_grid_lines) 
            myContext.strokeStyle = "#000000";
        else
            myContext.strokeStyle = "#e9e9e9";
        
        if(i == num_lines_x) {
            myContext.moveTo(0, grid_size*i);
            myContext.lineTo(canvas_width, grid_size*i);
        }
        else {
            myContext.moveTo(0, grid_size*i+0.5);
            myContext.lineTo(canvas_width, grid_size*i+0.5);
        }
        myContext.stroke();
    }
    // Draw grid lines along Y-axis
    for(i=0; i<=num_lines_y; i++) {
        myContext.beginPath();
        myContext.lineWidth = 1;
        
        // If line represents Y-axis draw in different color
        if(i == y_axis_distance_grid_lines) 
            myContext.strokeStyle = "#000000";
        else
            myContext.strokeStyle = "#e9e9e9";
        
        if(i == num_lines_y) {
            myContext.moveTo(grid_size*i, 0);
            myContext.lineTo(grid_size*i, canvas_height);
        }
        else {
            myContext.moveTo(grid_size*i+0.5, 0);
            myContext.lineTo(grid_size*i+0.5, canvas_height);
        }
        myContext.stroke();
    }
    myContext.translate(y_axis_distance_grid_lines*grid_size, x_axis_distance_grid_lines*grid_size);
// Ticks marks along the positive X-axis
for(i=1; i<(num_lines_y - y_axis_distance_grid_lines); i++) {
    myContext.beginPath();
    myContext.lineWidth = 1;
    myContext.strokeStyle = "#000000";
    // Draw a tick mark 6px long (-3 to 3)
    myContext.moveTo(grid_size*i+0.5, -3);
    myContext.lineTo(grid_size*i+0.5, 3);
    myContext.stroke();
    // Text value at that point
    myContext.font = '9px Arial';
    myContext.textAlign = 'start';
    myContext.fillText(x_axis_starting_point.number*i + x_axis_starting_point.suffix, grid_size*i-2, 15);
}
// Ticks marks along the negative X-axis
for(i=1; i<y_axis_distance_grid_lines; i++) {
    myContext.beginPath();
    myContext.lineWidth = 1;
    myContext.strokeStyle = "#000000";
    // Draw a tick mark 6px long (-3 to 3)
    myContext.moveTo(-grid_size*i+0.5, -3);
    myContext.lineTo(-grid_size*i+0.5, 3);
    myContext.stroke();
    // Text value at that point
    myContext.font = '9px Arial';
    myContext.textAlign = 'end';
    myContext.fillText(-x_axis_starting_point.number*i + x_axis_starting_point.suffix, -grid_size*i+3, 15);
}
// Ticks marks along the positive Y-axis
// Positive Y-axis of graph is negative Y-axis of the canvas
for(i=1; i<(num_lines_x - x_axis_distance_grid_lines); i++) {
    myContext.beginPath();
    myContext.lineWidth = 1;
    myContext.strokeStyle = "#000000";
    // Draw a tick mark 6px long (-3 to 3)
    myContext.moveTo(-3, grid_size*i+0.5);
    myContext.lineTo(3, grid_size*i+0.5);
    myContext.stroke();
    // Text value at that point
    myContext.font = '9px Arial';
    myContext.textAlign = 'start';
    myContext.fillText(-y_axis_starting_point.number*i + y_axis_starting_point.suffix, 8, grid_size*i+3);
}
// Ticks marks along the negative Y-axis
// Negative Y-axis of graph is positive Y-axis of the canvas
for(i=1; i<x_axis_distance_grid_lines; i++) {
    myContext.beginPath();
    myContext.lineWidth = 1;
    myContext.strokeStyle = "#000000";
    // Draw a tick mark 6px long (-3 to 3)
    myContext.moveTo(-3, -grid_size*i+0.5);
    myContext.lineTo(3, -grid_size*i+0.5);
    myContext.stroke();
    // Text value at that point
    myContext.font = '9px Arial';
    myContext.textAlign = 'start';
    myContext.fillText(y_axis_starting_point.number*i + y_axis_starting_point.suffix, 8, -grid_size*i+3);
}
};