// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './routers/index'
import settings from './settings'

// 开发配置文件
Vue.config.productionTip = false;
Vue.prototype.$settings = settings;

// 引入element UI
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

// 引入jquery
import $ from 'jquery'

// 引入bootstarp
import './assets/bootstrap-3.3.7-dist/css/bootstrap.css'
import './assets/bootstrap-3.3.7-dist/js/bootstrap'


// 调用插件
Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
