import Cookies from 'js-cookie'

export default async (to, from, next) => {
  if (!Cookies.get('token')) {
    next({ name: 'login' })
  } else {
    next()
  }
}
