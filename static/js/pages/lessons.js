import './../utils/sidebar.js';
import swiperSlider from "./../utils/swiperSlider.js";
import {getElement as select} from "./../utils/getElement.js";
import "./../utils/fileUploader.js";
import {tableUpdater} from "../utils/tableUpdater.js";

window.addEventListener('DOMContentLoaded', () => {
    $.ajax({
        url: "/api_lesson/lessons/", success: function (data) {
            const element = $('.lesson-table')[0];
            tableUpdater(data, element);
        }
    });


});
//lesson page
const numbersOfSliders = select('.swiper-slide').length;
// console.log(numbersOfSliders);
swiperSlider("#swiper-lesson", {slidesPerView: [1, 2, 3, 4], rows: 2, sliderNumbers: numbersOfSliders, loop: false});


$(document).ready(function () {
    const form = document.querySelector('.form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const input = $('.form input')[0];
        let data = new FormData($('.form')[0]);
        $.ajax({
            url: "/lesson/save/lesson/",
            type: "POST",
            cache: false,
            processData: false,
            contentType: false,
            mimeType: "multipart/form-data",
            headers: {
                "X-CSRFToken": input.value
            },
            data: data,
            success: function (response) {
                /**
                 * We parse the response to JsonObject because of row 35 (contentType: false)
                 * this would change the response type to String.
                 */
                $('.form').trigger("reset");
                $('input[name="image"]').trigger('reset');
                response = JSON.parse(response);
                if ('status' in response) {
                    if (response['status'] === 'failed')
                        alert('this lesson is already exist!');
                    else if (response['status'] === 'empty')
                        alert('please enter something!');
                } else
                    alert('lesson was added successfully');
                
            }
        });
    });
});