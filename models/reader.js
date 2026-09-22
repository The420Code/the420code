(function(){
  var all=document.querySelectorAll('details.sec');
  var ex=document.querySelector('[data-expand]'),co=document.querySelector('[data-collapse]');
  if(ex)ex.addEventListener('click',function(){all.forEach(function(d){d.open=true})});
  if(co)co.addEventListener('click',function(){all.forEach(function(d){d.open=false})});
  // a link to #section-or-switch opens the section that holds it
  function reveal(){var h=location.hash&&document.getElementById(location.hash.slice(1));if(!h)return;var d=h.closest('details');while(d){d.open=true;d=d.parentElement&&d.parentElement.closest('details')}h.scrollIntoView()}
  window.addEventListener('hashchange',reveal);reveal();
})();
