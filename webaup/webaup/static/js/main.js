const navigation = document.querySelector('[data-navigation]');
const mobileNavigation = navigation.querySelector('[data-mobile-navigation]');
const body = document.querySelector('body');
const mobileNavigationToggle = navigation.querySelector(
  '[data-mobile-navigation-toggle]',
);

function toggleMobileNavigation() {
  if (mobileNavigation.hidden) {
    body.classList.add('no-scroll');
    mobileNavigation.hidden = false;
    mobileNavigationToggle.setAttribute('aria-expanded', 'true');
  } else {
    body.classList.remove('no-scroll');
    mobileNavigation.hidden = true;
    mobileNavigationToggle.setAttribute('aria-expanded', 'false');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  mobileNavigationToggle.addEventListener('click', () => {
    toggleMobileNavigation();
  });
});

function map_init_basic (map, options) {
  L.marker([-7.937980684863552, -34.877658401127235])
  .addTo(map)
  map.on('click', function redirectPaulista(){
      window.location.href="locations/paulista";
      
  });
  
  L.marker([-8.29316784386745, -35.983504001363464])
  .addTo(map) 
  map.on('click', function redirectSaoJose(){
     window.location.href="locations/caruaru";
  });
  
  L.marker([-8.419704518568702, -37.05587860053689])
  .addTo(map) 
  map.on('click', function (){
      window.location.href="locations/arcoverde";
  })
}