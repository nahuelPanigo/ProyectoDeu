function getCookie(name){
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return true;
    return false;
  }

function getCookieValue(name){
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    try{
      return parts[1];
    }catch{
      return null
    }
  }

function createCookie(name,value) {
      var date = new Date();
      date.setTime(date.getTime()+(10*24*60*60*1000));
      var expires = "; expires="+date.toGMTString();
      document.cookie = name+"="+value+expires+"; path=/"
    }
function setProperty(colorback,colorprimary,colorbutton,colorcuadros){
      var declaration = document.styleSheets[16].cssRules[0].style;
      declaration.setProperty('--back-color', colorback);
      declaration.setProperty('--primary-color', colorprimary);
      declaration.setProperty('--cuadros-color', colorcuadros);
      declaration.setProperty('--button-color', colorbutton);
    }
function setVal(tema){
  if(tema === 'oscuro'){
    setProperty('rgb(0, 0, 24)','#95b3d1','#044d39','rgba(19, 35, 47, 0.9)')
  }else{
    setProperty('#c3c3d6','#000000','#8a91b7','rgb(145 170 189 / 51%)')
  }
}


export{getCookie,createCookie,setProperty,setVal,getCookieValue}