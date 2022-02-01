import {getElement as select} from "./getElement.js";
const navToggle = select('.nav-toggle');
const mobileToggle = select('.mobile-toggle');
const closeBtn = select('.close-btn');




//show sidebar
navToggle.addEventListener("click",()=>{
    mobileToggle.classList.toggle('show-sidebar');
})
closeBtn.addEventListener("click",()=>{
    mobileToggle.classList.remove('show-sidebar');
})
