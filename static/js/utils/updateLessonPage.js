export function updateLesson(data, element) {
    element.innerHTML += data.map(item => {
        const {name, title, uni} = item;
        console.log(item)
        return `<div class=" swiper-slide">
                    <div class="p-1 shadow lesson-container">
                        <div class="text-center mb-1 lesson__image-container ">
                            <img src="../../../static/img/index/1200px-University_of_Tehran_logo.png"
                                 class="card-img-top  py-2 lesson__image" alt="">
                        </div>
                        <div class="p-3 lesson__content">
                            <h4 class="lesson__title">${name}</h4>
                            <p class=" ">${title}</p>
                            <p class=" ">${uni}</p>
                        </div>
                    </div>
                </div>`
    }).join('')
}
