export default class Article {
    tableUpdater(data, element) {
        element.innerHTML += data.map(item => {
            const {name} = item;
            return `<div class="swiper-slide">
                        <div class=" article">
                            ${name}
                        </div>
                    </div>`
        }).join('');
    }
}