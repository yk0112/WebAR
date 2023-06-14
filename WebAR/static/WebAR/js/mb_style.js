var innerImageURL = null
var fullMarkerURL = null

document.querySelector('#fileinput').addEventListener('change', function(){
       var file = this.files[0];
      imageName = file.name
      // remove file extension
      imageName = imageName.substring(0, imageName.lastIndexOf('.')) || imageName
  
      // debugger

      var reader = new FileReader();
      reader.onload = function(event){
          innerImageURL = event.target.result
          updateFullMarkerImage()
    generatPattURL()
      };
     reader.readAsDataURL(file);
  })


document.querySelector('#buttonDownloadFullImage').addEventListener('click', function(){
      if( innerImageURL === null ){
             alert('upload a file first')
             return
       }
      var domElement = window.document.createElement('a');
      domElement.href = fullMarkerURL;
      domElement.download = "pattern-" + (imageName || 'marker') + '.png';
      document.body.appendChild(domElement)
      domElement.click();
      document.body.removeChild(domElement)
  })

function updateFullMarkerImage(){
   // get patternRatio
   var patternRatio = 50/100
   var imageSize = 512
   var borderColor = "black"

   function hexaColor(color) {
       return /^#[0-9A-F]{6}$/i.test(color);
   };

   var s = new Option().style;
   s.color = borderColor;
     if (borderColor === '' || (s.color != borderColor && !hexaColor(borderColor))) {
       borderColor = 'black';
   }

    THREEx.ArPatternFile.buildFullMarker(innerImageURL, patternRatio, imageSize, borderColor, function onComplete(markerUrl){
      fullMarkerURL = markerUrl

      var fullMarkerImage = document.createElement('img')
      fullMarkerImage.src = fullMarkerURL

      // put fullMarkerImage into #imageContainer
      var container = document.querySelector('#imageContainer')
      while (container.firstChild) container.removeChild(container.firstChild);
      container.appendChild(fullMarkerImage)
   })
}


function generatPattURL() {
 if( innerImageURL === null ){
      alert('upload a file first')
      return
  }
 console.assert(innerImageURL)
   var image = new Image;
 image.onload = function() {
  var patternFileString = THREEx.ArPatternFile.encodeImage(image);
  var domElement = window.document.createElement('a');
  domElement.href = window.URL.createObjectURL(new Blob([patternFileString], {type: 'text/plain'}));
  document.getElementById('pattURL').value = domElement.href;
 }
 image.src = innerImageURL;
}
