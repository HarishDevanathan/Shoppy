let profile = document.getElementById('profile-div');
let product = document.getElementById('product-div');
let prodimg = document.getElementById('product-image');
let price = document.getElementById('price-div');
let all=document.querySelector('*');
all.classList.add('mt-3');
function centerclasses() {
    let width = window.innerWidth;
    console.log(width);

    if (width < 770) {
        profile.classList.add('text-center');
        product.classList.add('text-center');
        prodimg.classList.remove('prod-image');
        price.classList.add('price');
        
    } else { 
        profile.classList.remove('text-center');
        product.classList.remove('text-center'); 
        prodimg.classList.add('prod-image');
        price.classList.remove('price');
    }
}

centerclasses();

window.addEventListener('resize', centerclasses);
