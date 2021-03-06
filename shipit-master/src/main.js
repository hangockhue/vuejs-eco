// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import vuetify from '@/plugins/vuetify' // path to vuetify export
import store from './vuex'
import App from './App'
import router from './router'
// import {VueSelect} from 'vue-cool-select'
// import 'material-design-icons-iconfont/dist/material-design-icons.css'
import {AutoCompletePlugin} from '@syncfusion/ej2-vue-dropdowns';

Vue.use(AutoCompletePlugin)


// Vue.use(VueSelect, {
//     theme: 'bootstrap'
// })

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  vuetify,
  store,
  components: { App },
  template: '<App/>'
})
