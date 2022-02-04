export default function showAlert({position = 'top-end', timer= 3000, icon="success" , massage="Signed in successfully"}){
  const Toast = Swal.mixin({
  toast: true,
  position: position,
  showConfirmButton: false,
  timer: timer,
  timerProgressBar: true,
  didOpen: (toast) => {
    toast.addEventListener('mouseenter', Swal.stopTimer)
    toast.addEventListener('mouseleave', Swal.resumeTimer)
  }
})

Toast.fire({
  icon: icon,
  title: massage
})


}
