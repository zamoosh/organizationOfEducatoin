export function tableUpdater(data, element) {
    element.innerHTML += data.map(item => {
        const {name, title, uni, image, id} = item;
        return `<div class=" swiper-slide">
                    <a href="/lesson/details/${id}">
                    <div class="p-1 shadow lesson-container">
                        <div class="text-center mb-1 lesson__image-container ">
                            <img src="${image}"
                                 class="card-img-top  py-2 lesson__image" alt="">
                        </div>
                        <div class="p-3 lesson__content">
                            <h4 class="lesson__title">${name}</h4>
                            <p class="">${title}</p>
                            <p class="">${uni}</p>
                        </div>
                    </div>
                    </a>
                </div>`
    }).join('');
}