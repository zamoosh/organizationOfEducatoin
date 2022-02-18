export default class Article {
    constructor(element) {
        this.element = element;
    }

    tableUpdater(data) {
        this.element.innerHTML += data.map(item => {
            const {name} = item;
            return `<div class="swiper-slide">
                        <div class=" article">
                            ${name}
                        </div>
                    </div>`
        }).join('');
    }
}