function similarity(s1, s2){
	
	var longer = s1;
	var shorter = s2;
		
	if (s1.length < s2.length) {
		longer = s2;
		shorter = s1;
	}
		
	var longerLength = longer.length;
		
	if (longerLength == 0) {
		return 1.0;
	}
		
	return (longerLength - this.editDistance(longer, shorter)) / parseFloat(longerLength);
		
}

function editDistance(s1, s2) {
	s1 = s1.toLowerCase();
	s2 = s2.toLowerCase();

	var costs = new Array();
	for (var i = 0; i <= s1.length; i++) {
			
		var lastValue = i;
		for (var j = 0; j <= s2.length; j++) {
			if (i == 0)
				costs[j] = j;
			else {
				
				if (j > 0) {
					
					var newValue = costs[j - 1];
					if (s1.charAt(i - 1) != s2.charAt(j - 1))
						newValue = Math.min(Math.min(newValue, lastValue), costs[j]) + 1;
					
					costs[j - 1] = lastValue;
					lastValue = newValue;
						
				}
			}
		}
	if (i > 0)
		costs[s2.length] = lastValue;
	}
		
	return costs[s2.length];
		
}

function openGoogle(){
	window.open("https://google.com", "_blank");
}

function openGitHub(){
	window.open("https://github.com", "_blank");
}

function openIpl(){
	window.open("https://ipl.com", "_blank");
}

class sound
{
       sound;
	
       constructor(src){
               this.sound=document.createElement('audio');
               this.sound.src=src;
               this.sound.setAttribute("preload","auto");
               this.sound.setAttribute("controls","none");
               this.sound.style.display="none";
       }
       
	play(){
               this.sound.play();
       }
       
	stop(){
		this.sound.pause();
       }
	
        decVol(){
              	if(this.volume>=0)
              {
             		this.volume-=20;
              }
       }
       
       incVol(){
		
		if(this.volume<=100)
               {
               	this.volume+=20;
               }
       }
}	
