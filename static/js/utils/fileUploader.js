const uploader = document.querySelector('.file-uploader');
const label = document.querySelector('.file-uploader-label')
const span = document.querySelector('.file-uploader-label--rounded-container span') ;

uploader.addEventListener('change', (event) => {
    const value = window.URL.createObjectURL(
    event.currentTarget.files[0]);
    if(!span) {
        label.style.backgroundImage = `url(${value})`;
    }
     span.textContent = event.currentTarget.files[0].name;
});