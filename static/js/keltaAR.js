
function dance(){
	
	waveLeftHand();
	
	setTimeout(function(){
		waveRightHand();
	},1000);
	
}

function explain(){

	document.querySelector('#right-hand').emit('explain-right-hand');
	setTimeout(function(){
		document.querySelector('#left-hand').emit('explain-left-hand');
	},1000);
	
}

function danceLeftLeg(){
	document.querySelector('#left-leg').emit('dance-left-leg');
}

function danceRightLeg(){
	document.querySelector('#right-leg').emit('dance-right-leg');
}
function danceHead(){
	document.querySelector('#head').emit('dance-head');
}

function waveLeftHand(){
	document.querySelector('#left-hand').emit('wave-left-hand');
}

function waveRightHand(){
	document.querySelector('#right-hand').emit('wave-right-hand');
}

function affermationHead(){
	document.querySelector('#head').emit('affermation-head');
}

function negationHead(){
	document.querySelector('#head').emit('negation-head');
}

let parameters2 = {
	onstart:waveLeftHand
};

window.onload = function(){
	
	responsiveVoice.speak("Welcome to Jarvis! I will be in service for you here.","UK English Male", parameters2);
	
};