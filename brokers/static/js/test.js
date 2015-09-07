var testAnim = function(){
  var path4 = document.querySelector('.test #fillpath');
  var totalLength4 = path4.getTotalLength();
  var anchorPoints4 = [1249, 884, 542, 10 , 0];
  var fillpath4 = Snap('.test #fillpath');
  fillpath4.attr({
    "stroke-dasharray": ""+totalLength4+" "+totalLength4+"",
    "stroke-dashoffset": totalLength4
  });
  nextStep(fillpath4, anchorPoints4, 0, testAnimations);
}

var testAnimations = function testAnimations(fillpath4 , anchorPoints4 , index4){
	index4++;
	if(index4 == 1){
    var x = 1;
    var bubble = setInterval(function(){
      if(x == 1){
        Snap("#blue_x5F_bubble").attr({"display":"inline"});
      } else if(x == 2){
        Snap("#yellow_x5F_bubble").attr({"display":"inline"});
      }else {
        Snap("#tooltip_x5F_1").attr({"display":"inline"});
        clearInterval(bubble);
      }
      x++;
    } ,500);
		nextStep(fillpath4, anchorPoints4, index4, testAnimations);
	} 
	if(index4 == 2){
    var x = 1;
    var graph = setInterval(function(){
      if(x == 1){
        Snap("#graph-arrow").attr({"display":"inline"});
      }else if(x == 2){
        Snap("#points_x5F_graph").attr({"display":"inline"});
      }else {
        Snap("#tooltip_x5F_2").attr({"display":"inline"});
        clearInterval(graph);
      }
      x++;  
    } , 500);
    nextStep(fillpath4, anchorPoints4, index4, testAnimations);
	}
	if(index4 == 3){
    var x = 1;
    var player_video = setInterval(function(){
      if(x == 1){
        Snap("#stop").attr({"display":"none"});
        Snap("#player_x5F_btn").animate({transform:'t75'},1200);
        Snap("#play").attr({"display":"inline"} ,200);
        Snap("#one").attr({"display":"inline"} , 200);
      }else if(x == 2){
        Snap("#two").attr({"display":"inline"} , 200);
      }else if(x == 3){
        Snap("#three").attr({"display":"inline"} , 200);
      }else{
        Snap("#tooltip_x5F_3").attr({"display":"inline"});
        nextStep(fillpath4, anchorPoints4, index4, testAnimations);
        clearInterval(player_video);
      }
      x++;
    } , 500);
	}
	if(index4 == 4){
    Snap("#tooltip_x5F_4").attr({"display":"inline"});
    nextStep(fillpath4, anchorPoints4, index4, testAnimations);
	}
}

var nextStep = function(fillpath4, anchorPoints4, index4, testAnimations) {
  fillpath4.animate({
    "stroke-dashoffset": anchorPoints4[index4]
  }, 1000, null, function(){
    testAnimations(fillpath4, anchorPoints4, index4);
  });
}