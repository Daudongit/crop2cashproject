import axios from 'axios'
import router from '../router'
import Swal from 'sweetalert2'
import Cookies from 'js-cookie'

// Request interceptor
axios.interceptors.request.use(request => {
  const token = Cookies.get('token')
  if (token) {
    request.headers.common['Authorization'] = `Token ${token}`
  }

  return request
})

// Response interceptor
axios.interceptors.response.use(response => response, error => {
  // const { status } = error.response
  console.log(error.response)

  // if (status >= 500) {
  //   Swal.fire({
  //     type: 'error',
  //     title: 'Error',
  //     text: 'An error oocur',
  //     reverseButtons: true,
  //     confirmButtonText: 'Ok',
  //     cancelButtonText: 'Cancel'
  //   })
  // }

  // if (status === 401 && Cookies.get('token')) {
  //   Swal.fire({
  //     type: 'warning',
  //     title: 'Token expired',
  //     text: 'Your token has expired',
  //     reverseButtons: true,
  //     confirmButtonText: 'Ok',
  //     cancelButtonText: 'Cancel'
  //   }).then(() => {
  //     Cookies.remove('token')

  //     router.push({ name: 'login' })
    // })
  // }

  return Promise.reject(error)
})
