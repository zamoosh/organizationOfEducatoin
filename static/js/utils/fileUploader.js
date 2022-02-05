const uploader = document.querySelector('.file-uploader');
const label = document.querySelector('.file-uploader-label');
uploader.addEventListener('change', (event) => {
    const value = window.URL.createObjectURL(
    event.currentTarget.files[0]);
    label.style.backgroundImage = `url(${value})`;
});