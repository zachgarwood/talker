function initTouchListeners() {
    console.log("starting init");
    var link_elements = document.getElementsByClassName("pictograms");
    for(var i = 0; i < link_elements.length; i++)
    {
        var el = link_elements.item(i);
        el.addEventListener("touchstart", function(){handleClick(this);}, false);
        el.addEventListener("click", function(){handleClick(this);}, false);
        // use the data-pictogram-text attribute from the HTML
        console.log("added listeners to "+el.dataset.pictogramText);
        // Other touch events:
        // el.addEventListener("touchstart", handleClick, false);
        // el.addEventListener("touchend", handleEnd, false);
        // el.addEventListener("touchcancel", handleCancel, false);
        // el.addEventListener("touchmove", handleMove, false);
    }
    console.log("initialized.");
}

function handleClick(el) {
    var audio = document.createElement('audio');
    audio.setAttribute("src", el.dataset.pictogramAudioUrl);
    audio.play();
    console.log("clicked "+el.dataset.pictogramText);
}

initTouchListeners();
