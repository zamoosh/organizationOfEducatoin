export default function swiperSlider(DOMID, {
    slidesPerView = [3],
    direction = "horizontal",
    loop = false,
    spaceBetween = 15,
    rows = 1,
    delay = 2000,
    sliderNumbers = 1,

}) {
    const swiper = new Swiper(`${DOMID} .swiper`, {
        direction,
        slidesPerView: slidesPerView[0],
        grid: {
            rows: sliderNumbers > slidesPerView[0] ? rows : 1,
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
                slidesPerView: getSlidersPerViews(slidesPerView, 1),
                grid: {
                    rows: sliderNumbers > getSlidersPerViews(slidesPerView, 1) ? rows : 1,
                }

            },
            992: {
                slidesPerView: getSlidersPerViews(slidesPerView, 2),
                grid: {
                    rows: sliderNumbers > getSlidersPerViews(slidesPerView, 2) ? rows : 1,

                }

            },
            1200: {
                slidesPerView: getSlidersPerViews(slidesPerView, 3),
                grid: {
                    rows: sliderNumbers > getSlidersPerViews(slidesPerView, 3) ? rows : 1,
                },

            }
        }

    });
}

function getSlidersPerViews(slidesPerView, index) {
    return slidesPerView[index] ? slidesPerView[index] : slidesPerView[slidesPerView.length - 1];
}

