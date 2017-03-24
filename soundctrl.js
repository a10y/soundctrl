// CHANGE URL Below
const SLIDER = document.getElementById("ctrl")
const LABEL = document.getElementById("volume")
var saved = 0;

SLIDER.oninput = () => { 
    let volume = SLIDER.value
    LABEL.innerHTML = volume
}

function setVolume() {
    let volume = SLIDER.value
    if (volume === saved) {
        return
    }
    saved = volume
    fetch(`${location.protocol}//${location.hostname}:8001/${volume}`) // Set the volume based off of input
}

// Block from occurring more than once every 100ms
setInterval(setVolume, 300)
