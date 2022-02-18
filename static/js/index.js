import swiperSlider from "./utils/swiperSlider.js";
import './utils/sidebar.js';

$('document').ready(() =>{



swiperSlider('#main-slider',{slidesPerView: [1],spaceBetween:0,loop:true})

swiperSlider("#swiper-article-1", {slidesPerView: [3], direction: "vertical", loop: true});
swiperSlider("#swiper-article-2", {slidesPerView: [3], direction: "vertical", loop: true});

swiperSlider("#swiper-lesson", {slidesPerView: [1, 2, 3, 4]});
swiperSlider("#swiper-notification", {slidesPerView: [1, 2, 3]});


})
















