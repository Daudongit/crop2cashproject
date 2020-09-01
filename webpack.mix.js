let mix = require('laravel-mix');
let staticPath = 'crop2cash/static/build'
let resourcesPath = 'crop2cash/resources'
// setResroucesRoots add prefix to url() in scss on example: from /images/close.svg to /static/images/close.svg
mix.setResourceRoot('/static/build') 
// Path where mix-manifest.json is created
mix.setPublicPath('crop2cash/static') 
// if you don't need browser-sync feature you can remove this lines
if (process.argv.includes('--browser-sync')) {
  mix.browserSync('localhost:8000')
}
// Now you can use full mix api
mix.js(`${resourcesPath}/js/project.js`, `${staticPath}/`)
mix.sass(`${resourcesPath}/sass/project.scss`, `${staticPath}/`)