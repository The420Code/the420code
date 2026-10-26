(function(){
  var all=document.querySelectorAll('details.sec');
  var ex=document.querySelector('[data-expand]'),co=document.querySelector('[data-collapse]');
  if(ex)ex.addEventListener('click',function(){all.forEach(function(d){d.open=true})});
  if(co)co.addEventListener('click',function(){all.forEach(function(d){d.open=false})});

  function reveal(){var h=location.hash&&document.getElementById(location.hash.slice(1));if(!h)return;var d=h.closest('details');while(d){d.open=true;d=d.parentElement&&d.parentElement.closest('details')}h.scrollIntoView()}
  window.addEventListener('hashchange',reveal);reveal();
})();

(function(){
  try{
    if(!sessionStorage.getItem('v420')){
      sessionStorage.setItem('v420','1');
      fetch('/.netlify/functions/visit-counter',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({path:location.pathname,ref:document.referrer})}).catch(function(){});
    }
  }catch(e){}
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href$=".pdf"]');
    if(!a)return;
    fetch('/.netlify/functions/download-counter',{method:'POST',keepalive:true,headers:{'Content-Type':'application/json'},
      body:JSON.stringify({file:a.getAttribute('href').split('/').pop()})}).catch(function(){});
  },true);
})();
