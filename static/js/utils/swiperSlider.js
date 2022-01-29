export default function swiperSlider(DOMID, {
    slidesPerView = [3],
    direction = "horizontal",
    loop = false,
    spaceBetween = 15,
    rows = 1,
    delay = 2000
}) {
    new Swiper(`${DOMID} .swiper`, {
        direction,
        slidesPerView: slidesPerView[0],
        grid: {
            rows: rows,
        },
        spaceBetween,

        loop,
        loopFillGroupWithBlank: true,
        pagination: {
            el: `${DOMID} .swiper-pagination`,
            clickable: true,

        },

        autoplay: {
            delay,
            disableOnInteraction: false,
        },


        navigation: {
            nextEl: `${DOMID} .swiper-button-next`,
            prevEl: `${DOMID} .swiper-button-prev`,
        },
        breakpoints: {
            768: {
                slidesPerView: slidesPerView[1] ? slidesPerView[1] : slidesPerView[slidesPerView.length - 1],


            },
            992: {
                slidesPerView: slidesPerView[2] ? slidesPerView[2] : slidesPerView[slidesPerView.length - 1],


            },
            1200: {
                slidesPerView: slidesPerView[3] ? slidesPerView[3] : slidesPerView[slidesPerView.length - 1],
            grid:{
                    rows:1,
            },

            }
        }
    });
}
