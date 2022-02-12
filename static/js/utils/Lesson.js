export default class Lesson {
    constructor(element) {
        this.element = element;
    }

    tableUpdater(data, element) {
        element.innerHTML += data.map(item => {
            const {name, title, uni, image} = item;
            return `<div class="swiper-slide">
                        <div class="p-1 shadow lesson-container">
                            <div class="text-center mb-1 lesson__image-container ">
                                <img src="${image}" class="card-img-top  py-2 lesson__image" alt="">
                            </div>
                            <div class="p-3 lesson__content">
                                <h4 class="lesson__title">${title}</h4>
                                <p class=" ">${name}</p>
                                <p class=" ">${uni}</p>
                            </div>
                        </div>
                    </div>`
        }).join('');
    }
}