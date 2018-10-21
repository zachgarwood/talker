function initTouchListeners() {
    console.log("starting init");
    var link_elements = document.getElementsByClassName("words");
    for(var i = 0; i < link_elements.length; i++)
    {
        var el = link_elements.item(i);
        var word = el.dataset.word; // use the data-word attribute from the HTML
        el.addEventListener("touchstart", function(){handleClick(this);}, false);
        el.addEventListener("click", function(){handleClick(this);}, false);
        console.log("added listeners to "+word);
        // Other touch events:
        // el.addEventListener("touchstart", handleClick, false);
        // el.addEventListener("touchend", handleEnd, false);
        // el.addEventListener("touchcancel", handleCancel, false);
        // el.addEventListener("touchmove", handleMove, false);
    }
    console.log("initialized.");
}

function handleClick(el) {
    var word = el.dataset.word;
    var audio = document.createElement('audio');
    audio.setAttribute("src", "../static/audio/"+word+".m4a");
    audio.play();
    console.log("clicked "+word);
}

initTouchListeners();
