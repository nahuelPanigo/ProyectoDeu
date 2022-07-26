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
function changeSize(font, h1, h2, h3, h4, tour, icon){
  var declaration = document.styleSheets[16].cssRules[0].style;
  var declarationTour = document.styleSheets[17].cssRules[0].style;
  declaration.setProperty('--font-size',font)
  declaration.setProperty('--h1-size',h1)
  declaration.setProperty('--h2-size',h2)
  declaration.setProperty('--h3-size',h3)
  declaration.setProperty('--h4-size',h4)
  declaration.setProperty('--size-icon',icon)
  declarationTour.setProperty('--font-size-tour', tour)
}

function setFontSize(size){
  if (size === 'chico'){
    changeSize('10px', '25px', '20px', '15px', '12px', '2rem','30px')
  } else {
    if (size === 'mediano'){
      changeSize('15px','30px','25px','20px', '18px', '2.5rem', '45px')
    } else {
        changeSize('20px', '40px', '35px', '30px', '25px', '3rem','65px')
    }
  }
}


export{getCookie,createCookie,setProperty,setVal,getCookieValue, changeSize, setFontSize}