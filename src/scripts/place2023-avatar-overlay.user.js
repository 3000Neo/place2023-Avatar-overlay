// ==UserScript==
// @name         r/place Avatar Overlay
// @namespace    http://tampermonkey.net/
// @version      5
// @description  try to take over the canvas!
// @author       placeDE Devs
// @match        https://garlic-bread.reddit.com/embed*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=reddit.com
// @updateURL    https://github.com/3000Neo/place2023-Avatar-overlay/raw/main/src/scripts/place2023-avatar-overlay.user.js
// @downloadURL  https://github.com/3000Neo/place2023-Avatar-overlay/raw/main/src/scripts/place2023-avatar-overlay.user.js
// ==/UserScript==

var overlayImage = null;

var imageUrl = "https://github.com/3000Neo/place2023-Avatar-overlay/raw/main/img/overlay.png";

if (window.top !== window.self) {
    window.addEventListener('load', () => {
        const canvasContainer = document.querySelector("garlic-bread-embed").shadowRoot.querySelector("div.layout").querySelector("garlic-bread-canvas").shadowRoot.querySelector("div.container");
        overlayImage = document.createElement("img");
        updateImage();
        overlayImage.style = `position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 1500px;height: 1000px;`;
        canvasContainer.appendChild(overlayImage);
    }, false);
}

function updateImage() {
    overlayImage.src = imageUrl + "?" + Date.now()
}

setInterval(function () {overlayImage.src = imageUrl + "?" + Date.now()}, 30000);