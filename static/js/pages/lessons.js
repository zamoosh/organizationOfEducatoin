import './../utils/menuSidebar.js';
import swiperSlider from "./../utils/swiperSlider.js";
import {getElement as select} from "./../utils/getElement.js";
import "./../utils/fileUploader.js"
import {sendAjax} from "../utils/ajax.js";


//lesson page
const numbersOfSliders = select('.swiper-slide').length;
console.log(numbersOfSliders);
swiperSlider("#swiper-lesson", {slidesPerView: [1, 2, 3, 4], rows: 2, sliderNumbers: numbersOfSliders, loop: false});
$(document).ready(function () {
    const form = $(".form")[0];
    sendAjax(null, form);
});


