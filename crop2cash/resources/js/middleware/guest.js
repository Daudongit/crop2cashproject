import Cookies from 'js-cookie'

export default (to, from, next) => {
  if (Cookies.get('token')) {
    next({ name: 'dashboard' })
  } else {
    next()
  }
}
