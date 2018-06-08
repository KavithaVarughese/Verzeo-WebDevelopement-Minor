function draw()
{

	var canvas = document.getElementById('canvas'); 
	if(canvas.getContext)
	{
    	var context = canvas.getContext('2d');  
    	context.beginPath()
    	context.arc(75,75,75,0,Math.PI*2,true)
    	context.lineWidth = 7
    	context.strokeStyle = '#008000';
    	context.stroke()
    	context.beginPath();
    	context.rect(12,35,125,80)
    	context.lineWidth = 5
    	context.strokeStyle = '#888888';
    	context.stroke();

    	
        context.font = '70pt Calibri';  
        context.strokeStyle = 'black';  
        context.fillText('K', 45, 105); 
	} 
}