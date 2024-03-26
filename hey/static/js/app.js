VANTA.TOPOLOGY({
    el: ".anim",
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.00,
    scaleMobile: 1.00
  })

document.getElementById('showInputButton').addEventListener('click', function() {
    document.getElementById('inputField').classList.toggle('visible');
    document.getElementById('showInputButton').classList.toggle('hidden');
    document.getElementById('c1').classList.toggle('hidden');
});


